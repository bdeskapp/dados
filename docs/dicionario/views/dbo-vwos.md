---
gerado: sincronizacao
---

# dbo.vwOS

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo |
|---|---|
| `idOs` | int |
| `dtAbertura` | datetime |
| `dtIniOS` | datetime |
| `dtFimOS` | datetime |
| `dtFimAgend` | datetime |
| `estacao` | varchar |
| `idUsu` | int |
| `idUsuAbertura` | int |
| `idUsuResponsavel` | int |
| `idTar` | int |
| `idGru` | int |
| `idLoc` | int |
| `idAvi` | int |
| `idFlO` | int |
| `idSta` | int |
| `idTpco` | int |
| `idPat` | int |
| `idhie` | int |
| `idEmp` | int |
| `flgConfidencial` | bit |
| `flgTpAgend` | tinyint |
| `flgMail` | bit |
| `flgTpAbertura` | tinyint |
| `slaOS` | real |
| `slaRealOS` | real |
| `slaAtualOS` | real |
| `idGruAbertura` | int |
| `idTarAbertura` | int |
| `flgTpReporteHora` | char |
| `TempoGastoTotal` | real |
| `CustoTotal` | money |
| `dtFimPrevisto` | datetime |
| `dtIniReal` | datetime |

!!! note "Tipos sem tamanho"
    Os tipos são mostrados sem tamanho nem precisão (por exemplo, varchar sem o comprimento).
