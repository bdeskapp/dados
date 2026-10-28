"""Portão de publicação: git, frescor do relatório e estados da régua."""
from __future__ import annotations

import subprocess
import warnings
from dataclasses import dataclass
from pathlib import Path

from sincronizacao.config import CAMINHO_DOCS_FONTE, CAMINHO_RELATORIO
from sincronizacao.fonte import Fonte

_PASTA_REGUA = str(Path(CAMINHO_RELATORIO).parent).replace("\\", "/")


class PortaoRecusado(Exception):
    pass


@dataclass(frozen=True)
class Politica:
    commit: str
    receitas_publicadas: set[str]
    receitas_em_revisao: set[str]
    receitas_barradas: set[str]
    regras_em_revisao: set[str]


def _git(raiz: Path, *args: str) -> str:
    try:
        r = subprocess.run(["git", *args], cwd=raiz, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise PortaoRecusado(f"Falha ao executar git {' '.join(args)}: {e.stderr.strip()}") from e
    return r.stdout.strip()


def validar_git(raiz_repo: Path, ramo_integrado: str = "origin/development") -> str:
    _git(raiz_repo, "fetch", "origin")
    if _git(raiz_repo, "status", "--porcelain", "--", CAMINHO_DOCS_FONTE, _PASTA_REGUA):
        raise PortaoRecusado(
            "Há alterações locais em Database/docs ou na pasta da régua. Faça commit ou descarte antes de sincronizar."
        )
    r = subprocess.run(["git", "merge-base", "--is-ancestor", "HEAD", ramo_integrado],
                       cwd=raiz_repo, capture_output=True, text=True)
    if r.returncode != 0:
        raise PortaoRecusado(f"O HEAD da fonte não está contido em {ramo_integrado}. Envie e integre os commits antes de sincronizar.")
    return _git(raiz_repo, "rev-parse", "HEAD")


def avaliar_relatorio(relatorio: dict) -> Politica:
    if relatorio.get("veredito") != "APROVADA":
        raise PortaoRecusado(f"Veredito da régua diferente de APROVADA: {relatorio.get('veredito')!r}.")
    pub, rev, bar = set(), set(), set()
    for rec in relatorio.get("receitas", []):
        estado = rec.get("estado")
        if estado == "aprovada":
            pub.add(rec["id"])
        elif estado in ("em-disputa", "reprovada"):
            bar.add(rec["id"])
        else:
            rev.add(rec["id"])
    regras = {i["id"] for i in relatorio.get("itens", []) if i.get("estado") != "vigente"}
    return Politica("", pub, rev, bar, regras)


def validar_frescor_relatorio(raiz_repo: Path) -> None:
    ref = _git(raiz_repo, "log", "-1", "--format=%H", "--", CAMINHO_RELATORIO)
    if not ref:
        raise PortaoRecusado("O relatório da régua não tem histórico no git.")
    if _git(raiz_repo, "rev-list", f"{ref}..HEAD", "--", CAMINHO_DOCS_FONTE):
        raise PortaoRecusado("Database/docs mudou depois do último relatório da régua. Rode a régua de novo.")


def avaliar(fonte: Fonte, *, modo_dev: bool = False) -> Politica:
    commit = ""
    for etapa in (lambda: validar_git(fonte.raiz_repo), lambda: validar_frescor_relatorio(fonte.raiz_repo)):
        try:
            res = etapa()
            if res:
                commit = res
        except PortaoRecusado as e:
            if not modo_dev:
                raise
            warnings.warn(str(e))
    if modo_dev and not commit:
        try:
            commit = _git(fonte.raiz_repo, "rev-parse", "HEAD")
        except PortaoRecusado:
            commit = ""
    p = avaliar_relatorio(fonte.relatorio)
    return Politica(commit, p.receitas_publicadas, p.receitas_em_revisao, p.receitas_barradas, p.regras_em_revisao)
