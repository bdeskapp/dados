---
gerado: sincronizacao
---

# dbo.SyncEmail

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [e-mail](../fora-de-escopo/email.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `dsKey` | VARCHAR(500) | não | não | não |
| `dsTo` | VARCHAR(100) | não | não | não |
| `dsFrom` | VARCHAR(100) | não | não | não |
| `dsSubject` | VARCHAR(300) | sim | não | não |
| `dsBody` | TEXT | sim | não | não |
| `dtReceived` | DATETIME | não | não | não |
| `qtdAnexo` | TINYINT | não | não | não |
| `dtSave` | DATETIME | não | não | não |
| `dtProcess` | DATETIME | sim | não | não |
| `dsErro` | VARCHAR(4000) | sim | não | não |
| `flgProc` | BIT | não | não | não |
| `idReq` | INT | sim | não | não |
| `flgUpdate` | BIT | sim | não | não |
| `flgDiscard` | BIT | sim | não | não |
| `UID` | VARCHAR(500) | sim | não | não |
| `sStatus` | CHAR(1) | sim | não | não |
| `dsCopia` | VARCHAR(3000) | sim | não | não |
| `idSyncEmail` | INT | não | não | não |
| `dsLog0` | TEXT | sim | não | não |
| `dsLog` | TEXT | sim | não | não |
