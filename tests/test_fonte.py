from sincronizacao.fonte import carregar_fonte, ler_pagina


def test_ler_pagina_separa_front_matter():
    p = ler_pagina("---\npapel: fato\ntabelas: [A, B]\n---\n# T\n", "fatos/x.md")
    assert p.meta == {"papel": "fato", "tabelas": ["A", "B"]}
    assert p.corpo == "# T\n"


def test_carregar_fonte_sintetica(fonte_sintetica):
    f = carregar_fonte(fonte_sintetica)
    assert "fatos/fato-a.md" in f.paginas
    assert "dbo.vwExemplo" in f.esquema.views
    assert f.relatorio["veredito"] == "APROVADA"
