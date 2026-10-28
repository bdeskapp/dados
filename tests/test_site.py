def test_build_estrito_passa_e_tem_noindex(site_construido):
    html = (site_construido / "index.html").read_text(encoding="utf-8")
    assert '<meta name="robots" content="noindex, nofollow">' in html


def test_sem_link_de_repositorio(site_construido):
    html = (site_construido / "index.html").read_text(encoding="utf-8")
    assert "github.com/bdeskapp" not in html
