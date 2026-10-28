---
gerado: sincronizacao
---

# dbo.SyncUsuConfig

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `flgInclusao` | BIT | não | não | não |
| `flgAtualizacao` | BIT | não | não | não |
| `tpLogin` | CHAR(1) | sim | não | não |
| `idDom` | INT | sim | não | não |
| `idEmp` | INT | sim | não | não |
| `idPer` | INT | sim | não | não |
| `idGruAcesso` | VARCHAR(1000) | sim | não | não |
| `flgUpdFone` | BIT | não | não | não |
| `flgUpdRamal` | BIT | não | não | não |
| `flgUpdCelular` | BIT | não | não | não |
| `flgUpdLoc` | BIT | não | não | não |
| `flgUpdCCusto` | BIT | não | não | não |
| `flgInativacao` | BIT | não | não | não |
| `flgReativacao` | BIT | não | não | não |
| `flgCadCargo` | BIT | não | não | não |
| `flgCadEmpresa` | BIT | não | não | não |
| `flgCadDominio` | BIT | não | não | não |
| `flgCadLoc` | BIT | não | não | não |
| `flgCadHie` | BIT | não | não | não |
| `idEmpHie` | INT | sim | não | não |
| `Contato1` | VARCHAR(100) | sim | não | não |
| `Contato2` | VARCHAR(100) | sim | não | não |
| `Contato3` | VARCHAR(100) | sim | não | não |
| `TempoLog` | TINYINT | não | não | não |
| `qtdMinUsu` | INT | sim | não | não |
| `flgUpdLogin` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.SyncUsuConfig` (idDom) → `dbo.Dominio` (idDom)
- `dbo.SyncUsuConfig` (idEmp) → `dbo.Empresa` (idEmp)
- `dbo.SyncUsuConfig` (idEmpHie) → `dbo.Empresa` (idEmp)
- `dbo.SyncUsuConfig` (idPer) → `dbo.Perfil` (idPer)
