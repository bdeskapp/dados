"""Verificação de vazamento: procura referências a código interno no que vai ser publicado.

Uso: python -m sincronizacao.vazamento [--repositorio] [--completo [--fonte P]] <pasta>

--repositorio: para arquivos do repositório que não vão para o site (README.md, CLAUDE.md). Não usa
a lista de permissões (sem "fora-da-lista" nem "trecho-de-codigo") e, em "arquivo-de-codigo", só barra
extensões de código do sistema de origem.

No modo genérico a saída tem só "caminho:linha categoria", nunca o trecho encontrado.
--fonte, quando omitido, vem de BDESK_FONTE ou da primeira linha de sincronizacao/privado/fonte.txt.
Códigos de saída: 0 sem achados, 1 com achados, 2 erro de uso (pasta ausente ou, no modo
completo, falta da fonte, de privado/bloqueio.json, de privado/exclusoes.json ou do
excecoes.json da fonte).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
_PASTA_PACOTE = Path(__file__).resolve().parent
_ARQ_PERMITIDOS_PUBLICOS = _PASTA_PACOTE / "permitidos-publicos.json"
_CAMINHO_EXCECOES = Path("Database") / "docs" / "_manutencao" / "excecoes.json"

CATEGORIAS = (
    "fora-da-lista",
    "arquivo-de-codigo",
    "numero-de-linha",
    "rotina",
    "bloqueio-privado",
    "definicao-de-view",
    "jargao",
    "marcador",
    "trecho-de-codigo",
)


@dataclass(frozen=True)
class Achado:
    caminho: str
    linha: int
    categoria: str  # um item de CATEGORIAS
    trecho: str = field(repr=False)  # só usado no modo completo


@dataclass(frozen=True)
class Listas:
    permitidos: set[str]  # identificadores aceitos, em casefold (esquema + domínios + públicos)
    bloqueio: list[re.Pattern]  # padrões privados (vazio no modo genérico)
    jargao: list[re.Pattern] = field(default_factory=list)  # termosInternos da fonte (modo completo)
    esquema: set[str] = field(default_factory=set)  # só nomes do esquema publicado, em casefold
    clientes: list[str] = field(default_factory=list)  # nomes de cliente dobrados, buscados como substring


# ---------------------------------------------------------------------------
# Padrões públicos, sempre ativos
# ---------------------------------------------------------------------------

_EXTENSOES = r"cs|cls|bas|frm|asp|aspx|js|ts|vb|html|json|sql|PRC|VIW|TRG|UDF"
RE_EXTENSAO = re.compile(rf"[\w\\/.:-]*\.({_EXTENSOES})\b", re.IGNORECASE)
# Modo repositório: só extensões de código do sistema de origem.
_EXTENSOES_ORIGEM = r"cls|bas|frm|ctl|asp|aspx|vb|cs|PRC|VIW|TRG|UDF|vbp|dll"
RE_EXTENSAO_ORIGEM = re.compile(rf"[\w\\/.:-]*\.({_EXTENSOES_ORIGEM})\b", re.IGNORECASE)
_CATEGORIAS_FORA_DO_REPOSITORIO = {"fora-da-lista", "trecho-de-codigo"}
RE_ROTINA = re.compile(
    r"(?i:\b(?:usp|udf|trg|cv_usp)_?\w{3,}|\bsp_\w+)|\bsp[A-Z]\w*|\bSP[A-Z0-9]{3,}\w*"
)
RE_VIEW = re.compile(r"\b(CREATE|ALTER)\s+VIEW\b", re.IGNORECASE)
RE_MARCADOR = re.compile(r"<!--\s*/?\s*(prova|decisao|ficticio)\b", re.IGNORECASE)
RE_LINHAS_PROSA = re.compile(r"(?i)\blinhas?\s+\d+(\s*(?:-|–|a|até)\s*\d+)?")
RE_ANCORA_LINHA = re.compile(r"#L\d+")
RE_LINHA_CRASE = re.compile(r"(\S+):\d+(-\d+)?")
RE_LINHA_INICIO = re.compile(r"^\s*:\d+")
RE_URL = re.compile(r"<?https?://[^\s>)\"']+>?")
RE_URL_PROIBIDA = re.compile(r"/_git/|/blob/|/tree/|[?&]path=", re.IGNORECASE)
RE_ALVO_ABSOLUTO = re.compile(r"(?i)^(?:[a-z][a-z0-9+.-]*:|//)")
RE_ALVO_ACEITO = re.compile(r"(?:\.md|/)(?:#[\w-]*)?$|^#[\w-]+$")
RE_IMAGEM = re.compile(r"(?i)\.(png|svg|jpe?g|gif|webp)$")

# ---------------------------------------------------------------------------
# Tokens
# ---------------------------------------------------------------------------

_MINUSCULA = "a-zß-öø-ÿ"
_MAIUSCULA = "A-ZÀ-ÖØ-Þ"
RE_CAMEL = re.compile(rf"[{_MINUSCULA}][{_MAIUSCULA}]")
RE_PREFIXO_COLUNA = re.compile(r"^(id|ds|dt|tp|flg|cd|nm)[A-Z]")
RE_NOME_EXT = re.compile(r"[^\W\d_][\w-]*(?:\.[^\W\d_][\w-]*)+")
RE_FIM_LINHA = re.compile(r":\d+(-\d+)?$")
RE_TEM_LETRA = re.compile(r"[^\W\d_]")
RE_TEM_ALNUM = re.compile(r"[^\W_]")
RE_PALAVRA_COMUM = re.compile(rf"[{_MAIUSCULA}]?[{_MINUSCULA}]+|\d+")
RE_MASCARA_DATA = re.compile(r"(?i)[dmyhs]+")
RE_QUALIFICADOR = re.compile(r"[a-z][a-z0-9_]*")
RE_APELIDO_SQL = re.compile(r"[a-z][a-z0-9_]*")
RE_VARIAVEL = re.compile(r"[A-Za-z]\w*")

RE_CERCA = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
RE_CRASE = re.compile(r"(`+)(.+?)\1")
RE_DEF_LINK = re.compile(r"^(\s*\[[^\]]+\]:)\s*(\S+)")
RE_LINK = re.compile(r"(!?)\[([^\]]*)\]\(\s*<?([^)\s>]*)>?(?:\s+(\"[^\"]*\"|'[^']*'))?\s*\)")
RE_ATRIBUTOS = re.compile(r"\{\s*[:#.][^}]*\}")
RE_PEDACO = re.compile(r"[\w.:/\\-]+")
RE_TOKEN_CRASE = re.compile(r"[\w.@#$\[\]/\\:]+")

_TAGS_HTML = (
    "a abbr address article aside audio b bdi bdo blockquote br button caption center cite code col colgroup "
    "data dd del details dfn div dl dt em figcaption figure font footer h1 h2 h3 h4 h5 h6 header hr i iframe img "
    "input ins kbd label legend li main mark nav ol p picture pre q s samp section small source span strong sub "
    "summary sup table tbody td tfoot th thead time tr u ul var video wbr"
).split()
RE_TAG_HTML = re.compile(
    rf"</?(?:{'|'.join(_TAGS_HTML)})(?=[\s/>])((?:[^>\"']|\"[^\"]*\"|'[^']*')*)>", re.IGNORECASE
)
RE_ATRIBUTO = re.compile(r"([\w:-]+)\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s\"'>]+))")
RE_INICIO_TAG_BRUTA = re.compile(r"<\s*([^\s/>]+)(.*?)/?\s*>$", re.DOTALL)
RE_ATRIBUTO_BRUTO = re.compile(r"([^\s\"'>/=]+)(\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s\"'>]+))?")
_ATRIBUTOS_DESTINO = {"href", "src"}
_ATRIBUTOS_TEXTO = {"title", "alt", "aria-label"}
_TAGS_CONHECIDAS = {t.casefold() for t in _TAGS_HTML} | {
    # documento HTML
    "html", "head", "body", "meta", "link", "title", "script", "style", "noscript", "template", "form",
    "select", "option", "optgroup", "textarea", "fieldset", "output", "progress", "meter", "dialog", "canvas",
    "object", "embed", "param", "base", "area", "map", "track", "menu", "search", "slot", "rp", "rt", "ruby",
    "hgroup",
    # SVG
    "svg", "g", "path", "rect", "circle", "ellipse", "line", "polyline", "polygon", "text", "tspan", "textpath",
    "defs", "use", "symbol", "desc", "clippath", "lineargradient", "radialgradient", "stop", "mask", "pattern",
    "marker", "foreignobject", "image", "filter", "switch", "metadata",
}
_ATRIBUTOS_SVG_IGNORADOS = {
    "d", "points", "transform", "viewbox", "x", "y", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry",
    "width", "height", "style", "fill", "opacity", "class",
}
RE_NUMERICO = re.compile(r"[\d\s.,%+-]*")

# ---------------------------------------------------------------------------
# SQL
# ---------------------------------------------------------------------------

_LINGUAGENS_SQL = {"sql", "tsql", "t-sql", "mssql", "sqlserver"}
_LINGUAGENS_PERMITIDAS = _LINGUAGENS_SQL | {"", "mermaid", "text", "json", "console"}
RE_PLACEHOLDER_SQL = re.compile(r"\s*@[A-Za-z]\w*\s*")
RE_COLLATION = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
RE_BR = re.compile(r"<br\s*/?>", re.IGNORECASE)
RE_SQL_COMENTARIO_OU_STRING = re.compile(r"N?'(?:[^']|'')*'|--[^\n]*|/\*.*?\*/", re.DOTALL)
RE_SQL_TOKEN = re.compile(
    r"N?'(?:[^']|'')*'|\[[^\]\n]+\]|\"[^\"\n]+\"|[@#]+[\w$#@]*|[^\W\d][\w$#@]*|\d+(?:\.\d+)?|\S"
)


def _ler_json(caminho: Path, padrao):
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return padrao


def _strings(valor) -> list[str]:
    if isinstance(valor, dict):
        valor = list(valor.keys())
    if not isinstance(valor, list):
        return []
    return [v for v in valor if isinstance(v, str) and v.strip()]


def _dobrar(texto: str) -> str:
    """Remove acentos (NFKD) e ignora caixa."""
    decomposto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in decomposto if not unicodedata.combining(c)).casefold()


def _publicos() -> dict[str, list[str]]:
    return _ler_json(_ARQ_PERMITIDOS_PUBLICOS, {})


_GRUPOS_NAO_SQL = {"mkdocs", "documentacao"}
_PALAVRAS_SQL: set[str] | None = None
_PALAVRAS_RESERVADAS: set[str] | None = None


def _palavras_chave() -> set[str]:
    """Palavras SQL aceitas como identificador (inclui partes de data como `d`, `mm`)."""
    global _PALAVRAS_SQL
    if _PALAVRAS_SQL is None:
        _PALAVRAS_SQL = {
            p.casefold()
            for chave, lista in _publicos().items()
            if chave not in _GRUPOS_NAO_SQL
            for p in _strings(lista)
        }
    return _PALAVRAS_SQL


def _palavras_reservadas() -> set[str]:
    """Palavras SQL que nunca são apelido. Partes de data (`s`, `d`, `mm`…) podem ser apelido."""
    global _PALAVRAS_RESERVADAS
    if _PALAVRAS_RESERVADAS is None:
        _PALAVRAS_RESERVADAS = {
            p.casefold()
            for chave, lista in _publicos().items()
            if chave not in _GRUPOS_NAO_SQL | {"partes_de_data"}
            for p in _strings(lista)
        }
    return _PALAVRAS_RESERVADAS


# ---------------------------------------------------------------------------
# Listas
# ---------------------------------------------------------------------------


def _nomes_do_esquema(esquema: dict) -> set[str]:
    aceitos: set[str] = set()
    for grupo in ("tabelas", "views"):
        objetos = esquema.get(grupo) or {}
        for nome, colunas in objetos.items():
            partes = nome.split(".")
            aceitos.add(nome.casefold())
            aceitos.update(p.casefold() for p in partes if p)
            for coluna in _strings(colunas):
                aceitos.add(coluna.casefold())
                aceitos.add(f"{partes[-1]}.{coluna}".casefold())
                aceitos.add(f"{nome}.{coluna}".casefold())
    return aceitos


def listas_genericas(
    raiz: Path, esquema_publicado: Path | None = None, dominios_publicados: Path | None = None
) -> Listas:
    """Esquema publicado + domínios publicados (opcional) + permitidos-publicos.json.

    Os dois caminhos opcionais substituem os arquivos de `sincronizacao/` (usados na sincronização,
    que verifica contra o esquema recém-gerado antes de copiá-lo).
    """
    pasta = Path(raiz) / "sincronizacao"
    esquema = _nomes_do_esquema(_ler_json(esquema_publicado or pasta / "esquema-publicado.json", {}))
    permitidos = set(esquema)
    permitidos.update(
        d.casefold() for d in _strings(_ler_json(dominios_publicados or pasta / "dominios-publicados.json", []))
    )
    for lista in _publicos().values():
        permitidos.update(p.casefold() for p in _strings(lista))
    return Listas(permitidos=permitidos, bloqueio=[], esquema=esquema)


def _palavra_inteira(termo: str, flags: int = 0) -> re.Pattern:
    return re.compile(rf"(?<!\w){re.escape(termo)}(?!\w)", flags)


class ModoCompletoIncompleto(Exception):
    """Falta algum arquivo exigido pelo modo completo. A mensagem só cita caminhos."""


def _faltas_do_modo_completo(raiz: Path, raiz_fonte: Path | None) -> list[str]:
    privado = Path(raiz) / "sincronizacao" / "privado"
    faltas = [str(privado / nome) for nome in ("bloqueio.json", "exclusoes.json") if not (privado / nome).is_file()]
    if raiz_fonte is None:
        faltas.append("--fonte (ou BDESK_FONTE, ou sincronizacao/privado/fonte.txt)")
    elif not (Path(raiz_fonte) / _CAMINHO_EXCECOES).is_file():
        faltas.append(str(Path(raiz_fonte) / _CAMINHO_EXCECOES))
    return faltas


def listas_completas(
    raiz: Path,
    raiz_fonte: Path | None,
    *,
    estrito: bool = False,
    esquema_publicado: Path | None = None,
    dominios_publicados: Path | None = None,
) -> Listas:
    """Listas genéricas + privado/bloqueio.json + privado/exclusoes.json + exceções da fonte.

    Com estrito=True, levanta ModoCompletoIncompleto se faltar a fonte ou algum dos arquivos.
    """
    from sincronizacao.privado import carregar_exclusoes

    if estrito:
        faltas = _faltas_do_modo_completo(raiz, raiz_fonte)
        if faltas:
            raise ModoCompletoIncompleto("Modo completo incompleto; faltam: " + "; ".join(faltas))

    base = listas_genericas(raiz, esquema_publicado, dominios_publicados)
    pasta_privado = Path(raiz) / "sincronizacao" / "privado"
    bloqueio: list[re.Pattern] = []
    jargao: list[re.Pattern] = []
    clientes: list[str] = []

    privado = _ler_json(pasta_privado / "bloqueio.json", {})
    for padrao in _strings(privado.get("padroes") if isinstance(privado, dict) else None):
        bloqueio.append(re.compile(padrao, re.IGNORECASE))

    exclusoes = carregar_exclusoes(pasta_privado)
    nomes_excluidos: set[str] = set()
    for nome in exclusoes.tabelas | exclusoes.views:
        nomes_excluidos.add(nome)
        nomes_excluidos.add(nome.split(".")[-1])
    for coluna in exclusoes.colunas:
        partes = coluna.split(".")
        if len(partes) >= 2:
            nomes_excluidos.add(coluna)
            nomes_excluidos.add(".".join(partes[-2:]))  # Tabela.coluna, sempre
        solto = partes[-1]
        if _cara_de_identificador(solto) and solto.casefold() not in base.esquema:
            nomes_excluidos.add(solto)
    for nome in sorted(n for n in nomes_excluidos if n.strip()):
        bloqueio.append(_palavra_inteira(nome, re.IGNORECASE))

    if raiz_fonte is not None:
        excecoes = _ler_json(Path(raiz_fonte) / _CAMINHO_EXCECOES, {})
        if isinstance(excecoes, dict):
            for nome in _strings(excecoes.get("nomesDeCliente")):
                if len(nome) >= 4:
                    clientes.append(_dobrar(nome))
                else:
                    bloqueio.append(_palavra_inteira(nome, re.IGNORECASE))
            for variavel in _strings(excecoes.get("variaveisDeCodigo")):
                bloqueio.append(_palavra_inteira(variavel))
            for termo in _strings(excecoes.get("termosInternos")):
                jargao.append(_palavra_inteira(termo, re.IGNORECASE))
    return Listas(
        permitidos=base.permitidos, bloqueio=bloqueio, jargao=jargao, esquema=base.esquema, clientes=clientes
    )


# ---------------------------------------------------------------------------
# Cara de identificador
# ---------------------------------------------------------------------------


def _mascara_de_data(tok: str) -> bool:
    return bool(RE_MASCARA_DATA.fullmatch(tok)) or all(
        RE_MASCARA_DATA.fullmatch(p) for p in re.split(r"[-/\\]", tok)
    )


def _cara_de_identificador(tok: str) -> bool:
    """Prosa: CamelCase, `_`, `nome.ext`, `/` suspeita, `:\\d+`."""
    if _mascara_de_data(tok):
        return False
    if RE_CAMEL.search(tok) or "_" in tok:
        return True
    if RE_FIM_LINHA.search(tok) and RE_TEM_LETRA.search(tok):
        return True
    if "/" in tok or "\\" in tok:
        if len(tok) > 1 and (tok[0] in "/\\" or tok[-1] in "/\\"):
            return True
        partes = re.split(r"[/\\]", tok)
        if len(partes) > 2 and not all(p.isdigit() for p in partes):
            return True
        return not all(RE_PALAVRA_COMUM.fullmatch(p) for p in partes)
    return bool(RE_NOME_EXT.fullmatch(tok))


def _cara_de_identificador_crase(tok: str) -> bool:
    """Crase: alinhada com a checagem da fonte; palavra comum passa."""
    if _mascara_de_data(tok):
        return False
    return bool(
        RE_CAMEL.search(tok)
        or RE_PREFIXO_COLUNA.match(tok)
        or "_" in tok
        or "/" in tok
        or "\\" in tok
        or RE_NOME_EXT.fullmatch(tok)
        or re.search(r":\d", tok)
        or RE_ROTINA.search(tok)
        or re.search(r"\w\.\w", tok)
    )


def _abreviacao(bruto: str, tok: str) -> bool:
    if "." not in tok:
        return False
    partes = tok.split(".")
    return all(len(p) <= 1 for p in partes) or (bruto.endswith(".") and all(len(p) <= 2 for p in partes))


@dataclass
class _Item:
    tipo: str  # "ref", "str", "var", "num", "sym"
    partes: list[str]
    pos: int
    delimitado: bool = False  # [nome] ou "nome"


# ---------------------------------------------------------------------------
# Coletor de achados
# ---------------------------------------------------------------------------


class _Coletor:
    def __init__(self, caminho: str, listas: Listas, profundidade: int = 0, modo_repositorio: bool = False):
        self.caminho = caminho
        self.modo_repositorio = modo_repositorio
        self.listas = listas
        self.profundidade = profundidade
        self.nomes_de_resultado: set[str] = set()  # `AS nome` dos blocos SQL da página, em casefold
        self.achados: list[Achado] = []
        self._vistos: set[tuple[int, str, str]] = set()

    def add(self, linha: int, categoria: str, trecho: str) -> None:
        if self.modo_repositorio:
            if categoria in _CATEGORIAS_FORA_DO_REPOSITORIO:
                return
            if categoria == "arquivo-de-codigo" and not RE_EXTENSAO_ORIGEM.search(trecho):
                return  # links, URLs e extensões deste repositório passam
        chave = (linha, categoria, trecho)
        if chave not in self._vistos:
            self._vistos.add(chave)
            self.achados.append(Achado(self.caminho, linha, categoria, trecho))

    def resultado(self) -> list[Achado]:
        return sorted(self.achados, key=lambda a: a.linha)

    def bloqueado(self, texto: str) -> bool:
        if any(p.search(texto) for p in self.listas.bloqueio) or any(p.search(texto) for p in self.listas.jargao):
            return True
        dobrado = _dobrar(texto)
        return any(c in dobrado for c in self.listas.clientes)

    # -- padrões públicos e privados -------------------------------------

    def padroes(self, texto: str, linha: int, fora_de_sql: bool) -> None:
        for m in RE_MARCADOR.finditer(texto):
            self.add(linha, "marcador", m.group(0))
        for m in RE_ROTINA.finditer(texto):
            self.add(linha, "rotina", m.group(0))
        for m in RE_VIEW.finditer(texto):
            self.add(linha, "definicao-de-view", m.group(0))
        for m in RE_LINHAS_PROSA.finditer(texto):
            self.add(linha, "numero-de-linha", m.group(0))
        for m in RE_ANCORA_LINHA.finditer(texto):
            self.add(linha, "numero-de-linha", m.group(0))
        if fora_de_sql:
            for m in (RE_EXTENSAO_ORIGEM if self.modo_repositorio else RE_EXTENSAO).finditer(texto):
                self.add(linha, "arquivo-de-codigo", m.group(0))
        for padrao in self.listas.bloqueio:
            for m in padrao.finditer(texto):
                self.add(linha, "bloqueio-privado", m.group(0))
        if self.listas.clientes:
            dobrado = _dobrar(texto)
            for cliente in self.listas.clientes:
                if cliente in dobrado:
                    self.add(linha, "bloqueio-privado", cliente)
        for padrao in self.listas.jargao:
            for m in padrao.finditer(texto):
                self.add(linha, "jargao", m.group(0))

    # -- lista de permissões (fora do SQL) ---------------------------------

    def permitido(self, tok: str) -> bool:
        if re.search(r":\d", tok):
            return False
        t = tok.casefold()
        if t in self.listas.permitidos or t in self.nomes_de_resultado:
            return True
        partes = [p for p in re.split(r"[./\\]", tok) if p]
        if len(partes) < 2:
            return False
        if RE_QUALIFICADOR.fullmatch(partes[0]):
            partes = partes[1:]  # `x.Coluna`: x minúsculo, Coluna do esquema ou nome de resultado
        return all(self._nome_de_coluna(p) for p in partes)

    def _nome_de_coluna(self, nome: str) -> bool:
        n = nome.casefold()
        return n in self.listas.esquema or n in self.nomes_de_resultado

    def coletar_nomes_de_resultado(self, texto_sql: str) -> None:
        """Guarda os nomes definidos com `AS nome` (sem rotina nem bloqueio) para a página toda."""
        reservadas = _palavras_reservadas()
        itens = self._itens_sql(RE_SQL_COMENTARIO_OU_STRING.sub(" ", texto_sql))
        for ant, it in zip(itens, itens[1:]):
            if not (ant.tipo == "ref" and len(ant.partes) == 1 and ant.partes[0].upper() == "AS"):
                continue
            if it.tipo != "ref" or len(it.partes) != 1 or it.delimitado:
                continue
            nome = it.partes[0]
            if nome.casefold() in reservadas or RE_ROTINA.search(nome) or self.bloqueado(nome):
                continue
            self.nomes_de_resultado.add(nome.casefold())

    # -- destinos de link e URLs -----------------------------------------

    def url(self, valor: str, linha: int) -> None:
        if RE_URL_PROIBIDA.search(valor):
            self.add(linha, "arquivo-de-codigo", valor)

    def destino(self, alvo: str, linha: int, imagem: bool = False, relativo_estrito: bool = True) -> None:
        alvo = alvo.strip().strip("<>")
        if not alvo:
            return
        self.padroes(alvo, linha, fora_de_sql=True)
        if RE_ALVO_ABSOLUTO.match(alvo):
            self.url(alvo, linha)
            return
        if not relativo_estrito:
            return
        caminho_alvo, _, ancora = alvo.partition("#")
        segmentos = caminho_alvo.split("/")
        e_imagem = imagem and RE_IMAGEM.search(caminho_alvo)
        if not e_imagem and not RE_ALVO_ACEITO.search(alvo):
            self.add(linha, "arquivo-de-codigo", alvo)
        subidas = 0
        for seg in segmentos:
            if seg != "..":
                break
            subidas += 1
        if subidas > self.profundidade:
            self.add(linha, "arquivo-de-codigo", alvo)  # sobe além da raiz do site
        for k, seg in enumerate(segmentos):
            if seg in ("", ".", ".."):
                continue
            if seg.endswith(".md"):
                seg = seg[:-3]
            elif e_imagem and k == len(segmentos) - 1:
                seg = seg.rsplit(".", 1)[0]
            self.tokens_prosa(seg, linha)
        self.tokens_prosa(ancora, linha)

    def _sem_urls(self, texto: str, linha: int) -> str:
        def _troca(m: re.Match) -> str:
            self.url(m.group(0), linha)
            return " "

        return RE_URL.sub(_troca, texto)

    # -- prosa ---------------------------------------------------------------

    def tokens_prosa(self, texto: str, linha: int) -> None:
        for m in RE_PEDACO.finditer(texto):
            bruto = m.group(0)
            tok = bruto.strip(".:-_")
            if not tok or not RE_TEM_ALNUM.search(tok):
                continue
            if _abreviacao(bruto, tok) or not _cara_de_identificador(tok):
                continue
            if self.permitido(tok):
                continue
            self.add(linha, "fora-da-lista", tok)
            if RE_FIM_LINHA.search(tok):
                self.add(linha, "numero-de-linha", tok)

    def crase(self, conteudo: str, linha: int) -> None:
        self.padroes(conteudo, linha, fora_de_sql=True)
        for m in RE_LINHA_CRASE.finditer(conteudo):
            if "://" in m.group(1):
                continue  # porta de URL, não número de linha
            if not m.group(1).strip("'\"(").isdigit():
                self.add(linha, "numero-de-linha", m.group(0))
        if RE_LINHA_INICIO.match(conteudo):
            self.add(linha, "numero-de-linha", conteudo.strip())
        for m in RE_TOKEN_CRASE.finditer(conteudo):
            tok = m.group(0).replace("[", "").replace("]", "").strip(".:")
            if tok[:1] in ("@", "#"):
                resto = tok.lstrip("@#")
                if RE_VARIAVEL.fullmatch(resto):
                    continue  # variável ou tabela temporária do leitor
                tok = resto
            if not tok or re.fullmatch(r"[\d.:]+", tok):
                continue
            if not _cara_de_identificador_crase(tok) or RE_ROTINA.search(tok):
                continue  # palavra comum passa; rotina já foi registrada
            if self.permitido(tok):
                continue
            self.add(linha, "fora-da-lista", tok)

    def _crases(self, texto: str, linha: int) -> str:
        def _troca(m: re.Match) -> str:
            self.crase(m.group(2), linha)
            return " "

        return RE_CRASE.sub(_troca, texto)

    def texto(self, texto: str, linha: int) -> None:
        """Texto puro: dados de HTML, blocos de código que não são SQL, arquivos de texto."""
        self.padroes(texto, linha, fora_de_sql=True)
        resto = self._crases(texto, linha)
        resto = resto.replace("<!--", " ").replace("-->", " ")
        resto = self._sem_urls(resto, linha)
        self.tokens_prosa(resto, linha)

    def prosa_markdown(self, texto: str, linha: int) -> None:
        """Prosa de Markdown: remove só tags HTML5 conhecidas e verifica os atributos."""
        self.padroes(texto, linha, fora_de_sql=True)
        resto = self._crases(texto, linha)
        resto = resto.replace("<!--", " ").replace("-->", " ")

        def _definicao(m: re.Match) -> str:
            self.destino(m.group(2), linha)
            return m.group(1)

        def _link(m: re.Match) -> str:
            self.destino(m.group(3), linha, imagem=bool(m.group(1)))
            if m.group(4):
                self.texto(m.group(4)[1:-1], linha)  # título do link
            return f" {m.group(2)} "

        def _tag(m: re.Match) -> str:
            self.atributos(m.group(1), linha, relativo_estrito=True)
            return " "

        def _attr_list(m: re.Match) -> str:
            self.atributos(m.group(0)[1:-1], linha, relativo_estrito=True)
            return " "

        resto = RE_DEF_LINK.sub(_definicao, resto)
        resto = RE_LINK.sub(_link, resto)
        resto = self._sem_urls(resto, linha)
        resto = RE_TAG_HTML.sub(_tag, resto)
        resto = RE_ATRIBUTOS.sub(_attr_list, resto)
        self.tokens_prosa(resto, linha)

    def atributos(self, texto_atributos: str, linha: int, relativo_estrito: bool) -> None:
        """Verifica os pares nome=valor e passa o resto (nomes soltos, #id, .classe) pela prosa."""
        for m in RE_ATRIBUTO.finditer(texto_atributos):
            nome = m.group(1).lower()
            valor = next((g for g in m.group(2, 3, 4) if g is not None), "")
            self.atributo(nome, valor, linha, relativo_estrito)
        self.tokens_prosa(RE_ATRIBUTO.sub(" ", texto_atributos), linha)

    def atributo(self, nome: str, valor: str, linha: int, relativo_estrito: bool) -> None:
        if nome in _ATRIBUTOS_DESTINO or nome.endswith(":href"):
            self.destino(valor, linha, imagem=(nome == "src"), relativo_estrito=relativo_estrito)
        else:
            self.texto(valor, linha)

    # -- SQL -----------------------------------------------------------------

    def sql(self, texto: str, linha0: int) -> None:
        for k, l in enumerate(texto.split("\n")):
            self.padroes(l, linha0 + k, fora_de_sql=False)

        limpo = list(texto)
        for m in RE_SQL_COMENTARIO_OU_STRING.finditer(texto):
            s = m.group(0)
            base = linha0 + texto.count("\n", 0, m.start())
            if s.startswith("--") or s.startswith("/*"):
                corpo = s[2:] if s.startswith("--") else s[2:-2]
                for p in range(m.start(), m.end()):
                    if limpo[p] != "\n":
                        limpo[p] = " "
                if s.startswith("/*") and RE_PLACEHOLDER_SQL.fullmatch(corpo):
                    continue  # placeholder /* @nome */
            else:
                corpo = s[s.index("'") + 1 : -1].replace("''", "'")
            for k, l in enumerate(corpo.split("\n")):
                self.texto(l, base + k)  # comentários e literais passam pela prosa
        limpo_txt = "".join(limpo)

        itens = self._itens_sql(limpo_txt)
        locais = self._locais_sql(itens)  # primeira passada: apelidos do bloco inteiro
        for k, it in enumerate(itens):
            if it.tipo != "ref":
                continue
            if any(RE_ROTINA.search(p) for p in it.partes):
                continue  # já registrado como "rotina" pelos padrões
            ant = itens[k - 1] if k else None
            if (
                ant is not None and ant.tipo == "ref" and len(ant.partes) == 1 and ant.partes[0].upper() == "COLLATE"
                and len(it.partes) == 1 and RE_COLLATION.fullmatch(it.partes[0]) and not self.bloqueado(it.partes[0])
            ):
                continue  # nome de collation
            if self._permitido_sql(it.partes, locais):
                continue
            self.add(linha0 + limpo_txt.count("\n", 0, it.pos), "fora-da-lista", ".".join(it.partes))

    def _permitido_sql(self, partes: list[str], locais: set[str]) -> bool:
        palavras = _palavras_chave()
        nomes = [p.casefold() for p in partes]
        if len(nomes) == 1:
            n = nomes[0]
            return n in palavras or n in self.listas.permitidos or n in locais or n in self.nomes_de_resultado
        resto = nomes[1:] if nomes[0] in locais else nomes
        if all(self._nome_de_coluna(n) for n in resto):
            return True
        return all(n in palavras for n in nomes)  # ex.: INFORMATION_SCHEMA.COLUMNS

    @staticmethod
    def _itens_sql(texto: str) -> list[_Item]:
        toks: list[_Item] = []
        for m in RE_SQL_TOKEN.finditer(texto):
            v = m.group(0)
            if v.startswith("'") or v.startswith("N'"):
                toks.append(_Item("str", [v], m.start()))
            elif v[0] in "[\"":
                toks.append(_Item("id", [v[1:-1]], m.start(), delimitado=True))
            elif v[0] in "@#":
                toks.append(_Item("var", [v], m.start()))
            elif v[0].isdigit():
                toks.append(_Item("num", [v], m.start()))
            elif RE_TEM_LETRA.match(v):
                toks.append(_Item("id", [v], m.start()))
            else:
                toks.append(_Item("sym", [v], m.start()))
        itens: list[_Item] = []
        i = 0
        while i < len(toks):
            t = toks[i]
            if t.tipo != "id":
                itens.append(t)
                i += 1
                continue
            partes = [t.partes[0]]
            j = i + 1
            while j + 1 < len(toks) and toks[j].partes[0] == "." and toks[j + 1].tipo == "id":
                partes.append(toks[j + 1].partes[0])
                j += 2
            itens.append(_Item("ref", partes, t.pos, delimitado=t.delimitado and len(partes) == 1))
            i = j
        return itens

    def _prosa_aceita(self, texto: str) -> bool:
        for m in RE_PEDACO.finditer(texto):
            bruto = m.group(0)
            tok = bruto.strip(".:-_")
            if not tok or not RE_TEM_ALNUM.search(tok) or _abreviacao(bruto, tok):
                continue
            if _cara_de_identificador(tok) and not self.permitido(tok):
                return False
        return True

    def _apelido_valido(self, nome: str, delimitado: bool, apos_as: bool) -> bool:
        if RE_ROTINA.search(nome) or self.bloqueado(nome):
            return False
        if delimitado:
            return self._prosa_aceita(nome)  # AS [Total de abertas], AS "Total"
        if apos_as:
            return True  # AS Total
        return bool(RE_APELIDO_SQL.fullmatch(nome)) or len(nome) <= 3

    def _locais_sql(self, itens: list[_Item]) -> set[str]:
        """Apelidos definidos no bloco: AS x; FROM/JOIN <ref> x; ) x; x AS ( ; SELECT|, x =."""
        palavras = _palavras_reservadas()

        def chave(it: _Item | None) -> str | None:
            if it and it.tipo == "ref" and len(it.partes) == 1 and it.partes[0].casefold() in palavras:
                return it.partes[0].upper()
            return None

        def simbolo(it: _Item | None, s: str) -> bool:
            return bool(it) and it.tipo == "sym" and it.partes[0] == s

        def item(k: int) -> _Item | None:
            return itens[k] if 0 <= k < len(itens) else None

        locais: set[str] = set()
        for k, it in enumerate(itens):
            if it.tipo != "ref" or len(it.partes) != 1 or chave(it):
                continue
            ant, ant2, prox, prox2 = item(k - 1), item(k - 2), item(k + 1), item(k + 2)
            define = (
                chave(ant) == "AS"
                or (ant is not None and ant.tipo == "ref" and not chave(ant) and chave(ant2) in ("FROM", "JOIN"))
                or simbolo(ant, ")")
                or (chave(prox) == "AS" and simbolo(prox2, "("))
                or (simbolo(prox, "=") and (chave(ant) == "SELECT" or simbolo(ant, ",")))
            )
            if define and self._apelido_valido(it.partes[0], it.delimitado, chave(ant) == "AS"):
                locais.add(it.partes[0].casefold())
        return locais


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------


def verificar_markdown(
    texto: str, caminho: str, listas: Listas, *, profundidade: int = 0, modo_repositorio: bool = False
) -> list[Achado]:
    """profundidade: número de pastas entre a página e a raiz do site (limite para `../` nos links).

    modo_repositorio: arquivo do repositório que não vai para o site (README.md, CLAUDE.md).
    """
    col = _Coletor(caminho, listas, profundidade, modo_repositorio)
    linhas = texto.splitlines()
    partes = list(_partes_markdown(linhas))
    for parte in partes:  # nomes de resultado (`AS nome`) valem para a página toda
        if parte[0] == "cerca" and parte[2] in _LINGUAGENS_SQL:
            col.coletar_nomes_de_resultado("\n".join(parte[4]))
    for parte in partes:
        if parte[0] == "prosa":
            _, n, linha = parte
            col.prosa_markdown(linha, n)
            continue
        _, n, linguagem, info, corpo, fim = parte
        if linguagem not in _LINGUAGENS_PERMITIDAS:
            col.add(n, "trecho-de-codigo", linguagem)
        col.texto(info, n)
        if linguagem in _LINGUAGENS_SQL:
            col.sql("\n".join(corpo), n + 1)
        else:
            for k, l in enumerate(corpo):
                if linguagem == "mermaid":
                    l = RE_BR.sub(" ", l)  # <br/> em rótulo é tag HTML; o texto do rótulo segue verificado
                col.texto(l, n + 1 + k)
        if fim is not None:
            col.padroes(fim[1], fim[0], fora_de_sql=True)
    return col.resultado()


def _partes_markdown(linhas: list[str]):
    """("prosa", nº, linha) ou ("cerca", nº, linguagem, info, corpo, (nº, linha de fechamento) | None)."""
    i = 0
    while i < len(linhas):
        m = RE_CERCA.match(linhas[i])
        if not m:
            yield ("prosa", i + 1, linhas[i])
            i += 1
            continue
        cerca, info = m.group(1), m.group(2)
        fim = re.compile(rf"^\s*{re.escape(cerca[0])}{{{len(cerca)},}}\s*$")
        j = i + 1
        while j < len(linhas) and not fim.match(linhas[j]):
            j += 1
        linguagem = re.match(r"[\s{.]*([\w+-]*)", info).group(1).lower()
        fechamento = (j + 1, linhas[j]) if j < len(linhas) else None
        yield ("cerca", i + 1, linguagem, info, linhas[i + 1 : j], fechamento)
        i = j + 1


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------


RE_PARECE_SQL = re.compile(
    r"^\s*(?:(?:--[^\n]*|/\*.*?\*/)\s*)*;?\s*(?:WITH|SELECT|DECLARE|SET|USE|EXEC|CREATE|ALTER|INSERT|UPDATE"
    r"|DELETE|MERGE|IF)\b|\bSELECT\b.*\bFROM\b",
    re.IGNORECASE | re.DOTALL,
)
RE_PARECE_MERMAID = re.compile(
    r"^\s*(?:%%[^\n]*\n\s*)*(?:flowchart|graph|erDiagram|sequenceDiagram|classDiagram|stateDiagram(?:-v2)?"
    r"|gantt|pie|journey|mindmap|timeline)\b"
)


def _tipo_do_bloco(conteudo: str, sql: bool, mermaid: bool) -> str:
    """Bloco <pre> do HTML: "sql", "mermaid" ou "codigo". Sem classe de linguagem, decide pelo conteúdo."""
    if sql:
        return "sql"
    if mermaid or RE_PARECE_MERMAID.match(conteudo):
        return "mermaid"
    if RE_PARECE_SQL.search(conteudo):
        return "sql"
    return "codigo"


class _ExtratorHtml(HTMLParser):
    RE_CLASSE_SQL = re.compile(r"\blanguage-(sql|tsql|t-sql|mssql|sqlserver)\b", re.IGNORECASE)
    RE_CLASSE_MERMAID = re.compile(r"\b(?:language-)?mermaid\b", re.IGNORECASE)

    def __init__(self, ignorar: set[str], todos_atributos: bool = False) -> None:
        super().__init__(convert_charrefs=True)
        self.tags_ignoradas = ignorar
        self.todos_atributos = todos_atributos
        self.residuos: list[tuple[int, str]] = []
        self.ignorar = 0
        self.pre = 0
        self.code = 0
        self.div_sql = False
        self.prosa: dict[int, list[str]] = {}
        self.crases: list[tuple[int, str]] = []
        self.blocos: list[tuple[int, str, bool]] = []
        self.comentarios: list[tuple[int, str]] = []
        self.atributos: list[tuple[int, str, str]] = []
        self._bloco: list | None = None
        self._crase: list | None = None

    def _texto_prosa(self, dados: str, linha: int) -> None:
        for k, parte in enumerate(dados.split("\n")):
            self.prosa.setdefault(linha + k, []).append(parte)

    def handle_starttag(self, tag, attrs):
        if tag in self.tags_ignoradas:
            self.ignorar += 1
            return
        if self.ignorar:
            return
        linha = self.getpos()[0]
        self._residuos_da_tag(linha)
        for nome, valor in attrs:
            if not valor:
                continue
            if self.todos_atributos:
                ignorado = (
                    nome in _ATRIBUTOS_SVG_IGNORADOS
                    or nome.startswith(("stroke", "font-"))
                    or RE_NUMERICO.fullmatch(valor)
                )
                if not ignorado:
                    self.atributos.append((linha, nome, valor))
            elif nome in (_ATRIBUTOS_DESTINO | _ATRIBUTOS_TEXTO):
                self.atributos.append((linha, nome, valor))
        classe = dict(attrs).get("class") or ""
        sql = bool(self.RE_CLASSE_SQL.search(classe))
        mermaid = bool(self.RE_CLASSE_MERMAID.search(classe))
        if tag == "div":
            self.div_sql = sql
        if tag == "pre":
            self.pre += 1
            if self.pre == 1:
                self._bloco = [None, [], sql or self.div_sql, mermaid]
        elif tag == "code":
            if self.pre:
                if self._bloco is not None:
                    self._bloco[2] = self._bloco[2] or sql
                    self._bloco[3] = self._bloco[3] or mermaid
            else:
                self.code += 1
                if self.code == 1:
                    self._crase = [None, []]
        elif not self.pre and not self.code:
            self._texto_prosa(" ", linha)

    def _residuos_da_tag(self, linha: int) -> None:
        """Nome de tag desconhecido e atributos sem valor, com a caixa original."""
        m = RE_INICIO_TAG_BRUTA.match(self.get_starttag_text() or "")
        if not m:
            return
        nome, resto = m.group(1), m.group(2)
        if nome.casefold() not in _TAGS_CONHECIDAS:
            self.residuos.append((linha, nome))
        for a in RE_ATRIBUTO_BRUTO.finditer(resto):
            if not a.group(2):
                self.residuos.append((linha, a.group(1)))

    def handle_endtag(self, tag):
        if tag in self.tags_ignoradas:
            self.ignorar = max(0, self.ignorar - 1)
            return
        if self.ignorar:
            return
        if tag == "pre" and self.pre:
            self.pre -= 1
            if self.pre == 0 and self._bloco is not None:
                linha, partes, sql, mermaid = self._bloco
                if linha is not None:
                    conteudo = "".join(partes)
                    self.blocos.append((linha, conteudo, _tipo_do_bloco(conteudo, sql, mermaid)))
                self._bloco = None
        elif tag == "code" and not self.pre and self.code:
            self.code -= 1
            if self.code == 0 and self._crase is not None:
                linha, partes = self._crase
                if linha is not None:
                    self.crases.append((linha, "".join(partes)))
                self._crase = None
        elif not self.pre and not self.code:
            self._texto_prosa(" ", self.getpos()[0])

    def handle_data(self, data):
        if self.ignorar:
            return
        linha = self.getpos()[0]
        if self.pre and self._bloco is not None:
            if self._bloco[0] is None:
                self._bloco[0] = linha
            self._bloco[1].append(data)
        elif self.code and self._crase is not None:
            if self._crase[0] is None:
                self._crase[0] = linha
            self._crase[1].append(data)
        else:
            self._texto_prosa(data, linha)

    def handle_comment(self, data):
        if not self.ignorar:
            self.comentarios.append((self.getpos()[0], data))


def _verificar_html(
    texto: str,
    caminho: str,
    listas: Listas,
    ignorar: set[str],
    todos_atributos: bool = False,
    modo_repositorio: bool = False,
    nomes_de_resultado: set[str] | None = None,
) -> list[Achado]:
    extrator = _ExtratorHtml(ignorar, todos_atributos)
    extrator.feed(texto)
    extrator.close()
    col = _Coletor(caminho, listas, modo_repositorio=modo_repositorio)
    col.nomes_de_resultado.update(nomes_de_resultado or ())
    for _, conteudo, tipo in extrator.blocos:  # apelidos da página antes da prosa e das tabelas
        if tipo == "sql":
            col.coletar_nomes_de_resultado(conteudo)
    for linha, residuo in extrator.residuos:
        col.tokens_prosa(residuo, linha)
    for linha, partes in sorted(extrator.prosa.items()):
        col.texto("".join(partes), linha)
    for linha, conteudo in extrator.crases:
        col.crase(" ".join(conteudo.split("\n")), linha)
    for linha, conteudo, tipo in extrator.blocos:
        if tipo == "sql":
            col.sql(conteudo, linha)
        else:
            for k, l in enumerate(conteudo.split("\n")):
                if tipo == "mermaid":
                    l = RE_BR.sub(" ", l)  # <br/> em rótulo é tag HTML; o texto do rótulo segue verificado
                col.texto(l, linha + k)
    for linha, conteudo in extrator.comentarios:
        for k, l in enumerate(conteudo.split("\n")):
            col.texto(("<!--" if k == 0 else "") + l, linha + k)
    for linha, nome, valor in extrator.atributos:
        col.atributo(nome, valor, linha, relativo_estrito=False)
    return col.resultado()


_IGNORAR_HTML = {"script", "style", "svg", "template"}


def verificar_html(
    texto: str,
    caminho: str,
    listas: Listas,
    *,
    modo_repositorio: bool = False,
    nomes_de_resultado: set[str] | None = None,
) -> list[Achado]:
    """nomes_de_resultado: `AS nome` já coletados em outras partes da mesma página."""
    return _verificar_html(
        texto, caminho, listas, _IGNORAR_HTML, modo_repositorio=modo_repositorio,
        nomes_de_resultado=nomes_de_resultado,
    )


def _nomes_de_resultado_html(texto: str, listas: Listas) -> set[str]:
    extrator = _ExtratorHtml(_IGNORAR_HTML)
    extrator.feed(texto)
    extrator.close()
    col = _Coletor("", listas)
    for _, conteudo, tipo in extrator.blocos:
        if tipo == "sql":
            col.coletar_nomes_de_resultado(conteudo)
    return col.nomes_de_resultado


def verificar_texto(texto: str, caminho: str, listas: Listas, *, modo_repositorio: bool = False) -> list[Achado]:
    col = _Coletor(caminho, listas, modo_repositorio=modo_repositorio)
    for n, linha in enumerate(texto.splitlines(), start=1):
        col.texto(linha, n)
    return col.resultado()


# ---------------------------------------------------------------------------
# Árvore e CLI
# ---------------------------------------------------------------------------

_EXTENSOES_TEXTO = {".txt", ".csv", ".yml", ".yaml", ".json"}


def _verificar_indice_busca(
    texto: str, caminho: str, listas: Listas, modo_repositorio: bool = False
) -> list[Achado]:
    dados = json.loads(texto)
    docs = [d for d in (dados.get("docs") or []) if isinstance(d, dict)]
    # Cada seção é um documento; os apelidos de resultado valem para a página (location antes do #).
    por_pagina: dict[str, set[str]] = {}
    for doc in docs:
        pagina = str(doc.get("location") or "").split("#", 1)[0]
        valor = doc.get("text")
        if isinstance(valor, str) and valor:
            por_pagina.setdefault(pagina, set()).update(_nomes_de_resultado_html(valor, listas))
    achados: list[Achado] = []
    for n, doc in enumerate(docs, start=1):
        nomes = por_pagina.get(str(doc.get("location") or "").split("#", 1)[0], set())
        for campo in ("title", "text"):
            valor = doc.get(campo)
            if isinstance(valor, str) and valor:
                for a in verificar_html(
                    valor, caminho, listas, modo_repositorio=modo_repositorio, nomes_de_resultado=nomes
                ):
                    achados.append(Achado(caminho, n, a.categoria, a.trecho))
    return achados


def verificar_arvore(raiz: Path, listas: Listas, *, modo_repositorio: bool = False) -> list[Achado]:
    """*.md; *.html; search/search_index.json; *.svg; *.txt, *.csv, *.yml, *.yaml e *.json como texto."""
    m = modo_repositorio
    raiz = Path(raiz)
    achados: list[Achado] = []
    for arq in sorted(raiz.rglob("*")):
        if not arq.is_file():
            continue
        rel = arq.relative_to(raiz).as_posix()
        caminho = f"{raiz.name}/{rel}"
        sufixo = arq.suffix.lower()
        if sufixo not in {".md", ".html", ".svg"} | _EXTENSOES_TEXTO:
            continue
        conteudo = arq.read_text(encoding="utf-8", errors="replace")
        if sufixo == ".md":
            achados += verificar_markdown(
                conteudo, caminho, listas, profundidade=rel.count("/"), modo_repositorio=m
            )
        elif sufixo == ".html":
            achados += verificar_html(conteudo, caminho, listas, modo_repositorio=m)
        elif sufixo == ".svg":
            achados += _verificar_html(
                conteudo, caminho, listas, {"script", "style"}, todos_atributos=True, modo_repositorio=m
            )
        elif rel == "search/search_index.json":
            achados += _verificar_indice_busca(conteudo, caminho, listas, m)
        else:
            achados += verificar_texto(conteudo, caminho, listas, modo_repositorio=m)
    return achados


def imprimir(achados: list[Achado], completo: bool) -> None:
    impressos: set[str] = set()
    for a in achados:
        saida = f"{a.caminho}:{a.linha} {a.categoria}"
        if completo:
            saida += f" {a.trecho}"
        if saida not in impressos:
            impressos.add(saida)
            print(saida)


def _fonte_padrao() -> Path | None:
    """BDESK_FONTE ou a primeira linha de sincronizacao/privado/fonte.txt (fora do git)."""
    ambiente = os.environ.get("BDESK_FONTE", "").strip()
    if ambiente:
        return Path(ambiente)
    arquivo = RAIZ / "sincronizacao" / "privado" / "fonte.txt"
    if arquivo.is_file():
        linhas = arquivo.read_text(encoding="utf-8").splitlines()
        if linhas and linhas[0].strip():
            return Path(linhas[0].strip())
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m sincronizacao.vazamento",
        description="Procura referências a código interno em docs/ ou site/.",
    )
    parser.add_argument("--completo", action="store_true", help="usa as listas privadas e mostra o trecho")
    parser.add_argument("--fonte", type=Path, default=None, help="raiz do repositório da fonte (modo completo)")
    parser.add_argument(
        "--repositorio",
        action="store_true",
        help="arquivos do repositório que não vão para o site: sem lista de permissões",
    )
    parser.add_argument("pasta", type=Path)
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    if not args.pasta.is_dir():
        print(f"Pasta não encontrada: {args.pasta}", file=sys.stderr)
        return 2
    if args.completo:
        try:
            listas = listas_completas(RAIZ, args.fonte or _fonte_padrao(), estrito=True)
        except ModoCompletoIncompleto as erro:
            print(erro, file=sys.stderr)
            return 2
    else:
        listas = listas_genericas(RAIZ)
    achados = verificar_arvore(args.pasta, listas, modo_repositorio=args.repositorio)
    imprimir(achados, args.completo)
    return 1 if achados else 0


if __name__ == "__main__":
    sys.exit(main())
