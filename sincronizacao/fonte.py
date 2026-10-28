"""Leitura da fonte (Database/docs) do repositório do produto."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from .config import CAMINHO_DOCS_FONTE, CAMINHO_RELATORIO

_FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


@dataclass(frozen=True)
class Pagina:
    caminho: str
    meta: dict
    corpo: str


@dataclass(frozen=True)
class Esquema:
    tabelas: dict[str, list[dict]]
    views: dict[str, list[dict]]
    fks: list[dict]


@dataclass(frozen=True)
class Fonte:
    raiz_repo: Path
    paginas: dict[str, Pagina]
    esquema: Esquema
    relatorio: dict
    dominios_md: str


def ler_pagina(texto: str, caminho: str) -> Pagina:
    m = _FRONT.match(texto)
    if not m:
        return Pagina(caminho, {}, texto)
    meta = yaml.safe_load(m.group(1)) or {}
    return Pagina(caminho, meta, texto[m.end():])


def _json(caminho: Path):
    return json.loads(caminho.read_text(encoding="utf-8"))


def carregar_fonte(raiz_repo: Path) -> Fonte:
    raiz_repo = Path(raiz_repo)
    docs = raiz_repo / CAMINHO_DOCS_FONTE
    paginas: dict[str, Pagina] = {}
    for arq in sorted(docs.rglob("*.md")):
        rel = arq.relative_to(docs).as_posix()
        if rel.startswith("_gerado/"):
            continue
        paginas[rel] = ler_pagina(arq.read_text(encoding="utf-8"), rel)
    gerado = docs / "_gerado"
    views = {
        (nome if "." in nome else f"dbo.{nome}"): cols
        for nome, cols in _json(gerado / "colunas-views.json").items()
    }
    esquema = Esquema(
        tabelas=_json(gerado / "colunas.json"),
        views=views,
        fks=_json(gerado / "fks.json"),
    )
    return Fonte(
        raiz_repo=raiz_repo,
        paginas=paginas,
        esquema=esquema,
        relatorio=_json(raiz_repo / CAMINHO_RELATORIO),
        dominios_md=(gerado / "dominios-do-produto.md").read_text(encoding="utf-8"),
    )
