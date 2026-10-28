import json
import re

import pytest

from sincronizacao import vazamento
from sincronizacao.vazamento import (
    Listas,
    listas_completas,
    listas_genericas,
    main,
    verificar_arvore,
    verificar_html,
    verificar_markdown,
)


def _escrever_esquema(raiz):
    (raiz / "sincronizacao").mkdir(parents=True, exist_ok=True)
    esquema = {
        "tabelas": {
            "dbo.TabelaA": ["colData", "colValor", "colStatus"],
            "dbo.TabelaB": ["colId", "colNome"],
        },
        "views": {"dbo.vwExemplo": ["colTotal"]},
    }
    (raiz / "sincronizacao" / "esquema-publicado.json").write_text(
        json.dumps(esquema), encoding="utf-8"
    )


@pytest.fixture
def listas(tmp_path) -> Listas:
    _escrever_esquema(tmp_path)
    return listas_genericas(tmp_path)


# Testes do plano


def test_codigo_sem_marcador_na_prosa_e_barrado(listas):
    a = verificar_markdown("O total é gravado por `ClasseFicticia.Metodo` toda noite.", "x.md", listas)
    assert [x.categoria for x in a] == ["fora-da-lista"]


def test_tabela_e_coluna_publicadas_passam(listas):
    assert verificar_markdown("Use `TabelaA.colData` e `vwExemplo`.", "x.md", listas) == []


def test_arquivo_e_linha(listas):
    cats = {x.categoria for x in verificar_markdown("ver Pasta/Arq.cls:12", "x.md", listas)}
    assert "arquivo-de-codigo" in cats


def test_rotina_em_sql(listas):
    assert any(x.categoria == "rotina" for x in verificar_markdown("```sql\nEXEC uspFicticia\n```", "x.md", listas))


def test_comentario_html_no_site(listas):
    assert verificar_html("<p>ok</p><!-- gerado:arq.json -->", "site/x.html", listas)


def test_modo_generico_nao_ecoa_trecho(tmp_path, capsys):
    (tmp_path / "docs").mkdir(); (tmp_path / "docs/x.md").write_text("Use `SegredoFicticio.cls:9`.", encoding="utf-8")
    assert main([str(tmp_path / "docs")]) == 1
    out = capsys.readouterr().out
    assert "x.md:1" in out and "SegredoFicticio" not in out


# Prosa em pt-BR


def test_prosa_ptbr_sem_falso_positivo(listas):
    texto = (
        "Some as requisições abertas e encerradas para qualquer volume histórico; "
        "use `TabelaA.colData`.\n"
        "\n"
        "Você pode filtrar por período e/ou por situação, p.ex. de 01/02/2026 às 10:30. "
        "Veja a [página de fatos](../fatos/requisicoes.md#visao-geral) e o "
        "**dicionário** de _TabelaA_.\n"
        "\n"
        '!!! note "Atenção"\n'
        "    Os valores de `colStatus` são `'A'` e `'F'`; `colValor IS NULL` indica ausência.\n"
    )
    assert verificar_markdown(texto, "x.md", listas, profundidade=1) == []


def test_sql_do_leitor_com_apelidos_e_comentarios_passa(listas):
    texto = (
        "```sql\n"
        "-- Some as requisições abertas por mês\n"
        "WITH base AS (\n"
        "    SELECT a.colData, a.colValor AS valor, b.colNome\n"
        "    FROM dbo.TabelaA a WITH (NOLOCK)\n"
        "    INNER JOIN dbo.TabelaB AS b ON b.colId = a.colStatus\n"
        "    WHERE a.colData >= DATEADD(day, -30, GETDATE()) AND a.colStatus = 'A'\n"
        ")\n"
        "SELECT colNome, COUNT(*) qtd, SUM(valor) total\n"
        "FROM base\n"
        "GROUP BY colNome\n"
        "ORDER BY total DESC;\n"
        "```\n"
    )
    assert verificar_markdown(texto, "x.md", listas) == []


def test_identificador_desconhecido_em_sql(listas):
    a = verificar_markdown("Texto.\n\n```sql\nSELECT colSecreta FROM dbo.TabelaA\n```\n", "x.md", listas)
    assert [(x.linha, x.categoria) for x in a] == [(4, "fora-da-lista")]


def test_camelcase_sem_crase_na_prosa(listas):
    a = verificar_markdown("O valor vem de ClasseFicticia toda noite.", "x.md", listas)
    assert [x.categoria for x in a] == ["fora-da-lista"]


def test_definicao_de_view(listas):
    texto = "```sql\nCREATE VIEW dbo.vwExemplo AS SELECT colData FROM TabelaA\n```"
    assert any(x.categoria == "definicao-de-view" for x in verificar_markdown(texto, "x.md", listas))


def test_numero_de_linha_em_crase(listas):
    cats = {x.categoria for x in verificar_markdown("Veja `TabelaA:42` e `:7`.", "x.md", listas)}
    assert "numero-de-linha" in cats


@pytest.mark.parametrize("marcador", ["<!-- prova -->x<!-- /prova -->", "<!-- decisao -->", "<!-- ficticio -->"])
def test_marcadores_nunca_sobram(listas, marcador):
    a = verificar_markdown(f"Texto comum {marcador} aqui.", "x.md", listas)
    assert "marcador" in {x.categoria for x in a}


def test_marcador_em_comentario_html(listas):
    a = verificar_html("<p>ok</p>\n<!-- prova -->\n", "site/x.html", listas)
    assert [(x.linha, x.categoria) for x in a] == [(2, "marcador")]


def test_html_com_codigo_publicado_passa(listas):
    html = (
        "<html><head><script>var segredoFicticio_x = 1;</script>"
        "<style>.md-x{color:red}</style></head><body>\n"
        "<p>Some as requisições abertas; use <code>TabelaA.colData</code>.</p>\n"
        '<div class="language-sql highlight"><pre><span></span><code>'
        '<span class="k">SELECT</span> <span class="n">t</span>.<span class="n">colData</span>\n'
        '<span class="k">FROM</span> <span class="n">TabelaA</span> <span class="n">t</span>\n'
        "</code></pre></div>\n"
        "</body></html>"
    )
    assert verificar_html(html, "site/x.html", listas) == []


def test_html_rotina_e_linha(listas):
    html = "<p>a</p>\n<p>b</p>\n<p>Chamado por <code>uspFicticia</code>.</p>"
    a = verificar_html(html, "site/x.html", listas)
    assert (3, "rotina") in {(x.linha, x.categoria) for x in a}


def test_dominio_publicado(tmp_path):
    _escrever_esquema(tmp_path)
    (tmp_path / "sincronizacao" / "dominios-publicados.json").write_text(
        json.dumps(["SituacaoFicticia"]), encoding="utf-8"
    )
    texto = "O domínio `SituacaoFicticia` agrupa os estados."
    assert verificar_markdown(texto, "x.md", listas_genericas(tmp_path)) == []
    sem = tmp_path / "outra"
    _escrever_esquema(sem)
    assert verificar_markdown(texto, "x.md", listas_genericas(sem))


def _montar_privado_e_fonte(tmp_path, exclusoes=None):
    raiz = tmp_path / "site-repo"
    _escrever_esquema(raiz)
    privado = raiz / "sincronizacao" / "privado"
    privado.mkdir()
    (privado / "bloqueio.json").write_text(json.dumps({"padroes": [r"servidor-ficticio\d+"]}), encoding="utf-8")
    if exclusoes is not None:
        (privado / "exclusoes.json").write_text(json.dumps(exclusoes), encoding="utf-8")
    fonte = tmp_path / "fonte"
    (fonte / "Database" / "docs" / "_manutencao").mkdir(parents=True)
    (fonte / "Database" / "docs" / "_manutencao" / "excecoes.json").write_text(
        json.dumps(
            {
                "nomesDeCliente": ["ClienteFicticio", "Abc"],
                "variaveisDeCodigo": {"rsFicticio": "x"},
                "termosInternos": ["TecFicticia"],
            }
        ),
        encoding="utf-8",
    )
    return raiz, fonte


def test_listas_completas_com_privado_e_fonte(tmp_path):
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    listas = listas_completas(raiz, fonte)
    texto = (
        "Rodou no servidor-ficticio01.\n"
        "Pedido do ClienteFicticio.\n"
        "Lido em rsFicticio.\n"
        "Feito em TecFicticia.\n"
        "Termo clientefictício também é barrado, assim como ClienteFicticioX.\n"
        "A sigla Abc é barrada, mas abcdef não.\n"
    )
    achados = verificar_markdown(texto, "x.md", listas)
    por_linha = {(x.linha, x.categoria) for x in achados}
    assert (1, "bloqueio-privado") in por_linha
    assert (2, "bloqueio-privado") in por_linha
    assert (3, "bloqueio-privado") in por_linha
    assert (4, "jargao") in por_linha
    assert (5, "bloqueio-privado") in por_linha
    assert [x.trecho for x in achados if x.linha == 6 and x.categoria == "bloqueio-privado"] == ["Abc"]

    genericas = listas_genericas(raiz)
    assert genericas.bloqueio == []
    assert listas_completas(raiz, None).bloqueio  # só o bloqueio privado


def test_listas_completas_sem_privado_nem_fonte(tmp_path):
    _escrever_esquema(tmp_path)
    listas = listas_completas(tmp_path, tmp_path / "inexistente")
    assert listas.bloqueio == []


def test_verificar_arvore_site(tmp_path, listas):
    site = tmp_path / "site"
    (site / "search").mkdir(parents=True)
    (site / "index.html").write_text("<p>Use <code>TabelaA.colData</code>.</p>", encoding="utf-8")
    (site / "search" / "search_index.json").write_text(
        json.dumps(
            {
                "config": {},
                "docs": [
                    {"location": "", "title": "Início", "text": "<p>ok</p>"},
                    {"location": "x/", "title": "X", "text": "<p>Ver <code>ClasseFicticia.cls:3</code></p>"},
                ],
            }
        ),
        encoding="utf-8",
    )
    achados = verificar_arvore(site, listas)
    assert achados
    assert {x.caminho for x in achados} == {"site/search/search_index.json"}
    assert {x.linha for x in achados} == {2}


def test_main_completo_mostra_trecho_e_sem_achados_sai_zero(tmp_path, capsys, monkeypatch):
    monkeypatch.delenv("BDESK_FONTE", raising=False)
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    monkeypatch.setattr(vazamento, "RAIZ", raiz)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "x.md").write_text("Use `SegredoFicticio.cls:9`.", encoding="utf-8")
    assert main(["--completo", "--fonte", str(fonte), str(docs)]) == 1
    assert "SegredoFicticio" in capsys.readouterr().out
    (docs / "x.md").write_text("Texto em português sem identificadores.", encoding="utf-8")
    assert main(["--completo", "--fonte", str(fonte), str(docs)]) == 0
    assert main([str(docs)]) == 0


# ---------------------------------------------------------------------------
# Revisão 1: um teste negativo por bypass
# ---------------------------------------------------------------------------


def _categorias(texto, listas, caminho="x.md"):
    return {x.categoria for x in verificar_markdown(texto, caminho, listas)}


def _trechos(achados, categoria="fora-da-lista"):
    return {x.trecho for x in achados if x.categoria == categoria}


# 1. <...> nunca verificado


def test_generico_entre_sinais_no_markdown(listas):
    assert "ClasseInterna" in _trechos(verificar_markdown("Devolve uma List<ClasseInterna> pronta.", "x.md", listas))


def test_sinais_escapados_no_markdown(listas):
    achados = verificar_markdown(r"Devolve \<ClasseInterna\> pronta.", "x.md", listas)
    assert any("ClasseInterna" in t for t in _trechos(achados))


def test_atributo_title_no_markdown(listas):
    achados = verificar_markdown('Veja <span title="Classe.Metodo">aqui</span>.', "x.md", listas)
    assert "Classe.Metodo" in _trechos(achados)


def test_tag_html_conhecida_no_markdown_passa(listas):
    texto = '<div markdown class="grid"><span title="Data de abertura">Use <b>TabelaA</b></span></div>'
    assert verificar_markdown(texto, "x.md", listas) == []


def test_entidade_html_no_site(listas):
    achados = verificar_html("<p>Devolve &lt;ClasseInterna&gt; pronta.</p>", "site/x.html", listas)
    assert "ClasseInterna" in _trechos(achados)


def test_atributos_no_site(listas):
    html = '<p><a title="Classe.Metodo" href="https://dev.azure.com/org/_git/repo">ok</a>\n<img alt="ClasseInterna" src="Arq.cls"></p>'
    achados = verificar_html(html, "site/x.html", listas)
    assert (1, "fora-da-lista") in {(x.linha, x.categoria) for x in achados}
    assert (1, "arquivo-de-codigo") in {(x.linha, x.categoria) for x in achados}
    assert {(2, "fora-da-lista"), (2, "arquivo-de-codigo")} <= {(x.linha, x.categoria) for x in achados}


# 2. Cercas que não são SQL


def test_cerca_de_linguagem_nao_permitida(listas):
    achados = verificar_markdown("Texto.\n\n```python\nx = 1\n```\n", "x.md", listas)
    assert [(x.linha, x.categoria) for x in achados] == [(3, "trecho-de-codigo")]


@pytest.mark.parametrize("linguagem", ["", "text", "json", "console", "mermaid", "sql", "tsql"])
def test_cercas_permitidas(listas, linguagem):
    assert verificar_markdown(f"```{linguagem}\nTabelaA\n```\n", "x.md", listas) == []


def test_info_da_cerca_e_verificada(listas):
    achados = verificar_markdown('```text title="Src/Modulo/Classe"\nok\n```\n', "x.md", listas)
    assert "Src/Modulo/Classe" in _trechos(achados)


# 3. Literais de string no SQL


def test_literal_de_string_no_sql(listas):
    achados = verificar_markdown("```sql\nSELECT colData FROM TabelaA WHERE colStatus = 'frmRequisicao.frm'\n```", "x.md", listas)
    assert "arquivo-de-codigo" in {x.categoria for x in achados}
    assert "frmRequisicao.frm" in _trechos(achados)


# 4. --completo sem fallback silencioso


def test_completo_exige_bloqueio_fonte_e_excecoes(tmp_path, monkeypatch, capsys):
    monkeypatch.delenv("BDESK_FONTE", raising=False)
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    monkeypatch.setattr(vazamento, "RAIZ", raiz)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "x.md").write_text("Texto.", encoding="utf-8")
    assert main(["--completo", str(docs)]) == 2
    (raiz / "sincronizacao" / "privado" / "exclusoes.json").unlink()
    assert main(["--completo", "--fonte", str(fonte), str(docs)]) == 2
    (raiz / "sincronizacao" / "privado" / "exclusoes.json").write_text("{}", encoding="utf-8")
    assert main(["--completo", "--fonte", str(fonte), str(docs)]) == 0
    (fonte / "Database" / "docs" / "_manutencao" / "excecoes.json").unlink()
    assert main(["--completo", "--fonte", str(fonte), str(docs)]) == 2
    _montar_privado_e_fonte(tmp_path / "b", exclusoes={})
    outra_fonte = tmp_path / "b" / "fonte"
    (raiz / "sincronizacao" / "privado" / "bloqueio.json").unlink()
    assert main(["--completo", "--fonte", str(outra_fonte), str(docs)]) == 2
    assert capsys.readouterr().err


# 5. Nome de cliente embutido


@pytest.mark.parametrize("texto", ["Use `vwVendasClienteFicticio`.", "Relatório ClienteFicticio_Rel.", "A CLIENTEFICTÍCIO pediu."])
def test_nome_de_cliente_embutido(tmp_path, texto):
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    assert "bloqueio-privado" in _categorias(texto, listas_completas(raiz, fonte))


# 6. Exclusões no bloqueio


def test_exclusoes_entram_no_bloqueio(tmp_path):
    raiz, fonte = _montar_privado_e_fonte(
        tmp_path,
        exclusoes={"tabelas": ["dbo.TabelaOculta"], "views": ["dbo.vwOculta"], "colunas": ["dbo.TabelaA.colOculta"]},
    )
    listas = listas_completas(raiz, fonte)
    texto = "A tabelaoculta.\nA vwOculta.\nA coluna COLOCULTA.\nA colOcultaX passa no bloqueio.\n"
    achados = verificar_markdown(texto, "x.md", listas)
    linhas = {x.linha for x in achados if x.categoria == "bloqueio-privado"}
    assert linhas == {1, 2, 3}


# 7. Apelidos SQL


def test_apelido_implicito_no_select_nao_e_aceito(listas):
    achados = verificar_markdown("```sql\nSELECT colData ClasseInterna, 1 ProcessarFila FROM TabelaA\n```", "x.md", listas)
    assert {"ClasseInterna", "ProcessarFila"} <= _trechos(achados)


def test_apelido_invalido_no_from(listas):
    achados = verificar_markdown("```sql\nSELECT colData FROM TabelaA ClasseInterna\n```", "x.md", listas)
    assert "ClasseInterna" in _trechos(achados)


def test_qualificador_sem_apelido_definido_no_sql(listas):
    achados = verificar_markdown("```sql\nSELECT x.colData FROM TabelaA\n```", "x.md", listas)
    assert "x.colData" in _trechos(achados)


def test_apelido_vale_so_no_mesmo_bloco(listas):
    texto = "```sql\nSELECT t.colData FROM TabelaA t\n```\n\n```sql\nSELECT t.colData FROM TabelaB\n```\n"
    achados = verificar_markdown(texto, "x.md", listas)
    assert [(x.linha, x.trecho) for x in achados] == [(6, "t.colData")]


# 8. Crases alinhadas com a fonte


def test_palavra_comum_em_crase_passa(listas):
    assert verificar_markdown("A situação `encerrada` e `ADO` aparecem.", "x.md", listas) == []


def test_identificador_em_crase_e_barrado(listas):
    assert _trechos(verificar_markdown("Ver `ClasseInterna`.", "x.md", listas)) == {"ClasseInterna"}


def test_prefixo_de_coluna_em_crase(listas):
    assert "dtFicticia" in _trechos(verificar_markdown("Ver `dtFicticia`.", "x.md", listas))


# 9. Rotina em qualquer caixa


@pytest.mark.parametrize("nome", ["uspprocessafila", "SPPROCESSAFILA", "sp_processa", "TRG_FILA"])
def test_rotina_em_qualquer_caixa(listas, nome):
    assert "rotina" in _categorias(f"Chamado por {nome} toda noite.", listas)
    assert "rotina" in _categorias(f"Chamado por `{nome}` toda noite.", listas)


# 10. Mais três bypasses


@pytest.mark.parametrize("texto", ["Use `@Classe.Metodo`.", "Use `#L120`.", "Use `'Classe.Metodo'`."])
def test_bypass_em_crase(listas, texto):
    assert verificar_markdown(texto, "x.md", listas)


@pytest.mark.parametrize("texto", ["Grava via Dal.Insert.", "Grava via `Svc.Execute`.", "Grava via `t.Insert`.", "Grava via t.Insert."])
def test_qualificado_fora_do_sql(listas, texto):
    assert "fora-da-lista" in _categorias(texto, listas)


def test_variavel_simples_em_crase_passa(listas):
    assert verificar_markdown("Defina `@DataInicio` e `#temporaria`.", "x.md", listas) == []


def test_qualificado_minusculo_com_coluna_publicada_passa(listas):
    assert verificar_markdown("Filtre por `t.colData` e t.colValor.", "x.md", listas) == []


# 11. URLs e linhas


@pytest.mark.parametrize(
    "url",
    [
        "https://dev.azure.com/org/proj/_git/repo",
        "https://github.com/org/repo/blob/main/x",
        "https://github.com/org/repo/tree/main/pasta",
        "https://dev.azure.com/org/proj?path=/pasta&version=GB",
    ],
)
def test_url_de_repositorio(listas, url):
    assert "arquivo-de-codigo" in _categorias(f"Veja {url} e [isto]({url}).", listas)


@pytest.mark.parametrize("alvo", ["../src/Classe", "pasta/arquivo", "..", "x.txt"])
def test_alvo_de_link_relativo_suspeito(listas, alvo):
    assert "arquivo-de-codigo" in _categorias(f"Veja [isto]({alvo}).", listas)


@pytest.mark.parametrize("alvo", ["../fatos/x.md", "../fatos/x.md#visao", "../fatos/", "#visao-geral", "https://bdeskapp.github.io/dados/"])
def test_alvo_de_link_aceito(listas, alvo):
    assert verificar_markdown(f"Veja [isto]({alvo}).", "x.md", listas, profundidade=1) == []


@pytest.mark.parametrize("texto", ["Ver as linhas 10 a 20.", "Na linha 12 do arquivo.", "Ver linhas 3–9.", "Trecho #L45."])
def test_referencia_a_linha(listas, texto):
    assert "numero-de-linha" in _categorias(texto, listas)


# 12. Tipos de arquivo publicados


@pytest.mark.parametrize("nome", ["a.svg", "a.txt", "a.csv", "a.yml", "a.yaml", "dados.json"])
def test_arvore_verifica_outros_tipos(tmp_path, listas, nome):
    site = tmp_path / "site"
    site.mkdir()
    conteudo = "<svg><text>ClasseInterna</text></svg>" if nome.endswith(".svg") else "valor: ClasseInterna\n"
    (site / nome).write_text(conteudo, encoding="utf-8")
    assert {x.caminho for x in verificar_arvore(site, listas)} == {f"site/{nome}"}


# Endurecimento


def test_trecho_fora_do_repr():
    assert "SegredoFicticio" not in repr(vazamento.Achado("x.md", 1, "rotina", "SegredoFicticio"))


def test_arquivo_e_linha_tem_numero_de_linha(listas):
    cats = {x.categoria for x in verificar_markdown("ver Pasta/Arq.cls:12", "x.md", listas)}
    assert "numero-de-linha" in cats


_TODAS = {
    "fora-da-lista", "arquivo-de-codigo", "numero-de-linha", "rotina", "bloqueio-privado",
    "definicao-de-view", "jargao", "marcador", "trecho-de-codigo",
}

_TEXTO_TODAS = (
    "SegredoUmFicticio grava em SegredoDois.cls:12 via uspSegredoTres.\n"
    "<!-- prova -->servidor-ficticio07 do ClienteFicticio usa TecFicticia.\n"
    "```python\nsegredo_quatro = 1\n```\n"
    "```sql\nCREATE VIEW dbo.vwExemplo AS SELECT colData FROM TabelaA\n```\n"
)


def test_modo_generico_nao_ecoa_trecho_de_nenhuma_categoria(tmp_path, capsys, monkeypatch):
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    achados = verificar_markdown(_TEXTO_TODAS, "x.md", listas_completas(raiz, fonte))
    assert {x.categoria for x in achados} == _TODAS
    vazamento.imprimir(achados, completo=False)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "x.md").write_text(_TEXTO_TODAS, encoding="utf-8")
    monkeypatch.setattr(vazamento, "RAIZ", raiz)
    assert main([str(docs)]) == 1
    saida = capsys.readouterr()
    linhas = saida.out.splitlines()
    assert linhas
    formato = re.compile(r"(?:docs/)?x\.md:\d+ (?:" + "|".join(map(re.escape, vazamento.CATEGORIAS)) + ")")
    for linha in linhas:
        assert formato.fullmatch(linha), linha
    assert saida.err == ""


# ---------------------------------------------------------------------------
# Revisão 2
# ---------------------------------------------------------------------------

# 1. HTML residual


@pytest.mark.parametrize("texto", ["Veja <span ClasseInterna>aqui</span>.", "Veja <p.ClasseInterna>aqui."])
def test_html_residual_no_markdown(listas, texto):
    assert any("ClasseInterna" in t for t in _trechos(verificar_markdown(texto, "x.md", listas)))


@pytest.mark.parametrize("texto", ["<p>Veja <span ClasseInterna>aqui</span>.</p>", "<p>Veja <p.ClasseInterna>aqui.</p>"])
def test_html_residual_no_site(listas, texto):
    assert any("ClasseInterna" in t for t in _trechos(verificar_html(texto, "site/x.html", listas)))


def test_html_atributo_sem_valor_comum_passa(listas):
    assert verificar_html('<p hidden data-md-x="a">ok <input type="checkbox" checked></p>', "site/x.html", listas) == []


# 2. Modo estrito reutilizável


def test_listas_completas_estrito(tmp_path):
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    assert listas_completas(raiz, fonte, estrito=True).bloqueio
    with pytest.raises(vazamento.ModoCompletoIncompleto):
        listas_completas(raiz, None, estrito=True)
    privado = raiz / "sincronizacao" / "privado"
    for arquivo in (privado / "exclusoes.json", privado / "bloqueio.json",
                    fonte / "Database" / "docs" / "_manutencao" / "excecoes.json"):
        conteudo = arquivo.read_text(encoding="utf-8")
        arquivo.unlink()
        with pytest.raises(vazamento.ModoCompletoIncompleto) as erro:
            listas_completas(raiz, fonte, estrito=True)
        assert arquivo.name in str(erro.value)
        assert "servidor-ficticio" not in str(erro.value)
        arquivo.write_text(conteudo, encoding="utf-8")


def test_fonte_padrao_por_ambiente_e_por_arquivo(tmp_path, monkeypatch, capsys):
    monkeypatch.delenv("BDESK_FONTE", raising=False)
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    monkeypatch.setattr(vazamento, "RAIZ", raiz)
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "x.md").write_text("Pedido do ClienteFicticio.", encoding="utf-8")
    assert main(["--completo", str(docs)]) == 2
    monkeypatch.setenv("BDESK_FONTE", str(fonte))
    assert main(["--completo", str(docs)]) == 1
    monkeypatch.delenv("BDESK_FONTE")
    (raiz / "sincronizacao" / "privado" / "fonte.txt").write_text(f"{fonte}\nignorada\n", encoding="utf-8")
    assert main(["--completo", str(docs)]) == 1
    assert "bloqueio-privado" in capsys.readouterr().out


# 3. Profundidade e segmentos de links relativos


@pytest.mark.parametrize("profundidade", [0, 1])
def test_link_sobe_alem_da_raiz(listas, profundidade):
    achados = verificar_markdown("Veja a [pasta](../../Database/Procedures/).", "x.md", listas, profundidade=profundidade)
    assert "arquivo-de-codigo" in {x.categoria for x in achados}


def test_link_dentro_da_profundidade_passa(listas):
    assert verificar_markdown("[a](../../index.md) e [b](../fatos/)", "x.md", listas, profundidade=2) == []


def test_segmento_de_link_com_cara_de_identificador(listas):
    achados = verificar_markdown("Veja [isto](../Src_Modulo/).", "x.md", listas, profundidade=1)
    assert "Src_Modulo" in _trechos(achados)


def test_arvore_usa_profundidade(tmp_path, listas):
    docs = tmp_path / "docs"
    (docs / "fatos").mkdir(parents=True)
    (docs / "fatos" / "x.md").write_text("[a](../index.md)\n[b](../../fora/)\n", encoding="utf-8")
    achados = verificar_arvore(docs, listas)
    assert [(x.linha, x.categoria) for x in achados] == [(2, "arquivo-de-codigo")]


# 4. Título de link e attr_list


def test_titulo_de_link(listas):
    achados = verificar_markdown('Veja [x](a.md "ClasseInterna.Processar").', "x.md", listas)
    assert "ClasseInterna.Processar" in _trechos(achados)


@pytest.mark.parametrize("texto", ["## Título {#ClasseInterna}", "Texto {.ClasseInterna}", 'Botão {: title="Classe.Metodo" }'])
def test_attr_list_e_verificado(listas, texto):
    assert "fora-da-lista" in _categorias(texto, listas)


def test_ancora_curta_legitima_passa(listas):
    assert verificar_markdown("## Regra A-01 {#r-fato-a-01}\n\n[Voltar](index.md){ .md-button }", "x.md", listas) == []


# 5. Atributos de SVG


@pytest.mark.parametrize("atributo", ['id="ClasseInterna"', 'sodipodi:docname="Fila.cls"'])
def test_atributo_de_svg(tmp_path, listas, atributo):
    site = tmp_path / "site"
    site.mkdir()
    (site / "a.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg"><g {atributo}></g></svg>', encoding="utf-8")
    assert verificar_arvore(site, listas)


def test_svg_geometria_passa(tmp_path, listas):
    site = tmp_path / "site"
    site.mkdir()
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" width="10" height="10" version="1.1">'
        '<path d="M0 0L10 10Z" fill="#fff" stroke-width="2" transform="rotate(45)" class="aB_c"/>'
        '<text x="1" y="2" font-family="Roboto, sans-serif" style="a:b">TabelaA</text></svg>'
    )
    (site / "a.svg").write_text(svg, encoding="utf-8")
    assert verificar_arvore(site, listas) == []


# 6. Exclusão de coluna


def test_exclusao_de_coluna_nao_bloqueia_palavra_comum(tmp_path):
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={"colunas": ["dbo.ParametroX.Valor"]})
    listas = listas_completas(raiz, fonte)
    assert verificar_markdown("O valor é somado.", "x.md", listas) == []
    achados = verificar_markdown("Ver ParametroX.Valor.", "x.md", listas)
    assert "bloqueio-privado" in {x.categoria for x in achados}


# 7. Falsos positivos


def test_mascaras_de_data_passam(listas):
    texto = "```sql\nSELECT FORMAT(colData, 'yyyy-MM'), FORMAT(colData, 'yyyyMMdd') FROM TabelaA\n```\nUse `'yyyyMMdd'`."
    assert verificar_markdown(texto, "x.md", listas) == []


@pytest.mark.parametrize("apelido", ["[Total de abertas]", '"Total"', "Total"])
def test_apelidos_legitimos(listas, apelido):
    texto = f"```sql\nSELECT COUNT(*) AS {apelido} FROM TabelaA ORDER BY {apelido}\n```"
    assert verificar_markdown(texto, "x.md", listas) == []


@pytest.mark.parametrize("apelido", ["[ClasseInterna]", "uspFila"])
def test_apelidos_ilegitimos(listas, apelido):
    assert verificar_markdown(f"```sql\nSELECT COUNT(*) AS {apelido} FROM TabelaA\n```", "x.md", listas)


def test_listas_genericas_com_esquema_e_dominios_alternativos(tmp_path):
    esquema = tmp_path / "novo-esquema.json"
    esquema.write_text(json.dumps({"tabelas": {"dbo.TabelaNova": ["colNova"]}, "views": {}}), encoding="utf-8")
    dominios = tmp_path / "novos-dominios.json"
    dominios.write_text(json.dumps(["ChaveNova"]), encoding="utf-8")
    listas = listas_genericas(tmp_path, esquema, dominios)
    assert "colnova" in listas.permitidos and "chavenova" in listas.permitidos
    assert "tabelanova" in listas.esquema


# ---------------------------------------------------------------------------
# Calibração com a saída real (padrões reproduzidos com nomes sintéticos)
# ---------------------------------------------------------------------------

# 1. Apelido usado antes da definição


@pytest.mark.parametrize("apelido", ["s", "d", "m", "dd", "b"])
def test_apelido_usado_antes_da_definicao(listas, apelido):
    texto = (
        "```sql\n"
        f"SELECT a.colData, {apelido}.colNome\n"
        "FROM TabelaA a\n"
        f"LEFT JOIN TabelaB {apelido} ON {apelido}.colId = a.colStatus\n"
        "```"
    )
    assert verificar_markdown(texto, "x.md", listas) == []


def test_apelido_nao_definido_continua_barrado(listas):
    texto = "```sql\nSELECT a.colData, s.colNome\nFROM TabelaA a\n```"
    assert _trechos(verificar_markdown(texto, "x.md", listas)) == {"s.colNome"}


# 2. Apelidos de resultado na prosa da mesma página


def test_apelidos_de_resultado_na_prosa_da_pagina(listas):
    texto = (
        "| Coluna | Significado |\n"
        "|---|---|\n"
        "| `qtd_encerradas` | Total de encerradas. |\n"
        "| n_ctx_campo1 | Primeiro campo. |\n"
        "\n"
        "Use `t.taxa_resposta` e `flg_aberta`.\n"
        "\n"
        "```sql\n"
        "SELECT t.qtd_encerradas, t.taxa_resposta, t.flg_aberta, t.n_ctx_campo1\n"
        "FROM (\n"
        "    SELECT COUNT(*) AS qtd_encerradas, AVG(colValor) AS taxa_resposta,\n"
        "           MAX(colStatus) AS flg_aberta, MIN(colData) AS n_ctx_campo1\n"
        "    FROM TabelaA\n"
        ") t\n"
        "```\n"
    )
    assert verificar_markdown(texto, "x.md", listas) == []


def test_apelido_de_resultado_vale_so_na_mesma_pagina(listas):
    assert _trechos(verificar_markdown("Use `qtd_encerradas`.", "y.md", listas)) == {"qtd_encerradas"}


def test_apelido_de_resultado_com_rotina_continua_barrado(listas):
    texto = "Veja usp_total_fila.\n\n```sql\nSELECT COUNT(*) AS usp_total_fila FROM TabelaA\n```\n"
    assert "rotina" in {x.categoria for x in verificar_markdown(texto, "x.md", listas)}


def test_apelido_de_resultado_bloqueado_continua_barrado(tmp_path):
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    texto = "Veja total_ClienteFicticio.\n\n```sql\nSELECT COUNT(*) AS total_ClienteFicticio FROM TabelaA\n```\n"
    achados = verificar_markdown(texto, "x.md", listas_completas(raiz, fonte))
    assert (1, "bloqueio-privado") in {(x.linha, x.categoria) for x in achados}
    assert "total_ClienteFicticio" in _trechos(achados)


def test_apelidos_de_resultado_no_site(listas):
    html = (
        "<p>A coluna qtd_encerradas soma.</p>\n"
        '<div class="language-sql highlight"><pre><code>SELECT COUNT(*) AS qtd_encerradas FROM TabelaA\n'
        "</code></pre></div>"
    )
    assert verificar_html(html, "site/x.html", listas) == []


# 3. Comentários SQL


def test_placeholder_em_comentario_sql(listas):
    texto = (
        "```sql\n"
        "SELECT MAX(CASE WHEN c.colId = /* @idFicticio1 */ 0 THEN v.colNome END) AS valor\n"
        "FROM TabelaB c JOIN TabelaB v ON v.colId = c.colId\n"
        "```"
    )
    assert verificar_markdown(texto, "x.md", listas) == []


def test_comentario_sql_usa_prosa(listas):
    texto = "```sql\n-- Some as abertas por mês; ver ClasseInterna\nSELECT colData FROM TabelaA /* @a */\n```"
    assert _trechos(verificar_markdown(texto, "x.md", listas)) == {"ClasseInterna"}


# 4. COLLATE


@pytest.mark.parametrize("collation", ["Latin1_General_BIN2", "Latin1_General_CI_AI", "SQL_Latin1_General_CP1_CI_AS"])
def test_collate(listas, collation):
    texto = f"```sql\nSELECT colNome COLLATE {collation} AS nome FROM TabelaB WHERE colNome COLLATE {collation} = 'a'\n```"
    assert verificar_markdown(texto, "x.md", listas) == []


# 5. Mermaid


def test_mermaid_br_em_rotulo(listas):
    texto = "```mermaid\nflowchart LR\n  A[Abertura<br/>da requisição] --> B[Encerramento<br>final]\n```"
    assert verificar_markdown(texto, "x.md", listas) == []


def test_mermaid_rotulo_continua_verificado(listas):
    texto = "```mermaid\nflowchart LR\n  A[Grava<br/>ClasseInterna] --> B\n```"
    assert _trechos(verificar_markdown(texto, "x.md", listas)) == {"ClasseInterna"}


# 6. Permitidos públicos


def test_placeholder_e_produto_de_terceiros(listas):
    assert verificar_markdown("Escreva `tabela.coluna` ou tabela.coluna; a ação OfficeTrack.", "x.md", listas) == []


# ---------------------------------------------------------------------------
# Modo repositório (README.md, CLAUDE.md: não vão para o site)
# ---------------------------------------------------------------------------

_README_SINTETICO = (
    "# Repositório do site\n"
    "\n"
    "Ative o hook com `git config core.hooksPath .githooks` e rode `.venv\Scripts\pytest -q`.\n"
    "Instale `requirements-dev.txt`; o site é configurado em `mkdocs.yml`.\n"
    "A verificação é `python -m sincronizacao.vazamento --repositorio README.md`.\n"
    "Defina `BDESK_FONTE` ou crie `sincronizacao/privado/exclusoes.json`.\n"
    "A fonte fica em `<repo bdesk>/Database/docs`, lida por sincronizacao/fonte.py e config.json.\n"
    "Veja [o modelo](sincronizacao/mkdocs.modelo.yml), [o hook](.githooks/pre-commit) e a página index.html.\n"
    "Sirva com `mkdocs serve` em `http://127.0.0.1:8000`.\n"
    "\n"
    "```powershell\n"
    ".venv\Scripts\python -m pip install -r requirements-dev.txt\n"
    "```\n"
    "\n"
    "```bash\n"
    "git config core.hooksPath .githooks\n"
    "```\n"
    "\n"
    "```sh\n"
    "python -m sincronizacao.vazamento docs\n"
    "```\n"
)


def test_repositorio_readme_com_comandos_passa(listas):
    assert verificar_markdown(_README_SINTETICO, "README.md", listas, modo_repositorio=True) == []
    assert verificar_markdown(_README_SINTETICO, "README.md", listas)  # no modo do site, barra


@pytest.mark.parametrize(
    "texto, categoria",
    [
        ("Veja Pasta/ClasseFicticia.cls:12.", "arquivo-de-codigo"),
        ("Veja Pasta/ClasseFicticia.cls:12.", "numero-de-linha"),
        ("Veja `Arq.py:12`.", "numero-de-linha"),
        ("Veja as linhas 10-20.", "numero-de-linha"),
        ("Chamado por uspFicticia.", "rotina"),
        ("Texto <!-- prova -->x<!-- /prova -->.", "marcador"),
        ("```sql\nCREATE VIEW dbo.vwExemplo AS SELECT 1\n```", "definicao-de-view"),
    ],
)
def test_repositorio_barra_o_que_e_codigo(listas, texto, categoria):
    assert categoria in {x.categoria for x in verificar_markdown(texto, "README.md", listas, modo_repositorio=True)}


@pytest.mark.parametrize("ext", ["cls", "bas", "frm", "ctl", "asp", "aspx", "vb", "cs", "PRC", "viw", "TRG", "UDF", "vbp", "DLL"])
def test_repositorio_extensoes_de_origem(listas, ext):
    achados = verificar_markdown(f"Veja ArquivoX.{ext} aqui.", "README.md", listas, modo_repositorio=True)
    assert {x.categoria for x in achados} == {"arquivo-de-codigo"}


def test_repositorio_nao_gera_fora_da_lista_nem_trecho(listas):
    texto = "ClasseQualquer e x_y.\n\n```python\nimport os\n```\n"
    assert verificar_markdown(texto, "README.md", listas, modo_repositorio=True) == []


def test_repositorio_completo_barra_bloqueio_e_jargao(tmp_path):
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    listas = listas_completas(raiz, fonte)
    achados = verificar_markdown("Pedido do ClienteFicticio.\nFeito em TecFicticia.\n", "README.md", listas, modo_repositorio=True)
    assert {(x.linha, x.categoria) for x in achados} == {(1, "bloqueio-privado"), (2, "jargao")}


def test_repositorio_na_cli(tmp_path, capsys, monkeypatch):
    raiz, fonte = _montar_privado_e_fonte(tmp_path, exclusoes={})
    monkeypatch.setattr(vazamento, "RAIZ", raiz)
    monkeypatch.delenv("BDESK_FONTE", raising=False)
    pasta = tmp_path / "raiz"
    pasta.mkdir()
    (pasta / "README.md").write_text(_README_SINTETICO, encoding="utf-8")
    assert main(["--repositorio", str(pasta)]) == 0
    assert main(["--repositorio", "--completo", "--fonte", str(fonte), str(pasta)]) == 0
    (pasta / "CLAUDE.md").write_text("Veja `Ficticia.cls:3`.\n", encoding="utf-8")
    assert main(["--repositorio", str(pasta)]) == 1
    saida = capsys.readouterr().out
    assert "raiz/CLAUDE.md:1 arquivo-de-codigo" in saida and "Ficticia" not in saida
    assert main([str(pasta)]) == 1  # sem --repositorio, o README é barrado


# ---------------------------------------------------------------------------
# Site gerado: blocos do Pygments, mermaid e índice de busca (fixtures sintéticas)
# ---------------------------------------------------------------------------


def _linha_pygments(n, spans):
    ancora = f'<a id="__codelineno-0-{n}" name="__codelineno-0-{n}" href="#__codelineno-0-{n}"></a>'
    return ancora + "".join(f'<span class="{c}">{t}</span>' for c, t in spans)


_W = ("w", " ")

_HTML_PYGMENTS = (
    "<h2>Resultado</h2>\n"
    "<p>A coluna qtd_ficticia soma; a taxa_ficticia divide.</p>\n"
    "<table><tr><th>qtd_ficticia</th><th>taxa_ficticia</th></tr></table>\n"
    '<div class="highlight"><pre><span></span><code>'
    + _linha_pygments(1, [("k", "SELECT"), _W, ("n", "a"), ("p", "."), ("n", "colData"), ("p", ","), _W,
                          ("k", "COUNT"), ("p", "("), ("o", "*"), ("p", ")"), _W, ("k", "AS"), _W, ("n", "qtd_ficticia")])
    + "\n"
    + _linha_pygments(2, [("p", ","), _W, ("mi", "1"), _W, ("k", "AS"), _W, ("n", "taxa_ficticia")])
    + "\n"
    + _linha_pygments(3, [("k", "FROM"), _W, ("n", "TabelaA"), _W, ("n", "a")])
    + "\n</code></pre></div>\n"
)


def test_site_bloco_pygments_sem_classe_de_linguagem_coleta_apelidos(listas):
    assert verificar_html(_HTML_PYGMENTS, "site/x/index.html", listas) == []


def test_site_bloco_pygments_aplica_regras_de_sql(listas):
    html = (
        '<div class="highlight"><pre><span></span><code>'
        + _linha_pygments(1, [("k", "SELECT"), _W, ("n", "colSecreta"), _W, ("k", "FROM"), _W, ("n", "TabelaA")])
        + "\n</code></pre></div>"
    )
    assert _trechos(verificar_html(html, "site/x.html", listas)) == {"colSecreta"}


def test_site_bloco_pygments_que_nao_e_sql_continua_verificado(listas):
    html = '<div class="highlight"><pre><span></span><code>chamar ClasseInterna agora\n</code></pre></div>'
    assert _trechos(verificar_html(html, "site/x.html", listas)) == {"ClasseInterna"}


def test_site_apelido_vale_so_na_mesma_pagina_html(listas):
    assert _trechos(verificar_html("<p>A qtd_ficticia soma.</p>", "site/y.html", listas)) == {"qtd_ficticia"}


_HTML_MERMAID = (
    '<pre class="mermaid"><code>flowchart LR\n'
    '  A["Abertura&lt;br/&gt;TabelaA"] --&gt; B["Fim&lt;br&gt;da requisição"]\n'
    "</code></pre>"
)


def test_site_mermaid_br_em_rotulo(listas):
    assert verificar_html(_HTML_MERMAID, "site/mapa/index.html", listas) == []


def test_site_mermaid_rotulo_continua_verificado(listas):
    html = '<pre class="mermaid"><code>flowchart LR\n  A["Grava&lt;br/&gt;ClasseInterna"]\n</code></pre>'
    assert _trechos(verificar_html(html, "site/mapa/index.html", listas)) == {"ClasseInterna"}


def _indice(tmp_path, docs):
    site = tmp_path / "site"
    (site / "search").mkdir(parents=True)
    (site / "search" / "search_index.json").write_text(json.dumps({"config": {}, "docs": docs}), encoding="utf-8")
    return site


def test_indice_de_busca_agrupa_secoes_por_pagina(tmp_path, listas):
    site = _indice(
        tmp_path,
        [
            {"location": "receitas/x/", "title": "X", "text": ""},
            {"location": "receitas/x/#sql", "title": "SQL",
             "text": "<p>Consulta</p> <pre><code>SELECT COUNT(*) AS qtd_ficticia, 1 AS taxa_ficticia FROM TabelaA\n</code></pre>"},
            {"location": "receitas/x/#resultado", "title": "Resultado",
             "text": "<p>Exemplo</p> colData qtd_ficticia taxa_ficticia 9001 200 0.2"},
            {"location": "outra/#secao", "title": "Outra", "text": "<p>A qtd_ficticia não vale aqui.</p>"},
        ],
    )
    achados = verificar_arvore(site, listas)
    assert [(x.linha, x.trecho) for x in achados] == [(4, "qtd_ficticia")]


def test_indice_de_busca_mermaid_com_br(tmp_path, listas):
    site = _indice(
        tmp_path,
        [{"location": "mapa/#modelo", "title": "Modelo",
          "text": '<pre><code>flowchart LR\n  A["Abertura&lt;br/&gt;TabelaA"] --- B["Fim&lt;br/&gt;final"]\n</code></pre>'}],
    )
    assert verificar_arvore(site, listas) == []


def test_indice_de_busca_sql_continua_verificado(tmp_path, listas):
    site = _indice(
        tmp_path,
        [{"location": "x/#sql", "title": "SQL", "text": "<pre><code>SELECT colSecreta FROM TabelaA\n</code></pre>"}],
    )
    assert _trechos(verificar_arvore(site, listas)) == {"colSecreta"}


@pytest.mark.parametrize("arquivo", ["mkdocs.yml", "sincronizacao/mkdocs.modelo.yml"])
def test_highlight_emite_classe_de_linguagem(arquivo):
    from pathlib import Path

    texto = (Path(__file__).resolve().parent.parent / arquivo).read_text(encoding="utf-8")
    bloco = texto.split("pymdownx.highlight:", 1)[1].split("\n  - ", 1)[0]
    assert re.search(r"^\s+pygments_lang_class:\s*true\s*$", bloco, re.MULTILINE)
