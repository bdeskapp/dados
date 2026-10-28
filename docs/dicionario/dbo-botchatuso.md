---
gerado: sincronizacao
---

# dbo.BotChatUso

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [chatbot (assistente virtual)](../fora-de-escopo/chatbot.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUso` | INT | não | sim | não |
| `idPerfil` | VARCHAR(50) | não | não | não |
| `cdCentroCusto` | VARCHAR(50) | não | não | não |
| `idUsu` | INT | sim | não | não |
| `cdCanal` | VARCHAR(20) | não | não | não |
| `dsModelo` | VARCHAR(100) | não | não | não |
| `nPromptTokens` | INT | não | não | não |
| `nCompletionTokens` | INT | não | não | não |
| `nTotalTokens` | INT | não | não | não |
| `nChamadasModelo` | INT | não | não | não |
| `nCustoUsd` | DECIMAL(18,10) | sim | não | não |
| `nTokensCache` | INT | sim | não | não |
| `nChamadasSemUso` | INT | sim | não | não |
| `dtCreate` | DATETIME | não | não | não |
