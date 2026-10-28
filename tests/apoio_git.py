"""Apoio de testes: repositório git sintético com remote bare."""
import shutil
import subprocess
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent


def _git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True, text=True)
    return r.stdout.strip()


@pytest.fixture
def repo_git_sintetico(tmp_path) -> Path:
    repo = tmp_path / "repo"
    shutil.copytree(RAIZ / "tests" / "fixtures" / "fonte", repo)
    origin = (tmp_path / "origin.git").resolve()
    _git(repo, "init", "-b", "development")
    _git(repo, "config", "user.name", "Teste")
    _git(repo, "config", "user.email", "teste@example.com")
    _git(repo, "config", "core.autocrlf", "false")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-m", "inicial")
    subprocess.run(["git", "init", "--bare", "-b", "development", str(origin)],
                   check=True, capture_output=True, text=True)
    _git(repo, "remote", "add", "origin", str(origin))
    _git(repo, "push", "-u", "origin", "development")
    return repo


def commit_local_nao_enviado(repo: Path) -> None:
    (repo / "local.txt").write_text("local", encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-m", "local")


def commitar_e_enviar(repo: Path, caminhos, msg: str) -> None:
    if isinstance(caminhos, str):
        caminhos = [caminhos]
    for c in caminhos:
        arq = repo / c
        arq.parent.mkdir(parents=True, exist_ok=True)
        arq.write_text(arq.read_text(encoding="utf-8") + f"\n{msg}\n" if arq.exists() else msg, encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-m", msg)
    _git(repo, "push", "origin", "development")
