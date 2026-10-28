"""Dicionário de tabelas e views: selos, exclusões e páginas."""
from __future__ import annotations

import json
import re
from pathlib import Path

from .fonte import Esquema, Fonte, Pagina
from .privado import Exclusoes

AVISO_SO_ESTRUTURA = (
    "O significado das colunas desta tabela não está documentado. "
    "Não deduza o significado pelo nome da coluna."
)
AVISO_CITADA_TABELA = (
    "Esta tabela é citada em receitas ou páginas de referência, "
    "mas não tem página de negócio própria."
)
NOTA_TIPOS_SEM_TAMANHO = (
    "Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento)."
)
_PASTAS_EXPLICADA = ("fatos/", "dimensoes/", "mapa/")
_PASTAS_CITADA = ("receitas/", "fora-de-escopo/", "views/")
_VIEWS_RECOMENDADAS = "views/views-recomendadas.md"
_CRASES = re.compile(r"`([^`\n]+)`")
_SELOS = ("explicada", "citada", "so_estrutura")
_ROTULO = {"explicada": "Explicada", "citada": "Citada", "so_estrutura": "Só estrutura"}
_PREFIXOS_TITULO = ("Fato: ", "Dimensão: ", "Receita: ", "Fora de escopo: ")
_FRONT = ["---", "gerado: sincronizacao", "---", ""]


def _canonico(nome: str) -> str:
    return nome if "." in nome else f"dbo.{nome}"


def _resolver(nome: str, esquema: Esquema) -> str | None:
    c = _canonico(nome)
    if c in esquema.tabelas or c in esquema.views:
        return c
    return None


def classificar_objetos(paginas: dict[str, Pagina], esquema: Esquema) -> dict[str, dict[str, set[str]]]:
    res = {n: {"explicada": set(), "citada": set()} for n in (*esquema.tabelas, *esquema.views)}
    for caminho, pag in paginas.items():
        for n, item in enumerate(pag.meta.get("tabelas") or [], start=1):
            obj = _resolver(str(item), esquema)
            if obj is None:
                raise ValueError(f"item nº {n} de `tabelas:` em {caminho} não é tabela nem view")
            if caminho.startswith(_PASTAS_EXPLICADA):
                res[obj]["explicada"].add(caminho)
            elif caminho.startswith(_PASTAS_CITADA):
                res[obj]["citada"].add(caminho)
    rec = paginas.get(_VIEWS_RECOMENDADAS)
    if rec is not None:
        for nome in _CRASES.findall(rec.corpo):
            obj = _resolver(nome.strip(), esquema)
            if obj is not None and obj in esquema.views:
                res[obj]["explicada"].add(_VIEWS_RECOMENDADAS)
    return res


def _selo(info: dict[str, set[str]]) -> str:
    if info["explicada"]:
        return "explicada"
    if info["citada"]:
        return "citada"
    return "so_estrutura"


def _resolver_exclusoes(fonte: Fonte, ex: Exclusoes) -> tuple[set[str], set[tuple[str, str]]]:
    """Devolve (objetos excluídos, colunas excluídas) com os nomes canônicos do esquema."""
    todas = {**fonte.esquema.tabelas, **fonte.esquema.views}
    objetos = {n.lower(): n for n in todas}
    objs: set[str] = set()
    for n, entrada in enumerate((*sorted(ex.tabelas), *sorted(ex.views)), start=1):
        alvo = objetos.get(_canonico(entrada.strip()).lower())
        if alvo is None:
            raise ValueError(f"exclusão nº {n} de tabelas/views de exclusoes.json sem correspondência")
        objs.add(alvo)
    cols: set[tuple[str, str]] = set()
    for n, entrada in enumerate(sorted(ex.colunas), start=1):
        obj, _, col = entrada.strip().rpartition(".")
        alvo = objetos.get(_canonico(obj).lower()) if obj else None
        nome_col = None
        if alvo is not None:
            nome_col = next((c["nome"] for c in todas[alvo] if c["nome"].lower() == col.lower()), None)
        if nome_col is None:
            raise ValueError(f"exclusão nº {n} de colunas de exclusoes.json sem correspondência")
        cols.add((alvo, nome_col))
    return objs, cols


def _publicados(fonte: Fonte, ex: Exclusoes) -> tuple[dict[str, list[dict]], dict[str, list[dict]]]:
    objs, cols = _resolver_exclusoes(fonte, ex)

    def filtra(origem: dict[str, list[dict]]) -> dict[str, list[dict]]:
        return {
            n: [c for c in cs if (n, c["nome"]) not in cols]
            for n, cs in origem.items()
            if n not in objs
        }

    return filtra(fonte.esquema.tabelas), filtra(fonte.esquema.views)


def escrever_esquema_publicado(fonte: Fonte, exclusoes: Exclusoes, caminho: Path) -> None:
    tabelas, views = _publicados(fonte, exclusoes)
    dados = {
        "tabelas": {n: [c["nome"] for c in cols] for n, cols in tabelas.items()},
        "views": {n: [c["nome"] for c in cols] for n, cols in views.items()},
    }
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _slug(nome: str) -> str:
    return nome.replace(".", "-").replace("_", "-").lower()


def _cel(txt) -> str:
    return str(txt).replace("|", "\\|")


def _sim(v) -> str:
    return "sim" if v else "não"


def _titulo(t: str) -> str:
    for pref in _PREFIXOS_TITULO:
        if t.startswith(pref):
            return t[len(pref):]
    return t


def _corpo_selo(selo: str, info: dict[str, set[str]], eh_view: bool, publicadas: dict[str, str] | None) -> list[str]:
    linhas = [f"**Selo:** {_ROTULO[selo]}", ""]
    if selo == "so_estrutura":
        linhas += ['!!! warning "Só estrutura"', f"    {AVISO_SO_ESTRUTURA}", ""]
    elif selo == "citada":
        aviso = AVISO_CITADA_TABELA.replace("Esta tabela", "Esta view") if eh_view else AVISO_CITADA_TABELA
        linhas += ['!!! info "Citada"', f"    {aviso}", ""]
    if publicadas is not None and selo != "so_estrutura":
        prefixo = "../../" if eh_view else "../"
        paginas = sorted(p for p in info[selo] if p in publicadas)
        if paginas:
            linhas += [f"{_ROTULO[selo]} em:", ""]
            linhas += [f"- [{_titulo(publicadas[p])}]({prefixo}{p})" for p in paginas]
            linhas.append("")
    return linhas


def _pagina_tabela(nome, cols, selo, info, fks, publicadas) -> str:
    out = _FRONT + [f"# {nome}", ""] + _corpo_selo(selo, info, False, publicadas)
    out += ["## Colunas", "", "| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |", "|---|---|---|---|---|"]
    for c in cols:
        out.append(
            f"| `{_cel(c['nome'])}` | {_cel(c['tipo'])} | {_sim(c.get('nulo'))} | "
            f"{_sim(c.get('pk'))} | {_sim(c.get('computada'))} |"
        )
    out.append("")
    if fks:
        out += ["## Chaves estrangeiras", ""] + fks + [""]
    return "\n".join(out)


def _pagina_view(nome, cols, selo, info, publicadas) -> str:
    out = _FRONT + [f"# {nome}", ""] + _corpo_selo(selo, info, True, publicadas)
    out += ["## Colunas", "", "| Coluna | Tipo |", "|---|---|"]
    for c in cols:
        out.append(f"| `{_cel(c['nome'])}` | {_cel(c['tipo'])} |")
    out += ["", '!!! note "Tipos sem tamanho"', f"    {NOTA_TIPOS_SEM_TAMANHO}", ""]
    return "\n".join(out)


def gerar_dicionario(
    fonte: Fonte,
    exclusoes: Exclusoes,
    destino: Path,
    esquema_publicado: Path | None = None,
    publicadas: dict[str, str] | None = None,
) -> dict:
    destino = Path(destino)
    tabelas, views = _publicados(fonte, exclusoes)
    classes = classificar_objetos(fonte.paginas, fonte.esquema)  # valida todos os itens de tabelas:
    if publicadas is not None:
        classes = classificar_objetos(
            {k: v for k, v in fonte.paginas.items() if k in publicadas}, fonte.esquema
        )
    colunas_ok = {n: {c["nome"] for c in cols} for n, cols in tabelas.items()}

    def fk_ok(lado: dict) -> bool:
        t = lado["tabela"]
        return t in colunas_ok and all(c in colunas_ok[t] for c in lado["colunas"])

    fks_pub = [f for f in fonte.esquema.fks if fk_ok(f["de"]) and fk_ok(f["para"])]
    for grupo in (tabelas, views):
        vistos: dict[str, str] = {}
        for nome in grupo:
            outro = vistos.setdefault(_slug(nome), nome)
            if outro != nome:
                raise ValueError(f"nomes de arquivo em colisão: {outro} e {nome}")
    pasta = destino / "dicionario"
    (pasta / "views").mkdir(parents=True, exist_ok=True)
    contagem_schema: dict[str, dict[str, int]] = {}

    def contar(nome: str, selo: str) -> None:
        schema = nome.split(".")[0]
        contagem_schema.setdefault(schema, {s: 0 for s in _SELOS})[selo] += 1

    for nome, cols in tabelas.items():
        selo = _selo(classes[nome])
        linhas = [
            f"- `{f['de']['tabela']}` ({', '.join(f['de']['colunas'])}) "
            f"→ `{f['para']['tabela']}` ({', '.join(f['para']['colunas'])})"
            for f in fks_pub
            if nome in (f["de"]["tabela"], f["para"]["tabela"])
        ]
        texto = _pagina_tabela(nome, cols, selo, classes[nome], linhas, publicadas)
        (pasta / f"{_slug(nome)}.md").write_text(texto, encoding="utf-8")
        contar(nome, selo)
    for nome, cols in views.items():
        selo = _selo(classes[nome])
        texto = _pagina_view(nome, cols, selo, classes[nome], publicadas)
        (pasta / "views" / f"{_slug(nome)}.md").write_text(texto, encoding="utf-8")
        contar(nome, selo)

    idx = _FRONT + ["# Dicionário de tabelas e views", ""]
    for schema in sorted(contagem_schema):
        c = contagem_schema[schema]
        idx += [
            f"## Schema {schema}",
            "",
            f"Explicadas: {c['explicada']} · Citadas: {c['citada']} · Só estrutura: {c['so_estrutura']}",
            "",
        ]
        itens = [
            (nome, f"- [{nome}]({_slug(nome)}.md) ({_ROTULO[_selo(classes[nome])]})") for nome in tabelas
        ] + [
            (nome, f"- [{nome}](views/{_slug(nome)}.md) (view, {_ROTULO[_selo(classes[nome])]})")
            for nome in views
        ]
        idx += [lin for n, lin in sorted(itens, key=lambda x: x[0].lower()) if n.split(".")[0] == schema]
        idx.append("")
    (pasta / "index.md").write_text("\n".join(idx), encoding="utf-8")

    if esquema_publicado is not None:
        escrever_esquema_publicado(fonte, exclusoes, esquema_publicado)
    return {
        "tabelas": len(tabelas),
        "colunas": sum(len(c) for c in tabelas.values()),
        "views": len(views),
        "fks": len(fks_pub),
    }
