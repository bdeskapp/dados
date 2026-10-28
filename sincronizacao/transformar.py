"""Transformações mecânicas de página: tudo é função pura sobre texto."""
from __future__ import annotations

import re

from sincronizacao.fonte import Pagina
from sincronizacao.portao import Politica

_SENTINELA = "\x00"
_TEXTO_AVISO = "A definição desta receita ainda não foi verificada por completo. Use-a com cautela e confira os resultados."


class AjusteOrfao(Exception):
    """Um ajuste privado cujo trecho `de` não existe na página."""


def _checar_balanceamento(texto: str, nome: str) -> None:
    abre = len(re.findall(rf"<!--\s*{nome}\s*-->", texto))
    fecha = len(re.findall(rf"<!--\s*/{nome}\s*-->", texto))
    if abre != fecha:
        raise ValueError(f"Marcador de {nome} desbalanceado: {abre} de abertura e {fecha} de fechamento.")


def remover_provas(texto: str) -> str:
    _checar_balanceamento(texto, "prova")
    # Marcadores sozinhos na linha: remove as linhas inteiras.
    texto = re.sub(
        r"^[ \t]*<!-- prova -->[ \t]*\n.*?^[ \t]*<!-- /prova -->[ \t]*(?:\n|\Z)",
        "", texto, flags=re.DOTALL | re.MULTILINE,
    )
    # Marcadores inline: troca por sentinela para normalizar só as linhas afetadas.
    texto = re.sub(r"<!-- prova -->.*?<!-- /prova -->", _SENTINELA, texto, flags=re.DOTALL)
    if _SENTINELA not in texto:
        return texto
    linhas = []
    for linha in texto.split("\n"):
        if _SENTINELA in linha:
            if linha.replace(_SENTINELA, "").strip() == "":
                continue
            recuo = re.match(r"\s*", linha).group(0)
            corpo = linha[len(recuo):].replace(_SENTINELA, " ")
            corpo = re.sub(r" {2,}", " ", corpo)
            corpo = re.sub(r"\s+([.,;:!?)\]])", r"\1", corpo)
            linha = recuo + corpo.rstrip()
        linhas.append(linha)
    return "\n".join(linhas)


def trocar_decisoes(texto: str) -> str:
    _checar_balanceamento(texto, "decisao")

    def troca(m: re.Match) -> str:
        resto = texto[:m.start()].split("\n")[-1]
        resto = re.sub(r"^[\s>*\-+]*(\d+\.\s*)?", "", resto)
        inicio = resto.strip() == "" or resto.rstrip()[-1] in ".!?"
        return "Decisão do produto" if inicio else "decisão do produto"

    return re.sub(r"<!-- decisao -->.*?<!-- /decisao -->", troca, texto, flags=re.DOTALL)


def trocar_ficticios(texto: str) -> str:
    def troca(m: re.Match) -> str:
        linhas = [l for l in m.group(1).split("\n") if l.strip() != "**exemplo fictício**"]
        while linhas and linhas[0].strip() == "":
            linhas.pop(0)
        while linhas and linhas[-1].strip() == "":
            linhas.pop()
        indentado = "\n".join(("    " + l) if l.strip() else "" for l in linhas)
        return '!!! example "Exemplo fictício"\n' + indentado + "\n"

    return re.sub(
        r"^<!-- ficticio -->[ \t]*\n(.*?)^<!-- /ficticio -->[ \t]*(?:\n|\Z)",
        troca, texto, flags=re.DOTALL | re.MULTILINE,
    )


def remover_breadcrumb(texto: str) -> str:
    return re.sub(r"^Você está em:[^\n]*(?:\n|\Z)", "", texto, flags=re.MULTILINE)


def remover_blocos_internos(texto: str) -> str:
    return re.sub(r"^```json pares[^\n]*\n.*?^```[ \t]*(?:\n|\Z)", "", texto, flags=re.DOTALL | re.MULTILINE)


def limpar_sql_receita(texto: str) -> str:
    def limpa(m: re.Match) -> str:
        corpo = re.sub(r"^[ \t]*-- (?:receita:[^\n]*|so-abertas|so-encerradas)[ \t]*\n", "", m.group(2),
                       flags=re.MULTILINE)
        return m.group(1) + corpo + m.group(3)

    return re.sub(r"(^```sql[^\n]*\n)(.*?)(^```)", limpa, texto, flags=re.DOTALL | re.MULTILINE)


_SEP_CELULAS = re.compile(r"(?<!\\)\|")


def _celulas(linha: str) -> list[str]:
    return [c.strip() for c in _SEP_CELULAS.split(linha.strip().strip("|"))]


def limpar_glossario(texto: str) -> str:
    texto = re.sub(r"^Caminho comum:[^\n]*(?:\n[^\n]+)*\n*", "", texto, flags=re.MULTILINE)
    linhas = texto.split("\n")
    saida: list[str] = []
    i = 0
    while i < len(linhas):
        if not linhas[i].lstrip().startswith("|"):
            saida.append(linhas[i])
            i += 1
            continue
        j = i
        while j < len(linhas) and linhas[j].lstrip().startswith("|"):
            j += 1
        tabela = linhas[i:j]
        idx = next((k for k, c in enumerate(_celulas(tabela[0])) if c.lower().startswith("caminho tela")), None)
        if idx is None:
            saida.extend(tabela)
        else:
            for n, l in enumerate(tabela):
                cel = _celulas(l)
                if idx < len(cel):
                    del cel[idx]
                if n == 1 and all(re.fullmatch(r":?-+:?", c) for c in cel):
                    saida.append("|" + "|".join(cel) + "|")
                else:
                    saida.append("| " + " | ".join(cel) + " |")
        i = j
    return "\n".join(saida)


def reduzir_fora_de_escopo(texto: str) -> str:
    return re.sub(r"^## Documentação existente[^\n]*\n.*?(?=^## |\Z)", "", texto, flags=re.DOTALL | re.MULTILINE)


def marcar_regras_em_revisao(texto: str, regras: set[str]) -> str:
    def marca(m: re.Match) -> str:
        if m.group(2) in regras:
            return m.group(1) + ' <span class="em-revisao">em revisão</span>'
        return m.group(0)

    return re.sub(r"^(#### (R-[^\s:]+)[^\n]*?)[ \t]*$", marca, texto, flags=re.MULTILINE)


def aviso_receita_em_revisao(texto: str) -> str:
    aviso = f'\n!!! warning "Em revisão"\n    {_TEXTO_AVISO}\n'
    return re.sub(r"^(# [^\n]*\n)", lambda m: m.group(1) + aviso, texto, count=1, flags=re.MULTILINE)


def transformar_pagina(p: Pagina, politica: Politica, ajustes: dict[str, list[dict]]) -> str:
    texto = p.corpo
    for aj in ajustes.get(p.caminho, []):
        if aj["de"] not in texto:
            raise AjusteOrfao(f"Ajuste órfão em {p.caminho}: o trecho a substituir não existe mais na página.")
        texto = texto.replace(aj["de"], aj["para"])
    texto = remover_provas(texto)
    texto = trocar_decisoes(texto)
    texto = trocar_ficticios(texto)
    texto = remover_breadcrumb(texto)
    texto = remover_blocos_internos(texto)
    em_revisao = False
    if p.caminho.startswith("receitas/"):
        texto = limpar_sql_receita(texto)
        id_receita = p.caminho.rsplit("/", 1)[-1].removesuffix(".md")
        em_revisao = id_receita in politica.receitas_em_revisao
    elif p.caminho.startswith("glossario-tela-banco.md"):
        texto = limpar_glossario(texto)
    elif p.caminho.startswith("fora-de-escopo/"):
        texto = reduzir_fora_de_escopo(texto)
    texto = marcar_regras_em_revisao(texto, politica.regras_em_revisao)
    if em_revisao:
        texto = aviso_receita_em_revisao(texto)
    return texto
