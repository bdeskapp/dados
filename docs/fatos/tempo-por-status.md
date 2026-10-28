---
gerado: sincronizacao
---
# Fato: tempo por status


## 1. O que mede

Quanto tempo a requisição ficou em cada status, a cada vez que passou por ele: de quando entrou no status até quando saiu, em minutos corridos e em minutos do calendário do grupo.

## 2. Granularidade

Uma linha por passagem da requisição por um status. Se a requisição volta a um status em que já esteve, a nova passagem é outra linha. A chave é `idReqStatus`. A passagem atual de uma requisição aberta ainda não foi fechada: ela fecha quando a requisição muda de status ou é encerrada, e até lá o lote diário grava nela um fim provisório (seção 4). Por decisão do produto, no tempo por status excluem-se só as passagens de intervalo negativo; a conta está na receita [tempo em cada status](../receitas/tempo-em-cada-status.md).

## 3. Tabelas

| Estado | Tabela | Observação |
|---|---|---|
| Aberta | `ReqStatus` | tem ainda `flgUtilizado` |
| Encerrada | `ReqStatusConcluida` | copiada de `ReqStatus` no encerramento |
| Ambas | `vwRepTimeStatus` | `UNION ALL` das duas, com `idReq`, `idFrmStatus`, `tStatusCal` e `dtFimStatus` (ver seção 7) |
| Status | `FormStatus` → `Status` | `idFrmStatus` → `FormStatus.idSta` → `Status.cdSta` |

- **Quem grava.** A cada mudança de status da requisição (`Req.idFrmStatus`), a passagem anterior é fechada e a nova linha é inserida em `ReqStatus`. O fechamento preenche `dtFimStatus`, `nIntervaloReal` (minutos corridos) e `nIntervaloCal` (minutos do calendário do grupo atual). Uma vez por dia, por rotina agendada, um lote atualiza as passagens atuais das abertas. No encerramento, a passagem atual é fechada e as linhas são copiadas para `ReqStatusConcluida`.
- **Fonte própria.** Os intervalos desta tabela vêm das passagens de status; os tempos de `ReqTime` vêm do histórico (`ReqHistorico`) e dos participantes. As duas fontes não se somam nem se completam.

## 4. Colunas-chave

A lista completa fica no dicionário de colunas.

| Coluna | Significado | Unidade |
|---|---|---|
| `idReqStatus` | identificador da passagem | |
| `idReq` | requisição | |
| `idFrmStatus` | status do formulário nesta passagem (`FormStatus`) | |
| `dtIniStatus` | entrada no status | data e hora |
| `dtFimStatus` | saída do status; na passagem atual de uma aberta, o lote diário grava um fim provisório, a data e hora do lote, de modo que a coluna fica vazia só antes do primeiro lote; o lote e a mudança de status escolhem a passagem por critérios diferentes (ver R-tempo-por-status-04) | data e hora |
| `nIntervaloReal` | duração da passagem em minutos corridos; vazia enquanto a passagem não tem `dtFimStatus`; na passagem atual de uma aberta traz o valor provisório do último lote | minutos |
| `nIntervaloCal` | duração da passagem no calendário do grupo; vazia enquanto a passagem não tem `dtFimStatus`; na passagem atual de uma aberta traz o valor provisório do último lote | minutos do calendário |

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Status | `idFrmStatus` → `FormStatus.idFrmStatus`; `FormStatus.idSta` → `Status.idSta`; o código é `Status.cdSta` |
| Requisição | `idReq` → `Req.idReq` ou `ReqConcluida.idReq` |
| Tempo da requisição | por `idReq` ([Tempo da requisição](tempo-requisicao.md)) |

## 6. Regras de uso

#### R-tempo-por-status-01: Some `ReqStatus` e `ReqStatusConcluida` para qualquer histórico. {#r-tempo-por-status-01}
A primeira guarda as requisições abertas e a segunda as encerradas.
Receita: [tempo em cada status](../receitas/tempo-em-cada-status.md)

#### R-tempo-por-status-02: Conte passagens por linha e requisições por `COUNT(DISTINCT idReq)`. {#r-tempo-por-status-02}
O mesmo status pode aparecer mais de uma vez na mesma requisição.
Receita: [tempo em cada status](../receitas/tempo-em-cada-status.md)

#### R-tempo-por-status-03: Leia o status pelo código, por `FormStatus.idSta` → `Status.cdSta`. {#r-tempo-por-status-03}
O rótulo `FormStatus.dsSta` é definido por formulário.
Receita: [tempo em cada status](../receitas/tempo-em-cada-status.md)

#### R-tempo-por-status-04: Entenda a passagem atual de uma aberta como uma passagem em curso. {#r-tempo-por-status-04}
`dtFimStatus IS NULL` não identifica a passagem em curso: o lote diário grava `dtFimStatus`, `nIntervaloReal` e `nIntervaloCal` provisórios (a data e hora do lote) nas passagens atuais das abertas. Há dois critérios para "passagem atual": na mudança de status, vale a de maior `idReqStatus`, e no lote, a de maior `dtIniStatus`. Eles coincidem quando `dtIniStatus` cresce com o `idReqStatus`; a mudança de status grava `dtIniStatus` com o maior `dtFimReqHist` do status anterior, que pode ser menor que o de uma passagem anterior, e então o lote grava o valor provisório numa passagem antiga já fechada, ou nas duas em caso de empate de `dtIniStatus`. `SUM`, `AVG` e `vwRepTimeStatus` incluem os valores provisórios. Para somar só passagens fechadas de uma aberta, exclua a passagem de maior `idReqStatus` da requisição e as passagens cujo `dtIniStatus` é igual ao maior `dtIniStatus` dela.
Receita: [tempo em cada status](../receitas/tempo-em-cada-status.md)

## 7. Views recomendadas

- `vwRepTimeStatus`: responde "tempo em minutos de calendário por passagem de status, abertas e encerradas". Granularidade: uma linha por passagem. Cobre abertas e encerradas, com `idReq`, `idFrmStatus`, `tStatusCal` (= `nIntervaloCal`) e `dtFimStatus`. **Como usar:** junte `idFrmStatus` a `FormStatus` e `Status` para chegar ao código; para minutos corridos ou para `dtIniStatus`, use as tabelas desta página.

## 8. Receitas

- [Tempo em cada status](../receitas/tempo-em-cada-status.md)

## Veja também

- [Tempo da requisição](tempo-requisicao.md)
- [Fato: requisição](requisicao.md)
