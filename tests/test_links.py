import pytest

from sincronizacao.links import ContextoLinks, ancora_regra, injetar_ancoras, reescrever_links


def ctx(publicadas=None, barradas=None, abertas=None, decididas=None):
    return ContextoLinks(
        publicadas=publicadas if publicadas is not None else {"fatos/fato-a.md", "mapa/regras-essenciais.md"},
        barradas=barradas or set(),
        pendencias_abertas=abertas or set(),
        pendencias_decididas=decididas or set(),
    )


def test_ancora_regra():
    assert ancora_regra("R-fato-a-01") == "r-fato-a-01"


def test_injetar_ancora_com_acento_e_crase():
    assert injetar_ancoras("#### R-fato-a-01: Some `TabelaA` histórico.") == "#### R-fato-a-01: Some `TabelaA` histórico. {#r-fato-a-01}"


def test_injetar_ancora_idempotente():
    uma = injetar_ancoras("#### R-fato-a-01: Título")
    assert injetar_ancoras(uma) == uma
    assert uma.count("{#") == 1


def test_injetar_so_em_titulos_de_regra():
    t = "### R-fato-a-01: x\n#### Outro título\nR-fato-a-01: texto"
    assert injetar_ancoras(t) == t


def test_link_longo_vira_curto():
    t = "[R-fato-a-01](../fatos/fato-a.md#r-fato-a-01-some-tabelaa-e-histórico)"
    assert reescrever_links(t, "mapa/regras-essenciais.md", ctx()) == "[R-fato-a-01](../fatos/fato-a.md#r-fato-a-01)"


def test_ancora_curta_nao_muda():
    t = "[x](../fatos/fato-a.md#r-fato-a-01)"
    assert reescrever_links(t, "mapa/regras-essenciais.md", ctx()) == t


def test_link_para_receita_barrada_vira_texto():
    t = "Receita [disputa](../receitas/receita-disputa.md)."
    assert reescrever_links(t, "fatos/fato-a.md", ctx(barradas={"receitas/receita-disputa.md"})) == "Receita disputa (em revisão)."


def test_pendencia_aberta_vira_limitacao():
    assert reescrever_links("[PEND-07](../pendencias-abertas.md#pend-07)", "fatos/fato-a.md", ctx(abertas={"07"})) == "[L-07](../limitacoes-conhecidas.md#l-07)"


def test_pendencia_inexistente_falha():
    with pytest.raises(ValueError, match="PEND-99"):
        reescrever_links("[PEND-99](../pendencias-abertas.md#pend-99)", "fatos/fato-a.md", ctx())


def test_pendencia_inexistente_em_texto_falha():
    with pytest.raises(ValueError, match="PEND-99"):
        reescrever_links("Ver PEND-99.", "fatos/fato-a.md", ctx())


def test_index_vira_busca():
    assert reescrever_links("[índice](../INDEX.md)", "fatos/fato-a.md", ctx()) == "[índice](../busca.md)"


def test_gerado_json_vira_dicionario():
    for nome in ("colunas", "fks", "colunas-views"):
        assert reescrever_links(f"[c](../_gerado/{nome}.json)", "fatos/fato-a.md", ctx()) == "[c](../dicionario/index.md)"


def test_dominios():
    assert reescrever_links("[d](_gerado/dominios-do-produto.md)", "glossario.md", ctx()) == "[d](dominios-do-produto.md)"


def test_alvo_nao_publicado_vira_texto():
    assert reescrever_links("Veja [outro](../fatos/outro.md).", "fatos/fato-a.md", ctx()) == "Veja outro."


def test_item_vazio_removido():
    t = "- [](../fatos/outro.md)\n- [A](../fatos/fato-a.md)"
    assert reescrever_links(t, "mapa/x.md", ctx()) == "- [A](../fatos/fato-a.md)"


def test_separador_orfao_removido():
    t = "- [A](../fatos/fato-a.md) · [](../fatos/b.md)"
    assert reescrever_links(t, "mapa/x.md", ctx()) == "- [A](../fatos/fato-a.md)"


def test_pendencia_decidida_some_com_parenteses():
    assert reescrever_links("A regra vale (PEND-05).", "fatos/fato-a.md", ctx(decididas={"05"})) == "A regra vale."


def test_pendencia_decidida_link_some():
    t = "A regra vale ([PEND-05](../pendencias-abertas.md#pend-05))."
    assert reescrever_links(t, "fatos/fato-a.md", ctx(decididas={"05"})) == "A regra vale."


def test_pendencia_decidida_com_virgula():
    r = reescrever_links("Ver PEND-05, PEND-07.", "fatos/fato-a.md", ctx(decididas={"05"}, abertas={"07"}))
    assert r == "Ver L-07."


def test_mencao_aberta_em_texto():
    assert reescrever_links("Ver PEND-07.", "fatos/fato-a.md", ctx(abertas={"07"})) == "Ver L-07."
