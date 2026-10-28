import json
from dataclasses import replace

import pytest

from sincronizacao.dicionario import AVISO_CITADA_TABELA, AVISO_SO_ESTRUTURA, classificar_objetos, escrever_esquema_publicado, gerar_dicionario
from sincronizacao.fonte import carregar_fonte
from sincronizacao.privado import Exclusoes, carregar_exclusoes

VAZIAS = Exclusoes(set(), set(), set())


@pytest.fixture
def fonte_com_tabelas_invalidas(fonte_sintetica):
    return carregar_fonte(fonte_sintetica)


@pytest.fixture
def fonte(fonte_com_tabelas_invalidas):
    f = fonte_com_tabelas_invalidas
    paginas = {k: v for k, v in f.paginas.items() if k != "dimensoes/dim-b.md"}
    return replace(f, paginas=paginas)


def test_selos(fonte):
    c = classificar_objetos(fonte.paginas, fonte.esquema)
    assert c["dbo.TabelaA"]["explicada"] == {"fatos/fato-a.md"}
    assert c["dbo.vwExemplo"]["explicada"] == {"fatos/fato-a.md", "views/views-recomendadas.md"}
    assert c["dbo.vwOutra"]["explicada"] == {"views/views-recomendadas.md"}
    assert not c["dbo.SenhaFicticia"]["explicada"] and not c["dbo.SenhaFicticia"]["citada"]


def test_citada_em_receita(fonte):
    paginas = dict(fonte.paginas)
    r = paginas["receitas/receita-ok.md"]
    paginas["receitas/receita-ok.md"] = replace(r, meta={**r.meta, "tabelas": ["SenhaFicticia"]})
    c = classificar_objetos(paginas, fonte.esquema)
    assert c["dbo.SenhaFicticia"] == {"explicada": set(), "citada": {"receitas/receita-ok.md"}}


def test_item_desconhecido_em_tabelas_falha(fonte_com_tabelas_invalidas):
    f = fonte_com_tabelas_invalidas
    with pytest.raises(ValueError, match=r"item nº 1 de `tabelas:` em dimensoes/dim-b.md"):
        classificar_objetos(f.paginas, f.esquema)


def test_exclusoes_somem_inclusive_das_fks(fonte, tmp_path):
    ex = Exclusoes(tabelas={"dbo.SenhaFicticia", "dbo.TabelaTemp"}, views=set(), colunas={"dbo.TabelaA.colData"})
    n = gerar_dicionario(fonte, ex, tmp_path)
    assert not (tmp_path / "dicionario/dbo-senhaficticia.md").exists()
    assert "colData" not in (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")
    assert n["tabelas"] == len(fonte.esquema.tabelas) - 2
    assert n["fks"] == 1


def test_fk_some_com_tabela_ou_coluna_excluida(fonte, tmp_path):
    ex = Exclusoes({"dbo.TabelaAConcluida"}, set(), set())
    n = gerar_dicionario(fonte, ex, tmp_path)
    assert n["fks"] == 0
    assert "FK_TabelaAConcluida" not in (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")


def test_view_tem_pagina_sem_definicao(fonte, tmp_path):
    gerar_dicionario(fonte, VAZIAS, tmp_path)
    t = (tmp_path / "dicionario/views/dbo-vwexemplo.md").read_text(encoding="utf-8")
    assert "Explicada" in t and "CREATE VIEW" not in t and "Tipos sem tamanho" in t


def test_aviso_so_estrutura_e_indice(fonte, tmp_path):
    gerar_dicionario(fonte, VAZIAS, tmp_path)
    t = (tmp_path / "dicionario/dbo-senhaficticia.md").read_text(encoding="utf-8")
    assert AVISO_SO_ESTRUTURA in t
    assert AVISO_SO_ESTRUTURA not in (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")
    idx = (tmp_path / "dicionario/index.md").read_text(encoding="utf-8")
    assert "Schema dbo" in idx and "Só estrutura: 2" in idx


def test_esquema_publicado(fonte, tmp_path):
    ex = Exclusoes({"dbo.TabelaTemp"}, {"dbo.vwOutra"}, {"dbo.TabelaA.colData"})
    destino = tmp_path / "saida" / "esquema.json"
    escrever_esquema_publicado(fonte, ex, destino)
    d = json.loads(destino.read_text(encoding="utf-8"))
    assert d["tabelas"]["dbo.TabelaA"] == ["id"]
    assert "dbo.TabelaTemp" not in d["tabelas"] and "dbo.vwOutra" not in d["views"]
    assert d["views"]["dbo.vwExemplo"] == ["id", "colData"]


def test_carregar_exclusoes(tmp_path):
    (tmp_path / "exclusoes.json").write_text(
        json.dumps({"tabelas": ["dbo.X"], "views": [], "colunas": ["dbo.X.c"]}), encoding="utf-8"
    )
    ex = carregar_exclusoes(tmp_path)
    assert ex.tabelas == {"dbo.X"} and ex.colunas == {"dbo.X.c"} and ex.views == set()


def test_exclusoes_ausentes_avisam(tmp_path):
    with pytest.warns(UserWarning):
        ex = carregar_exclusoes(tmp_path / "nada")
    assert ex == Exclusoes(set(), set(), set())


# ---- rodada 2: segurança e selos ----

def _todos_textos(raiz):
    arqs = list((raiz / "dicionario").rglob("*.md"))
    assert arqs
    return {a.relative_to(raiz).as_posix(): a.read_text(encoding="utf-8") for a in arqs}


def test_exclusoes_validam_formato(tmp_path):
    (tmp_path / "exclusoes.json").write_text(json.dumps({"tabelas": "dbo.X"}), encoding="utf-8")
    with pytest.raises(ValueError):
        carregar_exclusoes(tmp_path)
    (tmp_path / "exclusoes.json").write_text(json.dumps({"colunas": [1]}), encoding="utf-8")
    with pytest.raises(ValueError):
        carregar_exclusoes(tmp_path)


def test_coluna_exclusa_sem_diferenciar_caixa(fonte, tmp_path):
    ex = Exclusoes(set(), set(), {"dbo.tabelaa.COLDATA"})
    gerar_dicionario(fonte, ex, tmp_path)
    assert "colData" not in (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")
    destino = tmp_path / "e.json"
    escrever_esquema_publicado(fonte, ex, destino)
    assert json.loads(destino.read_text(encoding="utf-8"))["tabelas"]["dbo.TabelaA"] == ["id"]


def test_nome_curto_resolve_para_dbo(fonte, tmp_path):
    ex = Exclusoes({"senhaficticia"}, set(), {"TabelaA.colData"})
    gerar_dicionario(fonte, ex, tmp_path)
    assert not (tmp_path / "dicionario/dbo-senhaficticia.md").exists()


@pytest.mark.parametrize("ex", [
    Exclusoes({"dbo.NaoExiste"}, set(), set()),
    Exclusoes(set(), {"dbo.NaoExiste"}, set()),
    Exclusoes(set(), set(), {"dbo.TabelaA.naoExiste"}),
    Exclusoes(set(), set(), {"dbo.NaoExiste.id"}),
])
def test_exclusao_sem_correspondencia_levanta(fonte, tmp_path, ex):
    with pytest.raises(ValueError, match=r"exclusão nº 1 de .* sem correspondência"):
        gerar_dicionario(fonte, ex, tmp_path)
    with pytest.raises(ValueError, match=r"exclusão nº 1 de .* sem correspondência"):
        escrever_esquema_publicado(fonte, ex, tmp_path / "x.json")


def test_nome_da_fk_nao_e_publicado(fonte, tmp_path):
    gerar_dicionario(fonte, VAZIAS, tmp_path)
    for nome, t in _todos_textos(tmp_path).items():
        assert "FK_TabelaAConcluida_TabelaA" not in t, nome
    assert "dbo.TabelaAConcluida" in (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")


def test_nenhum_nome_excluido_em_nenhum_arquivo(fonte, tmp_path):
    ex = Exclusoes({"dbo.SenhaFicticia", "dbo.TabelaTemp"}, set(), {"dbo.TabelaA.colData", "dbo.vwExemplo.colData"})
    gerar_dicionario(fonte, ex, tmp_path)
    for nome, t in _todos_textos(tmp_path).items():
        for proibido in ("TabelaTemp", "SenhaFicticia", "colData"):
            assert proibido.lower() not in t.lower(), (nome, proibido)


def test_coluna_ponta_de_fk_remove_fk(fonte, tmp_path):
    n = gerar_dicionario(fonte, Exclusoes(set(), set(), {"dbo.TabelaA.id"}), tmp_path)
    assert n["fks"] == 0
    for p in ("dbo-tabelaa.md", "dbo-tabelaaconcluida.md"):
        assert "Chaves estrangeiras" not in (tmp_path / "dicionario" / p).read_text(encoding="utf-8")


def test_view_excluida_sem_pagina_e_sem_indice(fonte, tmp_path):
    n = gerar_dicionario(fonte, Exclusoes(set(), {"dbo.vwOutra"}, set()), tmp_path)
    assert n["views"] == 1
    assert not (tmp_path / "dicionario/views/dbo-vwoutra.md").exists()
    assert "vwOutra" not in (tmp_path / "dicionario/index.md").read_text(encoding="utf-8")


def test_coluna_de_view_excluida(fonte, tmp_path):
    gerar_dicionario(fonte, Exclusoes(set(), set(), {"dbo.vwExemplo.colData"}), tmp_path)
    assert "colData" not in (tmp_path / "dicionario/views/dbo-vwexemplo.md").read_text(encoding="utf-8")


def test_links_dos_selos(fonte, tmp_path):
    gerar_dicionario(fonte, VAZIAS, tmp_path, publicadas={"fatos/fato-a.md": "Fato: A", "views/views-recomendadas.md": "Views recomendadas"})
    t = (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")
    assert "[A](../fatos/fato-a.md)" in t and "[fatos/fato-a.md]" not in t
    v = (tmp_path / "dicionario/views/dbo-vwexemplo.md").read_text(encoding="utf-8")
    assert "(../../fatos/fato-a.md)" in v and "[Views recomendadas](../../views/views-recomendadas.md)" in v


def test_sem_publicadas_nao_ha_links(fonte, tmp_path):
    gerar_dicionario(fonte, VAZIAS, tmp_path)
    t = (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")
    assert "fato-a.md" not in t and "Explicada" in t


def test_pagina_barrada_rebaixa_selo(fonte, tmp_path):
    gerar_dicionario(fonte, VAZIAS, tmp_path, publicadas={})
    t = (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")
    assert "fato-a.md" not in t and AVISO_SO_ESTRUTURA in t
    paginas = dict(fonte.paginas)
    r = paginas["receitas/receita-ok.md"]
    paginas["receitas/receita-ok.md"] = replace(r, meta={**r.meta, "tabelas": ["TabelaA"]})
    f2 = replace(fonte, paginas=paginas)
    gerar_dicionario(f2, VAZIAS, tmp_path, publicadas={"receitas/receita-ok.md": "Receita: OK"})
    t = (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")
    assert "Selo:** Citada" in t and AVISO_CITADA_TABELA in t and "[OK](../receitas/receita-ok.md)" in t


def test_aviso_citada_view(fonte, tmp_path):
    paginas = dict(fonte.paginas)
    r = paginas["receitas/receita-ok.md"]
    paginas["receitas/receita-ok.md"] = replace(r, meta={**r.meta, "tabelas": ["vwOutra"]})
    f2 = replace(fonte, paginas=paginas)
    gerar_dicionario(f2, VAZIAS, tmp_path, publicadas={"receitas/receita-ok.md": "Receita: OK"})
    v = (tmp_path / "dicionario/views/dbo-vwoutra.md").read_text(encoding="utf-8")
    assert AVISO_CITADA_TABELA.replace("Esta tabela", "Esta view") in v


def test_indice_ordenado_e_front_matter_e_sem_crases(fonte, tmp_path):
    gerar_dicionario(fonte, VAZIAS, tmp_path)
    idx = (tmp_path / "dicionario/index.md").read_text(encoding="utf-8")
    nomes = [l.split("[")[1].split("]")[0] for l in idx.splitlines() if l.startswith("- [")]
    assert nomes == sorted(nomes, key=str.lower)
    assert "## Schema dbo" in idx
    for nome, t in _todos_textos(tmp_path).items():
        assert t.startswith("---\ngerado: sincronizacao\n---\n"), nome
        assert "<!--" not in t
    assert "`int`" not in (tmp_path / "dicionario/dbo-tabelaa.md").read_text(encoding="utf-8")


def test_chave_desconhecida_em_exclusoes(tmp_path):
    (tmp_path / "exclusoes.json").write_text(
        json.dumps({"tabelas": [], "coluna": ["dbo.X.y"]}), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="chave desconhecida em exclusoes.json: coluna"):
        carregar_exclusoes(tmp_path)


def test_nota_tipos_sem_crases(fonte, tmp_path):
    gerar_dicionario(fonte, VAZIAS, tmp_path)
    v = (tmp_path / "dicionario/views/dbo-vwexemplo.md").read_text(encoding="utf-8")
    assert "varchar" in v and "`varchar`" not in v


def _com_tabelas_extras(fonte, extras):
    esq = replace(fonte.esquema, tabelas={**fonte.esquema.tabelas, **extras})
    return replace(fonte, esquema=esq)


def test_nome_de_arquivo_kebab_sem_sublinhado(fonte, tmp_path):
    col = [{"nome": "id", "tipo": "int", "nulo": False, "pk": True, "computada": False}]
    f = _com_tabelas_extras(fonte, {"dbo.Modulo_Item": col})
    gerar_dicionario(f, VAZIAS, tmp_path)
    assert (tmp_path / "dicionario/dbo-modulo-item.md").exists()
    idx = (tmp_path / "dicionario/index.md").read_text(encoding="utf-8")
    assert "[dbo.Modulo_Item](dbo-modulo-item.md)" in idx
    for p in (tmp_path / "dicionario").rglob("*.md"):
        assert "_" not in p.name


def test_colisao_de_nome_de_arquivo(fonte, tmp_path):
    col = [{"nome": "id", "tipo": "int", "nulo": False, "pk": True, "computada": False}]
    f = _com_tabelas_extras(fonte, {"dbo.A_B": col, "dbo.A-B": col})
    with pytest.raises(ValueError, match=r"dbo\.A_B.*dbo\.A-B"):
        gerar_dicionario(f, VAZIAS, tmp_path)
