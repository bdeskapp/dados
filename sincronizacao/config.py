"""Constantes de pastas e caminhos da sincronização."""

PASTAS_ESPELHADAS = ("mapa", "fatos", "dimensoes", "receitas", "views", "fora-de-escopo")
ARQUIVOS_ESPELHADOS = {"glossario-tela-banco.md": "glossario-tela-banco.md", "INDEX.md": "busca.md"}
# pendencias-abertas.md não é publicado direto: vira as limitações conhecidas.
NAO_PUBLICADOS = ("receitas/_modelo-receita.md", "README.md", "pendencias-abertas.md")
SAIDAS_GERADAS = (
    "mapa", "fatos", "dimensoes", "receitas", "views", "fora-de-escopo",
    "dicionario", "sobre", "glossario-tela-banco.md", "busca.md",
    "dominios-do-produto.md", "limitacoes-conhecidas.md",
)
CAMINHO_DOCS_FONTE = "Database/docs"
CAMINHO_RELATORIO = "docs/plans/database-docs/regua/relatorio.json"
