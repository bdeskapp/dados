"""Sincronização: gera docs/ do site a partir da fonte, com troca atômica e verificação de vazamento.

Uso: python -m sincronizacao --fonte <repo bdesk> --versao-produto 8.0.3 [--saida-dev <pasta>]
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import shutil
import sys
from pathlib import Path

import yaml

from . import config, derivadas, dicionario, links, privado, transformar, vazamento
from .fonte import Pagina, carregar_fonte, ler_pagina
from .portao import PortaoRecusado, avaliar
from .transformar import AjusteOrfao
from .vazamento import ModoCompletoIncompleto

# nomes usados diretamente (e substituíveis em testes) neste módulo
gerar_dicionario = dicionario.gerar_dicionario
escrever_esquema_publicado = dicionario.escrever_esquema_publicado

_H1 = re.compile(r"^# (.+?)\s*$", re.MULTILINE)
_FRONT = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n?", re.DOTALL)
_FRONT_ESPELHADA = "---\ngerado: sincronizacao\n---\n"


class FalhaVazamento(Exception):
    """Há achados de vazamento; a mensagem traz só a contagem."""


def _h1(texto: str, padrao: str) -> str:
    m = _H1.search(_FRONT.sub("", texto, count=1))
    return m.group(1).strip() if m else padrao


def _paginas_espelhadas(fonte, politica) -> dict[str, str]:
    """Caminho na fonte -> destino em docs/, só do que vai ser publicado."""
    destinos: dict[str, str] = {}
    for caminho in fonte.paginas:
        if caminho in config.NAO_PUBLICADOS:
            continue
        if caminho in config.ARQUIVOS_ESPELHADOS:
            destinos[caminho] = config.ARQUIVOS_ESPELHADOS[caminho]
        elif "/" in caminho and caminho.split("/", 1)[0] in config.PASTAS_ESPELHADAS:
            if caminho.startswith("receitas/") and caminho.rsplit("/", 1)[-1].removesuffix(".md") in politica.receitas_barradas:
                continue
            destinos[caminho] = caminho
    return destinos


def _ajustes(raiz_site: Path) -> dict:
    arq = raiz_site / "sincronizacao" / "privado" / "ajustes.json"
    return json.loads(arq.read_text(encoding="utf-8")) if arq.is_file() else {}


def _paginas_proprias(docs: Path) -> dict[str, str]:
    saidas = tuple(config.SAIDAS_GERADAS)
    proprias: dict[str, str] = {}
    if not docs.is_dir():
        return proprias
    for arq in sorted(docs.rglob("*.md")):
        rel = arq.relative_to(docs).as_posix()
        if rel in saidas or rel.startswith(tuple(s + "/" for s in saidas)):
            continue
        proprias[rel] = _h1(arq.read_text(encoding="utf-8"), rel)
    return proprias


def _escrever(caminho: Path, texto: str) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(texto, encoding="utf-8", newline="\n")


def _remover(caminho: Path) -> None:
    if caminho.is_dir():
        shutil.rmtree(caminho)
    else:
        caminho.unlink(missing_ok=True)


def _trocar(tmp_docs: Path, raiz_site: Path, backup: Path) -> None:
    """Troca atômica das saídas geradas, de mkdocs.yml e dos dois JSON de sincronizacao/.

    Os antigos vão para `backup`, os novos entram com os.replace. Qualquer falha restaura tudo.
    Se a restauração também falhar, o backup é preservado em raiz_site/.sync-backup-<data>.
    """
    docs = raiz_site / "docs"
    tmp = tmp_docs.parent
    plano = [(tmp_docs / n, docs / n, backup / "docs" / n) for n in config.SAIDAS_GERADAS]
    plano.append((tmp / "mkdocs.yml", raiz_site / "mkdocs.yml", backup / "mkdocs.yml"))
    for nome in ("esquema-publicado.json", "dominios-publicados.json"):
        plano.append((tmp / nome, raiz_site / "sincronizacao" / nome, backup / "sincronizacao" / nome))
    movidos: list[tuple[Path, Path]] = []
    colocados: list[tuple[Path, Path]] = []
    try:
        docs.mkdir(parents=True, exist_ok=True)
        for _novo, destino, copia in plano:
            if destino.exists():
                copia.parent.mkdir(parents=True, exist_ok=True)
                os.replace(destino, copia)
                movidos.append((destino, copia))
        for novo, destino, _copia in plano:
            if novo.exists():
                destino.parent.mkdir(parents=True, exist_ok=True)
                os.replace(novo, destino)
                colocados.append((destino, novo))
    except BaseException as erro:
        try:
            for destino, novo in reversed(colocados):
                os.replace(destino, novo)
            for destino, copia in reversed(movidos):
                if destino.exists():  # evita aninhar a cópia dentro de um resto da troca
                    _remover(destino)
                os.replace(copia, destino)
        except BaseException:
            erro.restauracao_falhou = True
            carimbo = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            preservado = raiz_site / f".sync-backup-{carimbo}"
            try:
                os.rename(backup, preservado)
            except OSError:
                preservado = backup
            print(f"Restauração falhou; backup preservado em {preservado}", file=sys.stderr)
        raise


def _validar_saida_dev(raiz_site: Path, saida_dev: Path | None) -> None:
    if saida_dev is None:
        return
    alvo = Path(saida_dev).resolve()
    for proibida in (raiz_site / "docs", raiz_site / ".sync-tmp"):
        proibida = proibida.resolve()
        if alvo == proibida or proibida in alvo.parents:
            raise ValueError("saida_dev não pode ficar dentro de docs/ nem de .sync-tmp/")


def sincronizar(
    raiz_fonte: Path,
    raiz_site: Path,
    versao_produto: str,
    *,
    saida_dev: Path | None = None,
    hoje: str | None = None,
) -> dict:
    """Devolve {"commit", "contagens", "achados", ...}. Levanta PortaoRecusado, AjusteOrfao,
    ModoCompletoIncompleto, ValueError ou FalhaVazamento; nesses casos docs/ fica intacto."""
    raiz_fonte, raiz_site = Path(raiz_fonte), Path(raiz_site)
    _validar_saida_dev(raiz_site, saida_dev)
    tmp = raiz_site / ".sync-tmp"
    if (tmp / "antigo").exists():
        raise RuntimeError("backup pendente em .sync-tmp/antigo: recupere-o antes de sincronizar")
    preservar = False
    try:
        if tmp.exists():
            shutil.rmtree(tmp)
        return _gerar(raiz_fonte, raiz_site, versao_produto, tmp, saida_dev, hoje)
    except BaseException as erro:
        preservar = getattr(erro, "restauracao_falhou", False)
        raise
    finally:
        if not preservar:
            shutil.rmtree(tmp, ignore_errors=True)


def _carregar_fonte(raiz_fonte: Path):
    try:
        return carregar_fonte(raiz_fonte)
    except yaml.YAMLError:
        docs = raiz_fonte / config.CAMINHO_DOCS_FONTE
        ruins = []
        for arq in sorted(docs.rglob("*.md")):
            rel = arq.relative_to(docs).as_posix()
            try:
                ler_pagina(arq.read_text(encoding="utf-8"), rel)
            except yaml.YAMLError:
                ruins.append(rel)
        raise ValueError("front matter inválido em: " + ", ".join(ruins or ["(página não identificada)"])) from None


def _gerar(raiz_fonte: Path, raiz_site: Path, versao_produto: str, tmp: Path, saida_dev, hoje) -> dict:
    dev = saida_dev is not None
    fonte = _carregar_fonte(raiz_fonte)
    politica = avaliar(fonte, modo_dev=dev)
    exclusoes = privado.carregar_exclusoes(raiz_site / "sincronizacao" / "privado")
    ajustes = _ajustes(raiz_site)
    docs_site = raiz_site / "docs"
    tmp_docs = tmp / "docs"
    tmp_docs.mkdir(parents=True)

    destinos = _paginas_espelhadas(fonte, politica)
    pend = fonte.paginas.get("pendencias-abertas.md") or Pagina("pendencias-abertas.md", {}, "")
    limitacoes_md, abertas, decididas = derivadas.gerar_limitacoes(pend)

    proprias = _paginas_proprias(docs_site)
    titulos: dict[str, str] = {}  # destino -> título sem prefixo
    textos: dict[str, str] = {}
    for caminho, destino in destinos.items():
        texto = transformar.transformar_pagina(fonte.paginas[caminho], politica, ajustes)
        textos[caminho] = texto
        titulos[destino] = derivadas.titulo_nav(_h1(texto, destino))

    # dicionário e esquema novo
    esquema_novo = tmp / "esquema-publicado.json"
    dominios_novo = tmp / "dominios-publicados.json"
    para_dicionario = {c: titulos[d] for c, d in destinos.items() if c == d}
    contagens = gerar_dicionario(fonte, exclusoes, tmp_docs, publicadas=para_dicionario)
    escrever_esquema_publicado(fonte, exclusoes, esquema_novo)
    dominios_md = transformar.trocar_decisoes(transformar.remover_provas(fonte.dominios_md))
    _escrever(
        dominios_novo,
        json.dumps(derivadas.chaves_dominios(dominios_md), ensure_ascii=False, indent=2) + "\n",
    )

    # derivadas
    _escrever(tmp_docs / "dominios-do-produto.md", derivadas.gerar_dominios(dominios_md))
    _escrever(tmp_docs / "limitacoes-conhecidas.md", limitacoes_md)
    titulos_receitas = {r: titulos.get(f"receitas/{r}.md", r) for r in politica.receitas_em_revisao}
    data = hoje or datetime.date.today().isoformat()
    _escrever(
        tmp_docs / "sobre" / "versao.md",
        derivadas.gerar_versao(politica, versao_produto, data, contagens, titulos_receitas),
    )

    geradas = {
        arq.relative_to(tmp_docs).as_posix(): _h1(arq.read_text(encoding="utf-8"), arq.name)
        for arq in sorted(tmp_docs.rglob("*.md"))
    }
    contexto = links.ContextoLinks(
        publicadas=set(titulos) | set(geradas) | set(proprias),
        barradas={f"receitas/{r}.md" for r in politica.receitas_barradas},
        pendencias_abertas=abertas,
        pendencias_decididas=decididas,
    )

    # espelhadas: transformar -> âncoras -> links
    for caminho, destino in destinos.items():
        texto = links.injetar_ancoras(textos[caminho])
        texto = links.reescrever_links(texto, destino, contexto)
        _escrever(tmp_docs / destino, _FRONT_ESPELHADA + texto.lstrip("\n"))

    # mkdocs.yml
    nav = derivadas.gerar_nav({**proprias, **geradas, **titulos})
    modelo = (raiz_site / "sincronizacao" / "mkdocs.modelo.yml").read_text(encoding="utf-8")
    _escrever(tmp / "mkdocs.yml", derivadas.aplicar_nav(modelo, nav))

    # verificação de vazamento, contra o esquema e os domínios recém-gerados
    extra = {"esquema_publicado": esquema_novo, "dominios_publicados": dominios_novo}
    if dev:
        listas = vazamento.listas_completas(raiz_site, raiz_fonte, **extra)
    else:
        listas = vazamento.listas_completas(raiz_site, raiz_fonte, estrito=True, **extra)
    achados = vazamento.verificar_arvore(tmp_docs, listas)
    por_categoria: dict[str, int] = {}
    for a in achados:
        por_categoria[a.categoria] = por_categoria.get(a.categoria, 0) + 1
    resultado = {
        "commit": politica.commit,
        "contagens": contagens,
        "achados": len(achados),
        "achados_por_categoria": por_categoria,
        "paginas": sum(1 for _ in tmp_docs.rglob("*.md")),
    }

    if dev:
        vazamento.imprimir(achados, completo=False)
        saida_dev = Path(saida_dev)
        saida_dev.mkdir(parents=True, exist_ok=True)
        shutil.copytree(tmp_docs, saida_dev, dirs_exist_ok=True)
        return resultado
    if achados:
        vazamento.imprimir(achados, completo=False)
        raise FalhaVazamento(f"{len(achados)} achado(s) de vazamento; a troca não foi feita.")

    _trocar(tmp_docs, raiz_site, tmp / "antigo")
    return resultado


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m sincronizacao", description=__doc__)
    parser.add_argument("--fonte", type=Path, required=True, help="raiz do repositório do Bdesk")
    parser.add_argument("--versao-produto", required=True)
    parser.add_argument("--raiz-site", type=Path, default=None, help=argparse.SUPPRESS)
    parser.add_argument("--saida-dev", type=Path, default=None, help="gera só nesta pasta, sem tocar docs/")
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    raiz_site = args.raiz_site or Path(__file__).resolve().parent.parent
    try:
        r = sincronizar(args.fonte, raiz_site, args.versao_produto, saida_dev=args.saida_dev)
    except (PortaoRecusado, AjusteOrfao, FalhaVazamento, ModoCompletoIncompleto, ValueError, RuntimeError) as erro:
        print(f"{type(erro).__name__}: {erro}", file=sys.stderr)
        return 1
    print(f"Páginas geradas: {r['paginas']}; achados de vazamento: {r['achados']} {r['achados_por_categoria']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
