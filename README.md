# Bdesk: Dados

Documentação do banco de dados do Bdesk para engenheiros de dados de clientes. Este repositório contém o site publicado em [bdeskapp.github.io/dados](https://bdeskapp.github.io/dados).

O conteúdo é descritivo: tabelas, colunas, views e SQL para o leitor executar. Nada aqui cita código-fonte do produto (veja a regra de conteúdo abaixo).

## Conteúdo do site

- **Comece aqui** e **Consumo**: páginas próprias deste repositório.
- **Mapa**, **Fatos**, **Dimensões**, **Receitas**, **Views** e **Fora de escopo**: páginas espelhadas da fonte.
- **Dicionário**, **Sobre**, **Domínios do produto** e **Limitações conhecidas**: páginas geradas.
- **Glossário** e **busca**: páginas espelhadas da fonte.

## Três camadas em `docs/`

Nem toda página de `docs/` é editada aqui. Cada camada tem uma origem diferente:

- **Própria (editável aqui):** `docs/index.md`, `docs/comece-aqui/` e `docs/consumo/`.
- **Espelhada (não editar aqui):** `docs/mapa/`, `docs/fatos/`, `docs/dimensoes/`, `docs/receitas/`, `docs/views/`, `docs/fora-de-escopo/`, `docs/glossario-tela-banco.md` e `docs/busca.md`. São alteradas na fonte e copiadas pela sincronização.
- **Gerada (não editar aqui):** `docs/dicionario/`, `docs/sobre/`, `docs/dominios-do-produto.md` e `docs/limitacoes-conhecidas.md`. São produzidas pela sincronização.

As páginas espelhadas e geradas trazem no front matter a linha `gerado: sincronizacao`. **Não edite essas páginas aqui.** Alterações feitas nelas são sobrescritas na próxima sincronização. Para mudar o conteúdo, altere a fonte e sincronize de novo.

A lista completa das saídas geradas está em `SAIDAS_GERADAS` em `sincronizacao/config.py`.

## A configuração do site é gerada

`mkdocs.yml` não se edita à mão. Ele é montado a partir de `sincronizacao/mkdocs.modelo.yml`, cuja linha `# {{NAV_GERADO}}` recebe o `nav` gerado pela sincronização. Para mudar a configuração do site (tema, extensões, ajustes gerais), edite o modelo.

## Desenvolvimento local

Requisitos: Python 3.12 ou superior, no Windows.

```powershell
# Criar o ambiente virtual e instalar as dependências de desenvolvimento
python -m venv .venv
.venv\Scripts\pip install -r requirements-dev.txt

# Ativar a verificação de conteúdo antes de cada commit
git config core.hooksPath .githooks
```

### Sincronização

```powershell
# Sincronização normal: lê a fonte e atualiza docs/ e mkdocs.yml
.venv\Scripts\python -m sincronizacao --fonte <repo bdesk> --versao-produto 8.0.3

# Modo dev: gera numa pasta à parte e nunca toca docs/
.venv\Scripts\python -m sincronizacao --fonte <repo bdesk> --versao-produto 8.0.3 --saida-dev <pasta>
```

`<repo bdesk>` é o caminho local do repositório do produto. Use o caminho real da sua máquina, sem colocá-lo em nenhum arquivo versionado. A fonte é `<repo bdesk>/Database/docs`.

### Testes, build e site

```powershell
# Testes
.venv\Scripts\pytest -q

# Build estrito (o mesmo do CI; falha em avisos)
mkdocs build --strict

# Servidor local com recarregamento automático
mkdocs serve
```

### Verificação de vazamento

```powershell
# Verificação genérica sobre docs/
.venv\Scripts\python -m sincronizacao.vazamento docs

# Verificação completa, com as listas privadas
.venv\Scripts\python -m sincronizacao.vazamento --completo docs

# Arquivos da raiz que não vão para o site (README.md, CLAUDE.md)
.venv\Scripts\python -m sincronizacao.vazamento --repositorio .
```

O modo `--repositorio` é usado para os arquivos da raiz. Ele aceita comandos, caminhos e nomes de arquivo deste repositório, e só barra referências ao código do sistema de origem (extensões de arquivo de código do sistema de origem, referências de linha no formato arquivo:linha e nomes de rotinas) e os bloqueios privados. O hook de pre-commit usa esse modo.

## Regra de conteúdo

A regra abaixo vale para **todo** o conteúdo publicado e para tudo o que é commitado no repositório público. Ela vem da spec §4.1 (`planejamento/specs/2026-10-28-bdesk-dados-design.md`):

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
> - **Rotinas:** nomes de stored procedures e functions estão proibidos mesmo sem o corpo. *(Interpretação minha.)*

## Pasta privada `sincronizacao/privado/`

Esta pasta fica **fora do git** (está no `.gitignore`) e contém:

- `exclusoes.json`: as listas de exclusões do dicionário;
- `bloqueio.json`: os padrões de bloqueio da verificação de vazamento;
- `ajustes.json`: os ajustes por página;
- `fonte.txt`: o caminho da fonte (ou use a variável de ambiente `BDESK_FONTE`).

**Faça backup dessa pasta.** Ela não está no git, então não há como recuperá-la pelo repositório.

Sem a pasta privada, só roda a verificação genérica, e a sincronização normal **falha de propósito**. Assim, nada é publicado sem os filtros privados.

## Fonte e branches

- **Fonte:** `<repo bdesk>/Database/docs`, publicada só a partir de commits em `origin/development`, e só com a régua da fonte em `APROVADA`.
- As mudanças na fonte são feitas na branch `8005-database-melhorias-correcoes` e integradas depois.

## Integração contínua e publicação

O workflow `.github/workflows/deploy-docs.yml` roda a cada push em `main`:

1. verificação genérica de vazamento sobre `docs`;
2. `mkdocs build --strict`;
3. verificação de vazamento sobre o site gerado (`site`);
4. publicação no GitHub Pages.

## Restauração após falha

A sincronização troca `docs/` por um backup. Se a troca falhar e a restauração também, o backup fica em `.sync-backup-<data>` na raiz do repositório. Se sobrar `.sync-tmp/antigo`, recupere-o antes de sincronizar de novo: a sincronização recusa rodar enquanto esse backup pendente existir.

## Estrutura do repositório

```text
mkdocs.yml                    # Gerado a partir de sincronizacao/mkdocs.modelo.yml
requirements.txt              # Dependências de publicação
requirements-dev.txt          # Dependências de desenvolvimento (inclui as de publicação)
docs/
  index.md                    # Página inicial (própria)
  comece-aqui/                # Própria
  consumo/                    # Própria
  mapa/                       # Espelhada
  fatos/                      # Espelhada
  dimensoes/                  # Espelhada
  receitas/                   # Espelhada
  views/                      # Espelhada
  fora-de-escopo/             # Espelhada
  glossario-tela-banco.md     # Espelhada
  busca.md                    # Espelhada
  dicionario/                 # Gerada
  sobre/                      # Gerada
  dominios-do-produto.md      # Gerada
  limitacoes-conhecidas.md    # Gerada
overrides/                    # Ajustes do tema MkDocs Material
sincronizacao/
  __main__.py                 # Ponto de entrada da sincronização
  config.py                   # Pastas e lista de saídas geradas
  mkdocs.modelo.yml           # Modelo do mkdocs.yml (editável)
  vazamento.py                # Verificação de vazamento
  privado/                    # Fora do git (veja acima)
tests/                        # Testes (pytest)
.githooks/pre-commit          # Verificação do conteúdo staged
.github/workflows/deploy-docs.yml
```
