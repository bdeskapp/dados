---
gerado: sincronizacao
---

# dbo.EnvioEmail

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [e-mail](../fora-de-escopo/email.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idEnvioEmail` | INT | não | não | não |
| `NomeRemetente` | VARCHAR(100) | sim | não | não |
| `EmailRemetente` | VARCHAR(100) | sim | não | não |
| `EmailDestinatario` | VARCHAR(MAX) | sim | não | não |
| `EmHTML` | TINYINT | sim | não | não |
| `nTentativas` | INT | sim | não | não |
| `dsUltimoErro` | VARCHAR(MAX) | sim | não | não |
| `dtDataCriacao` | DATETIME | não | não | não |
| `dtDataUltimaTentativa` | DATETIME | sim | não | não |
| `dtEnvio` | DATETIME | sim | não | não |
| `Assunto` | VARCHAR(MAX) | sim | não | não |
| `Mensagem` | VARCHAR(MAX) | sim | não | não |
| `Anexos` | VARCHAR(MAX) | sim | não | não |
