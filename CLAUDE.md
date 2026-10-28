# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Documentation site for the Bdesk database, aimed at customer data engineers. Published to GitHub Pages at `https://bdeskapp.github.io/dados`. The site is built with MkDocs Material, and its content is written in **Brazilian Portuguese (pt-BR)**.

Most of `docs/` is not hand-written here. A synchronization step (`sincronizacao/`) reads the product documentation source and generates or copies pages into the site. Read the three-layer section before editing anything under `docs/`.

## Three Layers in `docs/`

- **Own (editable here):** `docs/index.md`, `docs/comece-aqui/`, `docs/consumo/`.
- **Mirrored (never edit here; changed at the source):** `docs/mapa/`, `docs/fatos/`, `docs/dimensoes/`, `docs/receitas/`, `docs/views/`, `docs/fora-de-escopo/`, `docs/glossario-tela-banco.md`, `docs/busca.md`.
- **Generated (never edit here):** `docs/dicionario/`, `docs/sobre/`, `docs/dominios-do-produto.md`, `docs/limitacoes-conhecidas.md`.

Mirrored and generated pages carry the front matter `gerado: sincronizacao`. The full list of generated outputs is `SAIDAS_GERADAS` in `sincronizacao/config.py`. Any edit to a mirrored or generated page is overwritten by the next synchronization. Fix the content at the source and synchronize again.

`mkdocs.yml` is also generated. Edit `sincronizacao/mkdocs.modelo.yml` instead; its line `# {{NAV_GERADO}}` receives the generated `nav`.

## Commands (Windows)

```powershell
# Setup
python -m venv .venv
.venv\Scripts\pip install -r requirements-dev.txt

# Tests
.venv\Scripts\pytest -q

# Synchronize (normal mode; rewrites docs/ and mkdocs.yml)
.venv\Scripts\python -m sincronizacao --fonte <repo bdesk> --versao-produto 8.0.3

# Dev mode: generates into a separate folder and never touches docs/
.venv\Scripts\python -m sincronizacao --fonte <repo bdesk> --versao-produto 8.0.3 --saida-dev <pasta>

# Strict build (same as CI; fails on warnings)
.venv\Scripts\python -m mkdocs build --strict

# Local server with live reload
.venv\Scripts\python -m mkdocs serve

# Leak check
.venv\Scripts\python -m sincronizacao.vazamento docs
.venv\Scripts\python -m sincronizacao.vazamento --completo docs

# Leak check for root files that do not go to the site (README.md, CLAUDE.md)
.venv\Scripts\python -m sincronizacao.vazamento --repositorio .

# Activate the pre-commit hook (checks staged content)
git config core.hooksPath .githooks
```

`--repositorio` accepts commands, paths and file names from this repository. It only blocks references to the source system's code (source-code file extensions of the source system, file:line references, and routine names) and the private blocklists. The pre-commit hook uses this mode for root files.

`<repo bdesk>` is a placeholder for the local path of the product repository. Never write a real path into a tracked file. The source is `<repo bdesk>/Database/docs`.

## Content Rule (spec §4.1)

Copied from `planejamento/specs/2026-10-28-bdesk-dados-design.md`, section 4.1. It applies to **all** published content and everything committed to this public repository:

> ### 4.1 Nenhuma referência ao código-fonte (decisão do usuário)
> Vale para **todo** o conteúdo publicado e para tudo o que é commitado no repositório público.
> - **Proibido:**
>   - caminhos e nomes de arquivos (código das aplicações, HTML de telas, scripts de banco, scripts de atualização de versão);
>   - números de linha;
>   - nomes de classes, métodos e funções;
>   - nomes de stored procedures, functions e triggers;
>   - trechos de código do sistema;
>   - nomes de camadas e tecnologias internas usados como referência de onde algo acontece. Exemplo: "a camada de telas antigas grava…" vira "o sistema grava…".
> - **Sempre** linguagem descritiva.
> - **Permitido:**
>   - nomes de tabelas, colunas e views, que formam o contrato de dados;
>   - SQL escrito para o leitor executar, como as receitas;
>   - exemplos fictícios.
> - **Views:** o nome pode aparecer, a definição não. A prosa também não descreve a lógica interna da view. Ela descreve o que a view devolve e como usá-la.
> - **Rotinas:** nomes de stored procedures e functions estão proibidos mesmo sem o corpo.

Do not write customer names, routine names, or code file names in any tracked file. Path examples must be synthetic (`<repo bdesk>`).

## Private Folder: `sincronizacao/privado/`

- Outside git (`.gitignore`). It contains only these files, and their contents must never appear in a tracked file:
  - `exclusoes.json`: dictionary exclusion lists;
  - `bloqueio.json`: leak-blocking patterns;
  - `ajustes.json`: per-page adjustments;
  - `fonte.txt`: the source path (or use the `BDESK_FONTE` environment variable).
- Never put examples of its contents in any tracked file, including this one.
- Back it up. It is not recoverable from git.
- Without it, only the generic leak check runs, and the normal synchronization fails on purpose.

## Source and Branches

- Source: `<repo bdesk>/Database/docs`, published only from commits on `origin/development`, and only when the source's quality gate (régua) verdict is `APROVADA`.
- Source changes are made on branch `8005-database-melhorias-correcoes` and integrated afterwards.
- `--fonte` must point to a clean checkout whose HEAD is contained in `origin/development` (the gate checks it); the main product checkout may be on an unrelated branch. Use remote `origin`; the `bitbucket` remote is stale.
- The régua report must be committed in the same commit as the last `Database/docs` change: its `commit` field points to the parent, so freshness is checked by file history.
- Source authoring rules (proof convention, `--rehash` after rewriting a rule) are in `<repo bdesk>/Database/docs/_manutencao/como-atualizar.md`. The source verifier and régua `--so` globs are relative to the repo root (`Database/docs/fatos/*.md`); a wrong glob silently selects nothing.

## Public History

- `main` on GitHub starts from a single clean commit. The local branch `historico-local` holds the development history and must never be pushed (an old commit there fails the full leak check).

## CI

`.github/workflows/deploy-docs.yml` runs on push to `main`:

1. generic leak check on `docs`;
2. `mkdocs build --strict`;
3. leak check on the built `site`;
4. deploy to GitHub Pages.

## Recovery

- The synchronization swaps `docs/` with a backup. If the swap fails and the restore also fails, the backup stays in `.sync-backup-<data>` at the repository root.
- If `.sync-tmp/antigo` is left behind, recover it before synchronizing again. The synchronization refuses to run while that pending backup exists.

## Repository Layout

```text
mkdocs.yml                        # Generated from sincronizacao/mkdocs.modelo.yml
requirements.txt                  # Publishing dependencies
requirements-dev.txt              # Development dependencies (includes requirements.txt)
docs/
  index.md                        # Own
  comece-aqui/                    # Own
  consumo/                        # Own
  mapa/  fatos/  dimensoes/       # Mirrored (do not edit)
  receitas/  views/
  fora-de-escopo/
  glossario-tela-banco.md
  busca.md
  dicionario/  sobre/             # Generated (do not edit)
  dominios-do-produto.md
  limitacoes-conhecidas.md
overrides/                        # MkDocs Material theme overrides
sincronizacao/
  __main__.py                     # Synchronization entry point
  config.py                       # Folder constants and SAIDAS_GERADAS
  mkdocs.modelo.yml               # Editable mkdocs.yml template
  vazamento.py                    # Leak check
  privado/                        # Outside git (see above)
tests/                            # pytest suite
.githooks/pre-commit              # Staged-content leak check
.github/workflows/deploy-docs.yml
```

## Gotchas

- `mkdocs.yml` and the mirrored/generated pages are overwritten by synchronization. Editing them by hand is lost work.
- `mkdocs build --strict` fails on warnings. The site only builds against a real synchronized `docs/`; the tests use a minimal project.
- In generic mode the leak check reports only `path:line category`, never the matched text. Use `--completo` locally to see private matches.
- `vazamento docs` before the first synchronization flags every table and column: the allowlist comes from `sincronizacao/esquema-publicado.json`, which the sync writes.
- Excluded credential columns must not be named anywhere on the site, not even in prose saying they are excluded. Fix wording at the source or with an entry in `privado/ajustes.json` (avoids reopening the source approval).
- The full check (hook) blocks the source's internal technology names even in README/CLAUDE quotes; describe the category instead of naming it.
- Published decisions: the content of the source's decision marker (an HTML comment named `decisao`) becomes "decisão do produto". Keep parentheses outside the marker so it reads "(decisão do produto)".
- Git converts line endings on this machine; `.gitattributes` forces LF because tests compare exact text.
- Spec, plans and the execution progress file live in `planejamento/` (gitignored, local only).
