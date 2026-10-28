import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from sincronizacao.__main__ import FalhaVazamento, main, sincronizar
from sincronizacao.portao import PortaoRecusado
from sincronizacao.vazamento import ModoCompletoIncompleto
from tests.apoio_git import _git, repo_git_sintetico  # noqa: F401

RAIZ = Path(__file__).resolve().parent.parent


def _montar_site(destino: Path, com_privado: bool = True) -> Path:
    (destino / "sincronizacao").mkdir(parents=True)
    shutil.copy(RAIZ / "sincronizacao" / "mkdocs.modelo.yml", destino / "sincronizacao" / "mkdocs.modelo.yml")
    shutil.copytree(RAIZ / "overrides", destino / "overrides")
    (destino / "docs").mkdir()
    (destino / "docs" / "index.md").write_text("PRÓPRIA\n", encoding="utf-8")
    if com_privado:
        privado = destino / "sincronizacao" / "privado"
        privado.mkdir()
        (privado / "exclusoes.json").write_text(
            json.dumps({"tabelas": ["dbo.SenhaFicticia", "dbo.TabelaTemp"], "views": [], "colunas": []}),
            encoding="utf-8",
        )
        (privado / "bloqueio.json").write_text(json.dumps({"padroes": []}), encoding="utf-8")
    return destino


@pytest.fixture
def site_vazio(tmp_path) -> Path:
    return _montar_site(tmp_path / "site")


@pytest.fixture
def site_com_docs_antigo(site_vazio) -> Path:
    docs = site_vazio / "docs"
    (docs / "fatos").mkdir()
    (docs / "fatos" / "antigo.md").write_text("# Antigo\n", encoding="utf-8")
    (docs / "dicionario").mkdir()
    (docs / "dicionario" / "x.md").write_text("# X\n", encoding="utf-8")
    (docs / "consumo").mkdir()
    (docs / "consumo" / "c.md").write_text("# Consumo próprio\n", encoding="utf-8")
    return site_vazio


def snapshot(pasta: Path) -> dict:
    return {p.relative_to(pasta).as_posix(): p.read_bytes() for p in sorted(pasta.rglob("*")) if p.is_file()}


def _commitar_pagina_e_relatorio(repo: Path, caminho: str, texto_extra: str, troca: tuple | None = None) -> None:
    pagina = repo / "Database" / "docs" / caminho
    texto = pagina.read_text(encoding="utf-8")
    if troca:
        texto = texto.replace(*troca)
    pagina.write_text(texto + texto_extra, encoding="utf-8")
    relatorio = repo / "docs/plans/database-docs/regua/relatorio.json"
    relatorio.write_text(relatorio.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-m", "muda")
    _git(repo, "push", "origin", "development")


@pytest.fixture
def repo_valido(repo_git_sintetico) -> Path:
    """Corrige o que a fixture compartilhada tem de inválido de propósito (usado por outros testes)."""
    base = repo_git_sintetico / "Database" / "docs"
    trocas = [
        ("dimensoes/dim-b.md", "TabelaB", "TabelaAConcluida"),
        ("fora-de-escopo/modulo-x.md", "TabelaTemp", "TabelaA"),
        ("_gerado/dominios-do-produto.md", "## DominioStatus", "## Status do item"),
    ]
    for caminho, de, para in trocas:
        arq = base / caminho
        arq.write_text(arq.read_text(encoding="utf-8").replace(de, para), encoding="utf-8")
    relatorio = repo_git_sintetico / "docs/plans/database-docs/regua/relatorio.json"
    relatorio.write_text(relatorio.read_text(encoding="utf-8") + " ", encoding="utf-8")
    _git(repo_git_sintetico, "add", "-A")
    _git(repo_git_sintetico, "commit", "-m", "corrige")
    _git(repo_git_sintetico, "push", "origin", "development")
    return repo_git_sintetico


@pytest.fixture
def repo_git_sintetico_com_vazamento(repo_valido) -> Path:
    _commitar_pagina_e_relatorio(repo_valido, "fatos/fato-a.md", "\nPedido do ClienteFicticio.\n")
    return repo_valido


@pytest.fixture
def repo_git_sujo(repo_valido) -> Path:
    pagina = repo_valido / "Database/docs/fatos/fato-a.md"
    pagina.write_text(pagina.read_text(encoding="utf-8") + "\nAlteração local.\n", encoding="utf-8")
    return repo_valido


def explode(*a, **k):
    raise RuntimeError("falha simulada")


def test_sincronizacao_completa_gera_e_troca(repo_valido, site_vazio):
    r = sincronizar(repo_valido, site_vazio, "9.9.9", hoje="2030-01-01")
    docs = site_vazio / "docs"
    assert r["achados"] == 0
    assert (docs / "fatos/fato-a.md").exists()
    assert not (docs / "receitas/receita-disputa.md").exists()
    texto = (docs / "fatos/fato-a.md").read_text(encoding="utf-8")
    assert "{#r-fato-a-01}" in texto
    assert texto.startswith("---\ngerado: sincronizacao\n---\n")
    assert (docs / "index.md").read_text(encoding="utf-8") == "PRÓPRIA\n"
    assert (docs / "busca.md").exists()
    assert "9.9.9" in (docs / "sobre/versao.md").read_text(encoding="utf-8")
    assert (docs / "dicionario/dbo-tabelaa.md").exists()
    assert not (docs / "dicionario/dbo-senhaficticia.md").exists()
    assert (site_vazio / "mkdocs.yml").exists()
    esquema = json.loads((site_vazio / "sincronizacao/esquema-publicado.json").read_text(encoding="utf-8"))
    assert "dbo.TabelaA" in esquema["tabelas"]
    assert (site_vazio / "sincronizacao/dominios-publicados.json").exists()
    assert not (site_vazio / ".sync-tmp").exists()


def test_troca_preserva_proprias_e_apaga_geradas_antigas(repo_valido, site_com_docs_antigo):
    sincronizar(repo_valido, site_com_docs_antigo, "9.9.9")
    docs = site_com_docs_antigo / "docs"
    assert not (docs / "fatos/antigo.md").exists()
    assert not (docs / "dicionario/x.md").exists()
    assert (docs / "consumo/c.md").read_text(encoding="utf-8") == "# Consumo próprio\n"
    assert (docs / "index.md").read_text(encoding="utf-8") == "PRÓPRIA\n"


def test_falha_no_meio_preserva_docs(repo_valido, site_com_docs_antigo, monkeypatch):
    antes = snapshot(site_com_docs_antigo / "docs")
    monkeypatch.setattr("sincronizacao.__main__.gerar_dicionario", explode)
    with pytest.raises(RuntimeError):
        sincronizar(repo_valido, site_com_docs_antigo, "9.9.9")
    assert snapshot(site_com_docs_antigo / "docs") == antes
    assert not (site_com_docs_antigo / ".sync-tmp").exists()


def test_vazamento_impede_troca(repo_git_sintetico_com_vazamento, site_com_docs_antigo, capsys):
    antes = snapshot(site_com_docs_antigo)
    with pytest.raises(FalhaVazamento) as erro:
        sincronizar(repo_git_sintetico_com_vazamento, site_com_docs_antigo, "9.9.9")
    assert snapshot(site_com_docs_antigo) == antes  # docs/, mkdocs.yml e JSON de sincronizacao/ intactos
    assert not (site_com_docs_antigo / ".sync-tmp").exists()
    assert not (site_com_docs_antigo / "mkdocs.yml").exists()
    assert not (site_com_docs_antigo / "sincronizacao/esquema-publicado.json").exists()
    assert not (site_com_docs_antigo / "sincronizacao/dominios-publicados.json").exists()
    saida = capsys.readouterr()
    assert "ClienteFicticio" not in saida.out + saida.err + str(erro.value)


def test_sem_exclusoes_levanta_e_preserva_docs(repo_valido, tmp_path):
    site = _montar_site(tmp_path / "outro", com_privado=False)
    antes = snapshot(site / "docs")
    with pytest.raises(ModoCompletoIncompleto):
        sincronizar(repo_valido, site, "9.9.9")
    assert snapshot(site / "docs") == antes


def test_saida_dev_nao_toca_docs(repo_git_sujo, site_com_docs_antigo, tmp_path):
    antes = snapshot(site_com_docs_antigo / "docs")
    sincronizar(repo_git_sujo, site_com_docs_antigo, "9.9.9", saida_dev=tmp_path / "dev")
    assert snapshot(site_com_docs_antigo / "docs") == antes
    assert (tmp_path / "dev/fatos/fato-a.md").exists()
    assert not (site_com_docs_antigo / ".sync-tmp").exists()


def test_saida_dev_nao_exige_privado_e_nao_levanta_por_achados(repo_git_sintetico_com_vazamento, tmp_path, capsys):
    site = _montar_site(tmp_path / "dev-site", com_privado=False)
    r = sincronizar(repo_git_sintetico_com_vazamento, site, "9.9.9", saida_dev=tmp_path / "dev")
    assert r["achados"] > 0 and (tmp_path / "dev/fatos/fato-a.md").exists()
    saida = capsys.readouterr()
    assert "ClienteFicticio" not in saida.out + saida.err
    assert "fatos/fato-a.md" in saida.out


@pytest.mark.parametrize("relativo", ["docs", "docs/sub", ".sync-tmp/x"])
def test_saida_dev_dentro_de_docs_ou_tmp_e_rejeitada(repo_valido, site_vazio, relativo):
    antes = snapshot(site_vazio)
    with pytest.raises(ValueError):
        sincronizar(repo_valido, site_vazio, "9.9.9", saida_dev=site_vazio / relativo)
    assert snapshot(site_vazio) == antes


def test_yaml_invalido_cita_so_o_caminho(repo_valido, site_vazio):
    _commitar_pagina_e_relatorio(repo_valido, "fatos/fato-a.md", "", troca=("papel: fato", "papel: [fato"))
    with pytest.raises(ValueError) as erro:
        sincronizar(repo_valido, site_vazio, "9.9.9")
    assert "fatos/fato-a.md" in str(erro.value) and "papel" not in str(erro.value)


def _espiao_replace(monkeypatch, falhar_a_partir_de=None, so_uma=False):
    chamadas = []
    real = os.replace

    def fake(src, dst):
        chamadas.append((str(src), str(dst)))
        n = len(chamadas)
        if falhar_a_partir_de is not None and (n == falhar_a_partir_de or (not so_uma and n > falhar_a_partir_de)):
            raise OSError("falha simulada de os.replace")
        return real(src, dst)

    monkeypatch.setattr(os, "replace", fake)
    return chamadas


def test_rollback_quando_replace_falha_na_n_esima_chamada(repo_valido, site_com_docs_antigo, tmp_path, monkeypatch):
    # conta as chamadas de uma sincronização completa em outro site
    outro = tmp_path / "contagem"
    shutil.copytree(site_com_docs_antigo, outro)
    chamadas = _espiao_replace(monkeypatch)
    sincronizar(repo_valido, outro, "9.9.9")
    total = len(chamadas)
    assert total > 3
    antes = snapshot(site_com_docs_antigo)
    for n in (1, 3, total):
        _espiao_replace(monkeypatch, falhar_a_partir_de=n, so_uma=True)
        with pytest.raises(OSError):
            sincronizar(repo_valido, site_com_docs_antigo, "9.9.9")
        monkeypatch.undo()
        assert snapshot(site_com_docs_antigo) == antes, f"falha na chamada {n}"
        assert not (site_com_docs_antigo / ".sync-tmp").exists()


def test_backup_pendente_nao_e_apagado(repo_valido, site_vazio):
    pendente = site_vazio / ".sync-tmp" / "antigo"
    pendente.mkdir(parents=True)
    (pendente / "x.md").write_text("# X", encoding="utf-8")
    with pytest.raises(RuntimeError, match="backup pendente"):
        sincronizar(repo_valido, site_vazio, "9.9.9")
    assert (pendente / "x.md").exists()


def test_cli_sai_com_1_por_backup_pendente(repo_valido, site_vazio, capsys):
    (site_vazio / ".sync-tmp" / "antigo").mkdir(parents=True)
    rc = main(["--fonte", str(repo_valido), "--versao-produto", "9.9.9", "--raiz-site", str(site_vazio)])
    assert rc == 1 and "backup pendente" in capsys.readouterr().err


def test_restauracao_que_falha_preserva_backup(repo_valido, site_com_docs_antigo, monkeypatch, capsys):
    _espiao_replace(monkeypatch, falhar_a_partir_de=4)  # a troca e a restauração falham
    with pytest.raises(OSError):
        sincronizar(repo_valido, site_com_docs_antigo, "9.9.9")
    monkeypatch.undo()
    backups = list(site_com_docs_antigo.glob(".sync-backup-*"))
    assert len(backups) == 1
    assert (backups[0] / "docs/fatos/antigo.md").read_text(encoding="utf-8") == "# Antigo\n"
    assert str(backups[0]) in capsys.readouterr().err


def _carregar_yaml_permissivo(texto: str) -> dict:
    class Carregador(yaml.SafeLoader):
        pass

    Carregador.add_multi_constructor("tag:yaml.org,2002:python/name:", lambda l, s, n: s)
    return yaml.load(texto, Loader=Carregador)


def test_dominios_sem_marcadores_nem_prova(repo_valido, site_vazio):
    _commitar_pagina_e_relatorio(
        repo_valido,
        "_gerado/dominios-do-produto.md",
        "\nObservação <!-- prova -->(`ArquivoFicticio.cls:12`)<!-- /prova --> final.\n",
    )
    sincronizar(repo_valido, site_vazio, "9.9.9")
    texto = (site_vazio / "docs/dominios-do-produto.md").read_text(encoding="utf-8")
    assert "<!--" not in texto
    assert "ArquivoFicticio" not in texto


def test_mkdocs_yml_gerado_tem_nav(repo_valido, site_vazio):
    sincronizar(repo_valido, site_vazio, "9.9.9")
    cfg = _carregar_yaml_permissivo((site_vazio / "mkdocs.yml").read_text(encoding="utf-8"))
    nav = cfg["nav"]
    assert nav[0] == {"Início": "index.md"}
    secoes = {list(i)[0]: list(i.values())[0] for i in nav[1:]}
    assert {"Fato A": "fatos/fato-a.md"} in secoes["Fatos"]
    assert {"OK": "receitas/receita-ok.md"} in secoes["Receitas"] or any(
        "receita-ok.md" in str(i) for i in secoes["Receitas"]
    )
    assert {"Busca": "busca.md"} in secoes["Referência"]
    assert not any("receita-disputa" in str(i) for i in nav)
    assert "repo_url" not in cfg and "edit_uri" not in cfg


def test_site_sintetico_constroi_estrito(repo_valido, site_vazio):
    sincronizar(repo_valido, site_vazio, "9.9.9")
    r = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict"],
        cwd=site_vazio, capture_output=True, text=True,
    )
    if r.returncode != 0:
        pytest.fail(f"mkdocs build --strict falhou\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}")


def test_cli_sai_com_1_por_vazamento_sem_trecho(repo_git_sintetico_com_vazamento, site_vazio, capsys):
    rc = main(["--fonte", str(repo_git_sintetico_com_vazamento), "--versao-produto", "9.9.9",
               "--raiz-site", str(site_vazio)])
    saida = capsys.readouterr()
    assert rc == 1
    assert "FalhaVazamento" in saida.err and "ClienteFicticio" not in saida.out + saida.err


def test_cli_sai_com_1_por_modo_completo_incompleto(repo_valido, tmp_path, capsys):
    site = _montar_site(tmp_path / "sem-privado", com_privado=False)
    rc = main(["--fonte", str(repo_valido), "--versao-produto", "9.9.9", "--raiz-site", str(site)])
    saida = capsys.readouterr()
    assert rc == 1 and "ModoCompletoIncompleto" in saida.err


def test_cli_sai_com_0(repo_valido, site_vazio, capsys):
    rc = main(["--fonte", str(repo_valido), "--versao-produto", "9.9.9", "--raiz-site", str(site_vazio)])
    assert rc == 0 and (site_vazio / "docs/fatos/fato-a.md").exists()
