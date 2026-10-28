---
gerado: sincronizacao
---
# Fora de escopo: motor de relatórios


**O que é.** Os relatórios customizados do produto, com seus gráficos, perfis de acesso e agendamento de envio. Esta documentação do banco não detalha o motor; ela cobre as tabelas de requisição que os relatórios leem.

## Tabelas principais

| Tabela | Papel |
|---|---|
| `RelCust`, `RelCustPerfil`, `RelCustRelac` | relatório customizado, perfis que o enxergam e relatórios relacionados |
| `Grafico` | tipo de gráfico (`cdGrafico`), referenciado por `ObjectQuery.cdChart` |
| `ObjectQuery`, `ObjectQueryParam` | consulta de objeto com parâmetros (`cmdQuery`, `nmParam`, `dsLabel`) |
| `ScheduledReport`, `ScheduledReportSubscriber` | relatório agendado e seus assinantes por e-mail; o envio agendado de relatórios está descontinuado (decisão do produto) |


## Onde toca a requisição

- Nenhuma tabela do motor tem FK para `Req` ou `ReqConcluida`.
- O banco não registra a ligação entre um relatório e a requisição em coluna de chave. Para as perguntas de negócio desta documentação, comece pelo [índice](../busca.md), que leva às receitas e às views recomendadas.

## Veja também

[Requisição](../fatos/requisicao.md) · [Abertas e encerradas](../mapa/abertas-e-encerradas.md) · [Índice](../busca.md)
