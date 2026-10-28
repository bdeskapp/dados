"""Páginas derivadas: domínios, limitações, versão e navegação."""
from __future__ import annotations

import re

from .fonte import Pagina
from .portao import Politica

FRONT_GERADO = "---\ngerado: sincronizacao\n---\n"

AVISO_DOMINIOS = (
    '!!! warning "Valores de referência"\n'
    '    Os valores marcados como "observado na instalação de referência" foram lidos numa '
    "instalação do Bdesk e podem variar no seu ambiente. "
    'Os marcados como "definido pelo produto" são fixos.\n'
)

SEM_LIMITACAO = "Não há limitação registrada nesta versão."

_SEP = re.compile(r"(?<!\\)\|")
_COMENTARIO_GERADO = re.compile(r"^[ \t]*<!--\s*/?gerado\b.*?-->[ \t]*\r?\n?", re.DOTALL | re.MULTILINE)


def _celulas(linha: str) -> list[str]:
    return [c.strip() for c in _SEP.split(linha.strip().strip("|"))]


def _linha(celulas: list[str]) -> str:
    return "| " + " | ".join(celulas) + " |"


def _processar_tabelas(corpo: str, remover_origem: bool) -> str:
    saida: list[str] = []
    linhas = corpo.split("\n")
    i = 0
    while i < len(linhas):
        if not linhas[i].lstrip().startswith("|"):
            saida.append(linhas[i])
            i += 1
            continue
        bloco = []
        while i < len(linhas) and linhas[i].lstrip().startswith("|"):
            bloco.append(linhas[i])
            i += 1
        cab = [c.lower() for c in _celulas(bloco[0])]
        if "categoria" not in cab:
            raise ValueError("categoria")
        if "origem" not in cab or not remover_origem:
            saida.extend(bloco)
            continue
        idx = cab.index("origem")
        for n, l in enumerate(bloco):
            cels = _celulas(l)
            del cels[idx]
            saida.append(_linha(cels) if n != 1 else "|" + "|".join("---" for _ in cels) + "|")
    return "\n".join(saida)


def gerar_dominios(dominios_md: str) -> str:
    texto = _COMENTARIO_GERADO.sub("", dominios_md)
    m = re.search(r"^## ", texto, flags=re.MULTILINE)
    resto = texto[m.start():] if m else ""
    resto = _processar_tabelas(resto, remover_origem=True)
    return f"{FRONT_GERADO}# Domínios do produto\n\n{AVISO_DOMINIOS}\n{resto.rstrip()}\n"


def chaves_dominios(dominios_md: str) -> list[str]:
    chaves: list[str] = []
    linhas = dominios_md.split("\n")
    i = 0
    while i < len(linhas):
        if not linhas[i].lstrip().startswith("|"):
            i += 1
            continue
        bloco = []
        while i < len(linhas) and linhas[i].lstrip().startswith("|"):
            bloco.append(linhas[i])
            i += 1
        for l in bloco[2:]:
            cels = _celulas(l)
            if cels and cels[0]:
                chaves.append(cels[0].strip("`").strip())
    return chaves


def gerar_limitacoes(pendencias: Pagina) -> tuple[str, set[str], set[str]]:
    abertas: set[str] = set()
    decididas: set[str] = set()
    secoes: list[str] = []
    partes = re.split(r"^#### PEND-(\d+)\s*$", pendencias.corpo, flags=re.MULTILINE)
    for k in range(1, len(partes), 2):
        numero, corpo = partes[k], partes[k + 1]
        linhas = [l for l in corpo.split("\n") if l.lstrip().startswith("|")]
        if len(linhas) < 3:
            continue
        cels = _celulas(linhas[2])
        estado = cels[0].lower() if cels else ""
        if "(aberta)" in estado:
            abertas.add(numero)
            o_que = cels[1] if len(cels) > 1 else ""
            afeta = cels[2] if len(cels) > 2 else ""
            sec = f"## L-{numero} {{#l-{numero}}}\n\n{o_que}\n"
            if afeta:
                sec += f"\n**Afeta:** {afeta}\n"
            secoes.append(sec)
        elif "decidida" in estado:
            decididas.add(numero)
    cabeca = f"{FRONT_GERADO}# Limitações conhecidas\n\n"
    if not secoes:
        return cabeca + SEM_LIMITACAO + "\n", abertas, decididas
    return cabeca + "\n".join(secoes), abertas, decididas


def gerar_versao(
    politica: Politica,
    versao_produto: str,
    data: str,
    contagens: dict,
    titulos_receitas: dict[str, str] | None = None,
) -> str:
    titulos = titulos_receitas or {}
    linhas = [
        f"{FRONT_GERADO}# Versão da documentação\n",
        f"- **Versão do produto:** {versao_produto}",
        f"- **Data da sincronização:** {data}",
        f"- **Commit de origem:** `{politica.commit[:12]}`",
        "",
        "## Contagens do dicionário\n",
    ]
    for chave, valor in contagens.items():
        linhas.append(f"- {chave}: {valor}")
    linhas += ["", "## Receitas em revisão\n"]
    if politica.receitas_em_revisao:
        for r in sorted(politica.receitas_em_revisao):
            linhas.append(f"- {titulos.get(r, r)}")
    else:
        linhas.append("Nenhuma receita em revisão.")
    linhas += ["", f"Receitas não publicadas nesta versão: {len(politica.receitas_barradas)}."]
    return "\n".join(linhas) + "\n"


_PREFIXOS = ("Fato: ", "Dimensão: ", "Receita: ", "Fora de escopo: ")


def titulo_nav(h1: str) -> str:
    for p in _PREFIXOS:
        if h1.startswith(p):
            return h1[len(p):]
    return h1


def _q(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _ordenar(caminhos: list[str], primeiros: tuple[str, ...]) -> list[str]:
    fixos = [c for p in primeiros for c in caminhos if c.endswith("/" + p) or c == p]
    return fixos + sorted(c for c in caminhos if c not in fixos)


def gerar_nav(paginas_publicadas: dict[str, str]) -> str:
    def pasta(prefixo: str) -> list[str]:
        return [c for c in paginas_publicadas if c.startswith(prefixo)]

    secoes: list[tuple[str, list[str]]] = [
        ("Comece aqui", _ordenar(pasta("comece-aqui/"), ("modelo-em-5-minutos.md", "regras-de-ouro.md"))),
        ("Consumo", _ordenar(pasta("consumo/"), (
            "carga-incremental.md", "calendario-e-tempos.md", "acesso-e-leitura.md", "traduzindo-as-receitas.md"))),
        ("Modelo", _ordenar(pasta("mapa/"), ("regras-essenciais.md",))),
        ("Fatos", sorted(pasta("fatos/"))),
        ("Dimensões", sorted(pasta("dimensoes/"))),
        ("Receitas", sorted(pasta("receitas/"))),
        ("Views", sorted(pasta("views/"))),
    ]
    ref = [
        c for c in (
            "dicionario/index.md", "dominios-do-produto.md", "glossario-tela-banco.md", "busca.md",
            "limitacoes-conhecidas.md",
        ) if c in paginas_publicadas
    ]
    ref += sorted(pasta("fora-de-escopo/")) + sorted(pasta("sobre/"))
    secoes.append(("Referência", ref))

    rotulos_fixos = {
        "dicionario/index.md": "Dicionário de dados",
        "dominios-do-produto.md": "Domínios do produto",
        "glossario-tela-banco.md": "Glossário",
        "busca.md": "Busca",
        "limitacoes-conhecidas.md": "Limitações conhecidas",
    }
    saida: list[str] = []
    for nome, caminhos in secoes:
        if not caminhos:
            continue
        saida.append(f"  - {_q(nome)}:")
        for c in caminhos:
            rotulo = rotulos_fixos.get(c) or titulo_nav(paginas_publicadas[c])
            saida.append(f"    - {_q(rotulo)}: {c}")
    return "\n".join(saida)


def aplicar_nav(modelo: str, nav: str) -> str:
    return re.sub(r"^[ \t]*# \{\{NAV_GERADO\}\}[ \t]*$", lambda _m: nav, modelo, flags=re.MULTILINE)
