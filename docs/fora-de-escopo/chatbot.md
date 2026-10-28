---
gerado: sincronizacao
---
# Fora de escopo: chatbot (assistente virtual)


**O que é.** O assistente virtual do portal e o bot de Teams e WhatsApp, que conversam com o usuário, buscam serviços e abrem requisições pela API. Esta documentação do banco não detalha o domínio.

## Tabelas principais

| Tabela | Papel |
|---|---|
| `BotChatUso` | uma linha por uso de modelo de IA: `idUsu`, `idPerfil`, `cdCanal`, `dsModelo`, tokens (`nPromptTokens`, `nCompletionTokens`, `nTotalTokens`), `nCustoUsd`, `dtCreate` |

A configuração do bot fica no parâmetro avançado (tabela `ParametroAvancado`).


## Onde toca a requisição

- `BotChatUso` não tem coluna de requisição e não tem FK.
- A abertura pelo bot usa a rota de abertura de requisição da API; a requisição criada é uma linha de `Req`, tratada em [requisição](../fatos/requisicao.md).

## Veja também

[Requisição](../fatos/requisicao.md) · [Canal de origem](../dimensoes/canal-origem.md) · [Índice](../busca.md)
