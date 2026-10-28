"""Lista privada de exclusões (fora do git): objetos e colunas que não podem ser publicados."""
from __future__ import annotations

import json
import warnings
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Exclusoes:
    tabelas: set[str]
    views: set[str]
    colunas: set[str]


def carregar_exclusoes(pasta_privado: Path) -> Exclusoes:
    caminho = Path(pasta_privado) / "exclusoes.json"
    if not caminho.exists():
        warnings.warn(f"Arquivo de exclusões ausente: {caminho}. Nada será excluído.")
        return Exclusoes(set(), set(), set())
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    if not isinstance(dados, dict):
        raise ValueError("exclusoes.json deve ser um objeto")
    for chave in dados:
        if chave not in ("tabelas", "views", "colunas"):
            raise ValueError(f"chave desconhecida em exclusoes.json: {chave}")
    listas = {}
    for chave in ("tabelas", "views", "colunas"):
        valor = dados.get(chave, [])
        if not isinstance(valor, list) or not all(isinstance(i, str) for i in valor):
            raise ValueError(f"exclusoes.json: '{chave}' deve ser uma lista de textos")
        listas[chave] = set(valor)
    return Exclusoes(**listas)
