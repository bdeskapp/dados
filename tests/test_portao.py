import pytest

from sincronizacao.config import CAMINHO_RELATORIO
from sincronizacao.portao import (
    PortaoRecusado, avaliar_relatorio, validar_frescor_relatorio, validar_git,
)
from tests.apoio_git import commitar_e_enviar, commit_local_nao_enviado, repo_git_sintetico  # noqa: F401


def test_arvore_suja_recusa(repo_git_sintetico):
    (repo_git_sintetico / "Database/docs/fatos/fato-a.md").write_text("x", encoding="utf-8")
    with pytest.raises(PortaoRecusado, match="alterações locais"):
        validar_git(repo_git_sintetico)


def test_commit_fora_do_ramo_integrado_recusa(repo_git_sintetico):
    commit_local_nao_enviado(repo_git_sintetico)
    with pytest.raises(PortaoRecusado, match="origin/development"):
        validar_git(repo_git_sintetico)


def test_docs_alterado_depois_do_relatorio_recusa(repo_git_sintetico):
    commitar_e_enviar(repo_git_sintetico, "Database/docs/fatos/fato-a.md", "mudou")
    with pytest.raises(PortaoRecusado, match="régua"):
        validar_frescor_relatorio(repo_git_sintetico)


def test_relatorio_no_mesmo_commit_das_docs_passa(repo_git_sintetico):
    commitar_e_enviar(repo_git_sintetico, ["Database/docs/fatos/fato-a.md", CAMINHO_RELATORIO], "junto")
    validar_frescor_relatorio(repo_git_sintetico)


def test_politica_por_estado():
    p = avaliar_relatorio({"veredito": "APROVADA",
        "receitas": [{"id": "a", "estado": "aprovada"}, {"id": "b", "estado": "em-disputa"}, {"id": "c", "estado": "nao-medida"}],
        "itens": [{"id": "R-x-01", "estado": "vigente"}, {"id": "R-x-02", "estado": "em-disputa"}]})
    assert p.receitas_publicadas == {"a"} and p.receitas_barradas == {"b"} and p.receitas_em_revisao == {"c"}
    assert p.regras_em_revisao == {"R-x-02"}


def test_veredito_inconclusivo_recusa():
    with pytest.raises(PortaoRecusado):
        avaliar_relatorio({"veredito": "INCONCLUSIVA", "receitas": [], "itens": []})
