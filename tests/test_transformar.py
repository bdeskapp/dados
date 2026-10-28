import pytest

from sincronizacao.fonte import Pagina
from sincronizacao.portao import Politica
from sincronizacao.transformar import (
    AjusteOrfao, aviso_receita_em_revisao, limpar_glossario, limpar_sql_receita,
    marcar_regras_em_revisao, reduzir_fora_de_escopo, remover_blocos_internos,
    remover_breadcrumb, remover_provas, trocar_decisoes, trocar_ficticios,
    transformar_pagina,
)


def politica(**kw):
    base = dict(commit="abc", receitas_publicadas=set(), receitas_em_revisao=set(),
                receitas_barradas=set(), regras_em_revisao=set())
    base.update(kw)
    return Politica(**base)


def test_remover_provas_inline_e_multilinha():
    assert remover_provas("Grava o tempo <!-- prova -->(`X.cls:1`)<!-- /prova -->.") == "Grava o tempo."
    assert remover_provas("A\n<!-- prova -->\nlinha\n<!-- /prova -->\nB") == "A\nB"


def test_remover_provas_colada_na_palavra():
    t = "A abertura<!-- prova --> (`x`)<!-- /prova --> escolhe o caminho<!-- prova -->(`y`)<!-- /prova -->, e segue."
    assert remover_provas(t) == "A abertura escolhe o caminho, e segue."


def test_marcador_de_prova_desbalanceado_falha():
    with pytest.raises(ValueError, match="prova"):
        remover_provas("<!-- prova --> sem fechamento")


def test_trocar_decisoes():
    assert trocar_decisoes("<!-- decisao -->Definição validada pelo usuário em 2030-01-01<!-- /decisao -->:") == "Decisão do produto:"
    assert trocar_decisoes("Veja a <!-- decisao -->x<!-- /decisao --> acima.") == "Veja a decisão do produto acima."
    assert trocar_decisoes("Fim. <!-- decisao -->x<!-- /decisao --> vale.") == "Fim. Decisão do produto vale."


def test_trocar_ficticios():
    t = "Antes\n\n<!-- ficticio -->\n**exemplo fictício**\nLinha 1\n\n```sql\nSELECT 1\n```\n<!-- /ficticio -->\nDepois\n"
    esperado = 'Antes\n\n!!! example "Exemplo fictício"\n    Linha 1\n\n    ```sql\n    SELECT 1\n    ```\nDepois\n'
    assert trocar_ficticios(t) == esperado


def test_remover_breadcrumb():
    assert remover_breadcrumb("# T\nVocê está em: A > B\nTexto\n") == "# T\nTexto\n"


def test_remover_blocos_internos():
    t = "A\n```json pares\n{\"a\": 1}\n```\nB\n```json\n{}\n```\n"
    assert remover_blocos_internos(t) == "A\nB\n```json\n{}\n```\n"


def test_limpar_sql_receita():
    t = "```sql\n-- receita: receita-a\n-- so-abertas\nSELECT 1\n```\n\n```sql\n-- receita: b\nSELECT 2 -- so-abertas\n```\n"
    assert limpar_sql_receita(t) == "```sql\nSELECT 1\n```\n\n```sql\nSELECT 2 -- so-abertas\n```\n"


def test_limpar_glossario_remove_coluna_e_caminho():
    t = "Caminho comum: algo.\n\n| termo | tabela.coluna | caminho tela→API/SP→coluna | página |\n|---|---|---|---|\n| T | `A.b` | x | [p](p.md) |\n"
    assert limpar_glossario(t) == "| termo | tabela.coluna | página |\n|---|---|---|\n| T | `A.b` | [p](p.md) |\n"


def test_reduzir_fora_de_escopo():
    t = "# T\n\n## Documentação existente\n\nx\n\n## Outra\n\ny\n"
    assert reduzir_fora_de_escopo(t) == "# T\n\n## Outra\n\ny\n"
    assert reduzir_fora_de_escopo("# T\n\n## Documentação existente\nx\n") == "# T\n\n"


def test_marcar_regras_em_revisao():
    t = "#### R-fato-a-01: Título\n\n#### R-fato-a-02: Outro\n"
    assert marcar_regras_em_revisao(t, {"R-fato-a-02"}) == (
        '#### R-fato-a-01: Título\n\n#### R-fato-a-02: Outro <span class="em-revisao">em revisão</span>\n')


def test_aviso_receita_em_revisao():
    assert aviso_receita_em_revisao("# Receita\n\nTexto\n") == (
        '# Receita\n\n!!! warning "Em revisão"\n'
        "    A definição desta receita ainda não foi verificada por completo. Use-a com cautela e confira os resultados.\n"
        "\nTexto\n")


def test_transformar_aplica_ajuste_e_detecta_orfao():
    p = Pagina("receitas/receita-a.md", {}, "# Receita\n\nTexto<!-- prova -->(`X.cls:1`)<!-- /prova --> ficticio-x.\n\n"
               "#### R-receita-a-01: Regra\n\n```sql\n-- receita: receita-a\nSELECT 1\n```\n")
    pol = politica(receitas_em_revisao={"receita-a"}, regras_em_revisao={"R-receita-a-01"})
    saida = transformar_pagina(p, pol, {p.caminho: [{"de": "ficticio-x", "para": "exemplo"}]})
    assert "exemplo." in saida and "X.cls" not in saida and "-- receita" not in saida
    assert saida.index('!!! warning "Em revisão"') < saida.index("Texto")
    assert 'em-revisao">em revisão' in saida
    with pytest.raises(AjusteOrfao):
        transformar_pagina(p, pol, {p.caminho: [{"de": "trecho inexistente", "para": "x"}]})


def test_transformar_sem_aviso_quando_receita_nao_esta_em_revisao():
    p = Pagina("receitas/receita-a.md", {}, "# Receita\n\nTexto\n")
    assert "warning" not in transformar_pagina(p, politica(), {})
