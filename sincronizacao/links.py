"""Âncoras curtas de regra e reescrita de links entre páginas."""
from __future__ import annotations

import posixpath
import re
from dataclasses import dataclass

_TITULO_REGRA = re.compile(r"^(#### (R-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*-\d{2}): .*?)[ \t]*$", re.MULTILINE)
_LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
_PEND = re.compile(r"PEND-(\d+)")
_ANCORA_LONGA = re.compile(r"^(r-.+?-\d{2})-.+$")
_EXTERNO = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
_REMOVIDO = "\x00"

_JSONS_GERADOS = {"_gerado/colunas.json", "_gerado/fks.json", "_gerado/colunas-views.json"}
_SEMPRE_PUBLICADAS = {"busca.md", "dicionario/index.md", "dominios-do-produto.md", "limitacoes-conhecidas.md"}


@dataclass(frozen=True)
class ContextoLinks:
    publicadas: set[str]          # caminhos relativos a docs/
    barradas: set[str]            # receitas barradas pelo portão
    pendencias_abertas: set[str]  # {"07", ...}
    pendencias_decididas: set[str]


def ancora_regra(id_regra: str) -> str:
    return id_regra.lower()


def injetar_ancoras(texto: str) -> str:
    def sub(m: re.Match) -> str:
        titulo = m.group(1)
        if re.search(r"\{#[^}]*\}\s*$", titulo):
            return titulo
        return f"{titulo} {{#{ancora_regra(m.group(2))}}}"

    return _TITULO_REGRA.sub(sub, texto)


def _encurtar_ancora(frag: str) -> str:
    m = _ANCORA_LONGA.match(frag)
    return m.group(1) if m else frag


def _relativo(destino: str, caminho: str) -> str:
    return posixpath.relpath(destino, posixpath.dirname(caminho) or ".")


def _pendencia_aberta(numero: str, ctx: ContextoLinks) -> bool:
    """True se aberta, False se decidida; ValueError se não existir na fonte."""
    if numero in ctx.pendencias_abertas:
        return True
    if numero in ctx.pendencias_decididas:
        return False
    raise ValueError(f"PEND-{numero} não tem bloco na fonte")


def _reescrever_link(m: re.Match, caminho: str, ctx: ContextoLinks) -> str:
    texto, alvo = m.group(1), m.group(2)
    if _EXTERNO.match(alvo):
        return m.group(0)
    arq, _, frag = alvo.partition("#")
    if not arq:
        return f"[{texto}](#{_encurtar_ancora(frag)})" if frag else m.group(0)
    resolvido = posixpath.normpath(posixpath.join(posixpath.dirname(caminho), arq))

    if resolvido == "pendencias-abertas.md":
        mp = re.fullmatch(r"pend-(\d+)", frag)
        if mp:
            numero = mp.group(1)
            if _pendencia_aberta(numero, ctx):
                return f"[L-{numero}]({_relativo('limitacoes-conhecidas.md', caminho)}#l-{numero})"
            return _REMOVIDO
        return f"[{texto}]({_relativo('limitacoes-conhecidas.md', caminho)})"
    if resolvido in ctx.barradas:
        return f"{texto} (em revisão)"

    destino = None
    if resolvido == "INDEX.md":
        destino = "busca.md"
    elif resolvido in _JSONS_GERADOS:
        destino = "dicionario/index.md"
    elif resolvido == "_gerado/dominios-do-produto.md":
        destino = "dominios-do-produto.md"
    if destino:
        return f"[{texto}]({_relativo(destino, caminho)})"

    if resolvido in ctx.publicadas or resolvido in _SEMPRE_PUBLICADAS:
        novo = arq + (f"#{_encurtar_ancora(frag)}" if frag else "")
        return f"[{texto}]({novo})"
    return texto


def _limpar_linha(linha: str) -> str:
    linha = re.sub(r"[ \t]*\(\s*\x00\s*\)", "", linha)
    linha = re.sub(r"[ \t]*[,;][ \t]*\x00", "", linha)
    linha = re.sub(r"\x00[ \t]*[,;][ \t]*", "", linha)
    linha = re.sub(r"[ \t]*\x00", "", linha)
    linha = re.sub(r"[ \t]*\([ \t]*\)", "", linha)
    return linha


def _arrumar_separadores(linha: str) -> str:
    linha = re.sub(r"([·,;])(\s*[·,;])+", r"\1", linha)
    linha = re.sub(r"[ \t]*[·,;][ \t]*$", "", linha)
    linha = re.sub(r"^(\s*(?:[-*+]\s+)?)[·,;][ \t]*", r"\1", linha)
    return linha


def reescrever_links(texto: str, caminho: str, contexto: ContextoLinks) -> str:
    saida = []
    for linha in texto.split("\n"):
        nova = _LINK.sub(lambda m: _reescrever_link(m, caminho, contexto), linha)

        def mencao(m: re.Match) -> str:
            numero = m.group(1)
            return f"L-{numero}" if _pendencia_aberta(numero, contexto) else _REMOVIDO

        nova = _PEND.sub(mencao, nova)
        if nova != linha:
            nova = _limpar_linha(nova)
            nova = _arrumar_separadores(nova)
            if re.fullmatch(r"\s*(?:[-*+]\s*)?", nova) and linha.strip():
                continue
        saida.append(nova)
    return "\n".join(saida)
