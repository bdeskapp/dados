# Regras de ouro

Estas são as regras que mais evitam número errado. Cada uma resume uma regra `R-…`; o link leva à explicação completa e à receita que a aplica. A lista de todas as regras está em [regras essenciais](../mapa/regras-essenciais.md) e em [regras essenciais das dimensões](../mapa/regras-essenciais-dimensoes.md).

## Volume e estado

1. **Some abertas e encerradas.** Qualquer volume ou tempo histórico junta a tabela das abertas e a das encerradas, que não têm `idReq` em comum ([R-requisicao-01](../fatos/requisicao.md#r-requisicao-01), [R-tempo-requisicao-01](../fatos/tempo-requisicao.md#r-tempo-requisicao-01), [R-tempo-por-status-01](../fatos/tempo-por-status.md#r-tempo-por-status-01) e [R-tempo-por-grupo-02](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-02)).
2. **Leia o estado pela tabela e o status pelo código.** Aberta é estar em `Req`; o status é `Status.cdSta`, e não o texto exibido ([R-requisicao-02](../fatos/requisicao.md#r-requisicao-02) e [R-status-fase-01](../dimensoes/status-fase.md#r-status-fase-01)).
3. **Cancelada é um status.** A requisição cancelada tem o código `CL` e está em uma das duas tabelas; decida se ela entra no seu indicador ([R-status-fase-04](../dimensoes/status-fase.md#r-status-fase-04)).
4. **Use `LEFT JOIN` nas ligações que aceitam vazio.** O status e a atividade da requisição podem estar vazios, e o `JOIN` comum some com essas linhas ([R-status-fase-02](../dimensoes/status-fase.md#r-status-fase-02) e [R-requisicao-04](../fatos/requisicao.md#r-requisicao-04)).

## Prazo e SLA

5. **Meça o prazo pelas datas.** Estourou o prazo é `dtFimPrev` anterior a `dtFimReal`, nas encerradas, ou ao momento da consulta, nas abertas ([R-marcos-02](../fatos/marcos.md#r-marcos-02)). A coluna `flgForaSLA` retrata só a última gravação, feita pela criação do plano de alertas, pelo processamento de alertas ou por uma atualização de versão do produto, que a zera ([R-marcos-04](../fatos/marcos.md#r-marcos-04)). Compare sempre com o `dtFimPrev` atual, porque o prazo de uma aberta é recalculado, por exemplo, quando o calendário ou o grupo muda ([R-tempo-calendario-04](../dimensoes/tempo-calendario.md#r-tempo-calendario-04) e [Marcos, seção 3](../fatos/marcos.md#3-tabelas)).
6. **Capture o "agora" uma vez por carga.** Nas abertas, guarde o horário da carga numa variável, use-o em todas as consultas e grave-o junto com o resultado ([R-marcos-07](../fatos/marcos.md#r-marcos-07)).
7. **Leia as datas como hora local, sem fuso, de dois relógios.** O servidor que executa o produto grava a data do histórico, e por isso `dtResposta` e `dtUltHistADO`, e é a base de `dtIniPrev` e `dtFimPrev`. O servidor de banco grava `dtAbertura`, `dtIniReal`, `dtFimReal` (quando o encerramento não informa a data) e `dtCalc`. Com fusos diferentes, um grupo de datas fica deslocado do outro; a regra traz a consulta que mostra se os dois relógios coincidem ([R-marcos-06](../fatos/marcos.md#r-marcos-06)).

## Tempos

8. **Os tempos são do último cálculo.** Uma aberta mostra o tempo de `dtCalc`; grave `dtCalc` junto e meça a defasagem ([R-tempo-requisicao-06](../fatos/tempo-requisicao.md#r-tempo-requisicao-06) e [R-tempo-requisicao-07](../fatos/tempo-requisicao.md#r-tempo-requisicao-07)).
9. **Não misture as unidades.** As colunas com sufixo `Cal` estão em minutos do calendário do grupo; as demais, em minutos corridos ([R-tempo-requisicao-03](../fatos/tempo-requisicao.md#r-tempo-requisicao-03)). O `sla` também está em minutos de calendário ([R-prioridade-sla-04](../dimensoes/prioridade-sla.md#r-prioridade-sla-04)).
10. **Primeira resposta é `dtResposta`.** Para o tempo até a primeira resposta, mantenha só as requisições com `dtResposta` preenchida ([R-marcos-01](../fatos/marcos.md#r-marcos-01) e [R-tempo-requisicao-05](../fatos/tempo-requisicao.md#r-tempo-requisicao-05)).

## Contagem e participação

11. **Conte requisições com `COUNT(DISTINCT idReq)`** quando a tabela tem mais de uma linha por requisição, como passagens por status e participações ([R-tempo-por-status-02](../fatos/tempo-por-status.md#r-tempo-por-status-02) e [R-participacao-06](../fatos/participacao.md#r-participacao-06)).
12. **Filtre o participante vigente com `dtFim IS NULL`.** As tabelas de participação guardam o histórico inteiro ([R-participacao-02](../fatos/participacao.md#r-participacao-02)).
13. **Ao juntar tempo por grupo e participação, confirme a requisição.** Junte por `idReqPart` e exija o mesmo `idReq` dos dois lados ([R-tempo-por-grupo-04](../fatos/tempo-por-grupo.md#r-tempo-por-grupo-04)).
14. **Leia a classificação da encerrada no retrato.** A encerrada guarda a categoria, a subcategoria e a atividade como estavam no encerramento ([R-requisicao-03](../fatos/requisicao.md#r-requisicao-03)).
