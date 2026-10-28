---
gerado: sincronizacao
---
# Matriz fato × dimensão


Cada linha é um fato; cada coluna, uma dimensão. A célula diz por qual coluna o fato cruza com a dimensão. Onde não há cruzamento direto, a célula aponta o fato que responde aquela combinação (por exemplo, tempo × grupo: use **tempo por grupo**). O modelo está em [Modelo](modelo.md).

Convenções das células:

- "**Requisição**" quer dizer: parta de [Fato: requisição](../fatos/requisicao.md), ligando o fato a `Req` ou `ReqConcluida` por `idReq`, e use a coluna da requisição.
- "`Req`/`ReqConcluida`" indica que a coluna existe nas duas tabelas da requisição (aberta e encerrada).

## 1. Matriz

| Fato | Tempo e calendário | Classificação | Status | Grupo | Pessoa e organização | Prioridade e SLA | Canal |
|---|---|---|---|---|---|---|---|
| [Requisição](../fatos/requisicao.md) | datas na própria linha (`dtAbertura`, `dtFimReal`); tempos gravados: **tempo da requisição**, por `idReq` | aberta: `Req.idTar` → `Tarefa`; encerrada: retrato em `ReqConcluida` | `idFrmStatus` → `FormStatus.idSta` → `Status.cdSta` | `idGruAtual`, `idGru` → `Grupo.idGru` | pessoas: **participação**; organização: `Req.idEmp` → `Empresa`, `Req.idHie` → `OrgHierarquia` | `nPrioridade`, `nImp`, `nUrg`, `sla` | `tpAgenteReg`; `idFrmOrigem` → `FormOrigem` |
| [Marcos](../fatos/marcos.md) | `idReq` → `ReqTime`/`ReqTimeConcluida`; calendário do grupo (`Grupo.idCan`) | mesma linha de `Req`/`ReqConcluida`: **Requisição** | mesma linha: **Requisição** | `idGruAtual` → `Grupo.idGru` | mesma linha: **Requisição** | `sla`, `flgForaSLA` na mesma linha | mesma linha: **Requisição** |
| [Tempo da requisição](../fatos/tempo-requisicao.md) | é o fato (`ReqTime`, `ReqTimeConcluida`); calendário do grupo (`Grupo.idCan`) | **Requisição** | **Tempo por status** | **Tempo por grupo** | **Tempo por grupo** | **Marcos** (`sla`, datas de prazo) | **Requisição** |
| [Tempo por grupo](../fatos/tempo-por-grupo.md) | é o fato (`tAtivoCal`, `tFreezeCal`); total: **tempo da requisição** | **Requisição** | **Tempo por status** | `idReqPart` → `ReqParticipante`; com `idTpPapel = 2`, `idPart` → `Grupo.idGru` | com `idTpPapel = 1`, `idPart` → `Usuario.idUsu` | **Marcos** | **Requisição** |
| [Tempo por status](../fatos/tempo-por-status.md) | é o fato (`nIntervaloCal`, `dtIniStatus`, `dtFimStatus`) | **Requisição** | `idFrmStatus` → `FormStatus.idSta` → `Status.cdSta` | grupo atual: **Requisição**; tempo do grupo: **tempo por grupo** | **Requisição** → participação, por `idReq` | **Marcos** | **Requisição** |
| [Eventos do histórico](../fatos/eventos-historico.md) | `dtFimReqHist` (data do evento); tempos: **tempo da requisição** | **Requisição** | `ReqHistorico.idFrmStatus` → `FormStatus.idSta` → `Status.cdSta` | **Requisição** (grupo atual, `idGruAtual`); grupo do autor: **Participação** por `idReqPart` | autor: `idUsu` → `Usuario.idUsu`; participação: `idReqPart` | **Marcos** | **Requisição** |
| [Participação](../fatos/participacao.md) | `dtInicio`, `dtFim` da participação; tempo gravado: **tempo por grupo** (`ReqTimeAdo.idReqPart`) | **Requisição** | **Requisição** | `idTpPapel = 2`: `idPart` → `Grupo.idGru` | `idTpPapel = 1`: `Usuario.idUsu`; `3`: `OrgHierarquia.idHie`; `13`: `UsuarioExterno.idExt` | **Requisição** | **Requisição** |
| [Dados adicionais](../fatos/dados-adicionais.md) | **Requisição**, por `DadValor.idQQ` | **Requisição**, por `idQQ` (a classificação é a da requisição); o escopo do contexto do campo (`DadContextoCampo.idTar`, `idSca`, `idCat`, `idAre`) está em R-dados-adicionais-10 | **Requisição**, por `idQQ` | **Requisição**, por `idQQ` | **Participação**, a partir da requisição por `idQQ` | **Requisição**, por `idQQ` | **Requisição**, por `idQQ` |
| [Vínculos](../fatos/vinculos.md) | **Requisição** (em `ReqVinculada`, pai por `idReq` e filha por `idReqVinculo`; o desdobramento `DESDD`, em `ReqVinculadaRef`, vai no sentido inverso: [R-vinculos-01](../fatos/vinculos.md)) | **Requisição** | **Requisição** | **Requisição** | **Participação** | **Requisição** | **Requisição** |
| [Avaliação e satisfação](../fatos/avaliacao-satisfacao.md) | `PesqRespCab.dtResp` (data da resposta); tempos: **tempo da requisição** | **Requisição** | **Requisição** | **Requisição** (`idGruAtual`) | `ReqAvaliacao.idUsu` → `Usuario.idUsu` | **Requisição** | **Requisição** |
| [Apontamento e despesas](../fatos/apontamento-e-despesas.md) | `ReqApontamento.dtBase` e `dtInicio`; `ReqDespesa.dtDespesa` e `dtRegistro`; tempos: **tempo da requisição** | **Requisição** | **Requisição** | **Requisição** (`idGruAtual`) | `idUsu`, `idUsuReporte`, `idUsuAprov` → `Usuario.idUsu`; `idReqPart` → **Participação** | **Requisição** | **Requisição** |

## 2. Onde achar o detalhe de cada coluna

- Tempo e calendário: [Calendário](../dimensoes/tempo-calendario.md).
- Classificação: [Classificação](../dimensoes/classificacao.md).
- Status: [Status e fase](../dimensoes/status-fase.md).
- Grupo: [Grupo e área](../dimensoes/grupo-area.md).
- Pessoa e organização: [Pessoa e organização](../dimensoes/pessoa-organizacao.md) e [Papéis e participação](papeis-e-participacao.md).
- Prioridade e SLA: [Prioridade e SLA](../dimensoes/prioridade-sla.md).
- Canal: [Canal e origem](../dimensoes/canal-origem.md).

## Veja também

- [Modelo](modelo.md)
- [Regras essenciais](regras-essenciais.md)
- [Abertas e encerradas](abertas-e-encerradas.md)
