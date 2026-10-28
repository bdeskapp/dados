import json
from pathlib import Path

import pytest
import yaml

from sincronizacao.derivadas import (
    aplicar_nav, chaves_dominios, gerar_dominios, gerar_limitacoes, gerar_nav, gerar_versao, titulo_nav,
)
from sincronizacao.fonte import carregar_fonte
from sincronizacao.portao import Politica

MODELO = Path(__file__).resolve().parent.parent / "sincronizacao" / "mkdocs.modelo.yml"


@pytest.fixture
def fonte(fonte_sintetica):
    return carregar_fonte(fonte_sintetica)


def test_dominios_sem_origem_e_com_aviso(fonte):
    t = gerar_dominios(fonte.dominios_md)
    assert "| origem" not in t and "origem" not in t.split("## ")[1]
    assert '!!! warning "Valores de referência"' in t and "<!-- gerado" not in t
    assert t.startswith("---\ngerado: sincronizacao\n---\n# Domínios do produto")
    assert "| 1 | Aberto | ativo |" in t


def test_dominios_sem_categoria_falha():
    with pytest.raises(ValueError, match="categoria"):
        gerar_dominios("## X\n\n| chave | rótulo | origem |\n|---|---|---|\n| `1` | A | z |\n")


def test_dominios_cabecalho_sem_rotulo():
    t = gerar_dominios("## X\n\n| chave | categoria | origem |\n|---|---|---|\n| `1` | c | z |\n")
    assert "| chave | categoria |" in t and "origem" not in t.split("## X")[1]


def test_chaves_dominios(fonte):
    assert chaves_dominios(fonte.dominios_md) == ["1", "2"]
    assert chaves_dominios("| chave | categoria | origem |\n|---|---|---|\n| `ABC` | c | z |\n") == ["ABC"]


def test_limitacoes_so_abertas(fonte):
    md, abertas, decididas = gerar_limitacoes(fonte.paginas["pendencias-abertas.md"])
    assert abertas == {"07"} and decididas == {"05"} and "{#l-07}" in md and "PEND-05" not in md
    assert md.startswith("---\ngerado: sincronizacao\n---\n")
    assert "colData" in md and "R-fato-a-02" in md


def test_limitacoes_vazia():
    from sincronizacao.fonte import Pagina
    md, a, d = gerar_limitacoes(Pagina("p.md", {}, "# x\n"))
    assert "Não há limitação registrada nesta versão." in md and not a and not d


def test_versao():
    pol = Politica("a" * 40, {"a"}, {"c"}, {"b", "d"}, set())
    t = gerar_versao(pol, "9.9", "2030-01-01", {"tabelas": 3}, {"c": "Receita C"})
    assert t.startswith("---\ngerado: sincronizacao\n---\n")
    assert "a" * 12 in t and "a" * 13 not in t and "Receita C" in t and "tabelas: 3" in t
    assert "2 " not in t.split("Receitas em revisão")[1].split("Receita C")[0] and "não publicadas" in t


def test_titulo_nav():
    assert titulo_nav("Fato: A") == "A" and titulo_nav("Fora de escopo: X") == "X" and titulo_nav("Y") == "Y"


def test_nav_ordem_e_dicionario_fora():
    y = gerar_nav({"mapa/regras-essenciais.md": "Regras essenciais", "dicionario/dbo-tabelaa.md": "TabelaA", "fatos/fato-a.md": "Fato: A"})
    assert "dicionario/dbo-tabelaa.md" not in y and '"A": fatos/fato-a.md' in y
    assert all(l.startswith("  ") for l in y.splitlines())


def test_nav_secoes_proprias_e_omitidas():
    y = gerar_nav({
        "comece-aqui/regras-de-ouro.md": "Regras de ouro",
        "comece-aqui/modelo-em-5-minutos.md": "Modelo: em 5 minutos",
        "fatos/fato-a.md": "Fato: A",
    })
    assert y.index("modelo-em-5-minutos") < y.index("regras-de-ouro")
    assert '"Consumo"' not in y and '"Comece aqui"' in y and '"Modelo: em 5 minutos"' in y


def _loader():
    class L(yaml.SafeLoader):
        pass
    L.add_multi_constructor("tag:yaml.org,2002:python/name:", lambda l, suf, n: suf)
    return L


def test_aplicar_nav_modelo_real():
    nav = gerar_nav({
        "comece-aqui/regras-de-ouro.md": "Regras de ouro",
        "mapa/regras-essenciais.md": "Regras essenciais",
        "fatos/fato-a.md": "Fato: A",
        "dicionario/index.md": "Dicionário",
        "sobre/versao.md": "Versão",
    })
    out = aplicar_nav(MODELO.read_text(encoding="utf-8"), nav)
    assert "{{NAV_GERADO}}" not in out
    n = yaml.load(out, Loader=_loader())["nav"]
    assert n[0] == {"Início": "index.md"}
    assert [list(s)[0] for s in n[1:]] == ["Comece aqui", "Modelo", "Fatos", "Referência"]


def test_dominios_remove_marcadores_gerado():
    entrada = (
        "<!-- gerado:dominios-fonte.json -->\n# T\n\n## D\n\n"
        "| chave | categoria | origem |\n|---|---|---|\n| `1` | c | z |\n\n<!-- /gerado -->\n"
    )
    assert "<!--" not in gerar_dominios(entrada)
    assert chaves_dominios(entrada) == ["1"]
