"""O hook de pre-commit bloqueia referência a código no que está staged e deixa passar texto comum."""
import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent

pytestmark = pytest.mark.skipif(
    shutil.which("git") is None or shutil.which("sh") is None,
    reason="precisa de git e sh (no Windows, o do Git for Windows) no PATH",
)

LIMPO = "# Página\n\nTexto comum, sem nada de especial.\n"
VAZA = "# Página\n\nVeja `Ficticia.cls:3` para detalhes.\n"
GENERICO_ACEITA = "# Página\n\nO servidor-ficticio7 responde.\n"


def _git(repo, *args, env=None):
    return subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
        cwd=repo, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env,
    )


def _saida(r):
    return r.stdout + r.stderr


def _repo(tmp_path, texto=LIMPO, extras=None, stage=True):
    repo = tmp_path / "repo"
    repo.mkdir()
    shutil.copytree(
        RAIZ / "sincronizacao", repo / "sincronizacao",
        ignore=shutil.ignore_patterns("privado", "__pycache__"),
    )
    hooks = repo / ".githooks"
    hooks.mkdir()
    shutil.copy(RAIZ / ".githooks" / "pre-commit", hooks / "pre-commit")
    (repo / "docs").mkdir()
    (repo / "docs" / "x.md").write_text(texto, encoding="utf-8")
    for nome, conteudo in (extras or {}).items():
        (repo / nome).write_text(conteudo, encoding="utf-8")
    assert _git(repo, "init", "-q").returncode == 0
    _git(repo, "config", "core.hooksPath", ".githooks")
    _git(repo, "config", "core.autocrlf", "false")
    if stage:
        _git(repo, "add", "-A")
    return repo


def _privado(repo, tmp_path, com_fonte=True):
    """privado/ sintético, criado depois do git add (fica fora do index)."""
    privado = repo / "sincronizacao" / "privado"
    privado.mkdir()
    (privado / "bloqueio.json").write_text(json.dumps({"padroes": [r"servidor-ficticio\d+"]}), encoding="utf-8")
    (privado / "exclusoes.json").write_text("{}", encoding="utf-8")
    env = {k: v for k, v in os.environ.items() if k != "BDESK_FONTE"}
    if com_fonte:
        fonte = tmp_path / "fonte"
        (fonte / "Database" / "docs" / "_manutencao").mkdir(parents=True)
        (fonte / "Database" / "docs" / "_manutencao" / "excecoes.json").write_text("{}", encoding="utf-8")
        env["BDESK_FONTE"] = str(fonte)
    return env


def test_commit_com_codigo_e_bloqueado_sem_vazar_o_trecho(tmp_path):
    repo = _repo(tmp_path, VAZA)
    r = _git(repo, "commit", "-m", "x")
    saida = _saida(r)
    assert r.returncode != 0
    assert "Ficticia" not in saida
    assert "docs/x.md:3 " in saida  # prova que o verificador rodou
    assert "verificação completa indisponível" in saida


def test_commit_limpo_passa(tmp_path):
    repo = _repo(tmp_path)
    r = _git(repo, "commit", "-m", "x")
    assert r.returncode == 0, _saida(r)


def test_vazamento_so_na_arvore_nao_bloqueia(tmp_path):
    repo = _repo(tmp_path)
    (repo / "docs" / "x.md").write_text(VAZA, encoding="utf-8")  # não staged
    r = _git(repo, "commit", "-m", "x")
    assert r.returncode == 0, _saida(r)


def test_vazamento_staged_e_limpo_na_arvore_bloqueia(tmp_path):
    repo = _repo(tmp_path, VAZA)
    (repo / "docs" / "x.md").write_text(LIMPO, encoding="utf-8")  # árvore limpa, index não
    r = _git(repo, "commit", "-m", "x")
    assert r.returncode != 0
    assert "docs/x.md:3 " in _saida(r)


def test_docs_ausente_do_index_bloqueia(tmp_path):
    repo = _repo(tmp_path, stage=False)
    _git(repo, "add", "sincronizacao", ".githooks")
    r = _git(repo, "commit", "-m", "x")
    assert r.returncode != 0
    assert "incompleta ou pasta ausente" in _saida(r)


README_COM_COMANDOS = (
    "# Leia\n\nAtive com `git config core.hooksPath .githooks` e instale `requirements-dev.txt`.\n\n"
    "```bash\ngit config core.hooksPath .githooks\n```\n"
)


def test_readme_com_comandos_do_repositorio_passa(tmp_path):
    repo = _repo(tmp_path, extras={"README.md": README_COM_COMANDOS, "CLAUDE.md": README_COM_COMANDOS})
    r = _git(repo, "commit", "-m", "x")
    assert r.returncode == 0, _saida(r)


def test_readme_com_comandos_e_privado_passa(tmp_path):
    repo = _repo(tmp_path, extras={"README.md": README_COM_COMANDOS})
    env = _privado(repo, tmp_path)
    r = _git(repo, "commit", "-m", "x", env=env)
    assert r.returncode == 0, _saida(r)


def test_readme_com_codigo_bloqueia(tmp_path):
    repo = _repo(tmp_path, extras={"README.md": "# Leia\n\nVeja `Ficticia.cls:3`.\n"})
    r = _git(repo, "commit", "-m", "x")
    saida = _saida(r)
    assert r.returncode != 0
    assert "README.md:" in saida
    assert "Ficticia" not in saida


def test_com_privado_bloqueia_o_que_o_generico_aceita(tmp_path):
    repo = _repo(tmp_path, GENERICO_ACEITA)
    env = _privado(repo, tmp_path)
    r = _git(repo, "commit", "-m", "x", env=env)
    assert r.returncode != 0
    assert "docs/x.md:3" in _saida(r)
    assert "indisponível" not in _saida(r)


def test_com_privado_limpo_passa(tmp_path):
    repo = _repo(tmp_path)
    env = _privado(repo, tmp_path)
    r = _git(repo, "commit", "-m", "x", env=env)
    assert r.returncode == 0, _saida(r)


def test_com_privado_e_fonte_incompleta_bloqueia_sem_cair_no_generico(tmp_path):
    repo = _repo(tmp_path)  # conteúdo limpo: só a incompletude pode bloquear
    env = _privado(repo, tmp_path, com_fonte=False)
    r = _git(repo, "commit", "-m", "x", env=env)
    saida = _saida(r)
    assert r.returncode != 0
    assert "incompleta ou pasta ausente" in saida
    assert "indisponível" not in saida
