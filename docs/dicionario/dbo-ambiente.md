---
gerado: sincronizacao
---

# dbo.Ambiente

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `Id` | BIGINT | não | sim | não |
| `Nome` | NVARCHAR(255) | não | não | não |
| `StringConexao` | NVARCHAR(500) | não | não | não |
| `PastaImagens` | NVARCHAR(255) | não | não | não |
| `PastaImportacoes` | NVARCHAR(255) | não | não | não |
| `UrlImagens` | NVARCHAR(255) | sim | não | não |
| `UrlAsk` | NVARCHAR(255) | sim | não | não |
| `UrlChat` | NVARCHAR(255) | sim | não | não |
| `PastaAnexos` | NVARCHAR(255) | sim | não | não |
| `UrlAnexos` | NVARCHAR(255) | sim | não | não |
| `Ativo` | BIT | sim | não | não |
| `GruposAcessoAdmin` | NVARCHAR(255) | sim | não | não |
| `UrlAutenticacaoRemota` | NVARCHAR(255) | sim | não | não |
| `LoginNativo` | BIT | sim | não | não |
| `LoginWindows` | BIT | sim | não | não |
| `UrlAplicacaoLogin` | NVARCHAR(255) | sim | não | não |
| `StringConexaoAsk` | NVARCHAR(500) | sim | não | não |
| `UrlApiRestAsk` | NVARCHAR(500) | sim | não | não |
| `UrlDownloadAnexosAsk` | NVARCHAR(500) | sim | não | não |
| `ContatoEMail` | NVARCHAR(255) | sim | não | não |
| `ContatoTelefone` | NVARCHAR(255) | sim | não | não |
| `ParametrosAsk` | TEXT | sim | não | não |
