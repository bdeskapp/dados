---
gerado: sincronizacao
---

# dbo.SyncEmailConfig

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [e-mail](../fora-de-escopo/email.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idEmailConfig` | INT | não | sim | não |
| `dsTo` | VARCHAR(100) | não | não | não |
| `diasLog` | INT | não | não | não |
| `idFrm` | INT | não | não | não |
| `idTpPapelADO` | INT | não | não | não |
| `idPartADO` | INT | não | não | não |
| `idFrmOrigem` | INT | sim | não | não |
| `dtAtualiza` | DATETIME | não | não | não |
| `idUsu` | INT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgExterno` | BIT | não | não | não |
| `Contato1` | VARCHAR(100) | sim | não | não |
| `Contato2` | VARCHAR(100) | sim | não | não |
| `Contato3` | VARCHAR(100) | sim | não | não |
| `flgAnexos` | BIT | não | não | não |
| `idFrmTpDoc` | INT | sim | não | não |

## Chaves estrangeiras

- `dbo.SyncEmailConfig` (idFrmTpDoc) → `dbo.FormTipoDoc` (idFrmTpDoc)
- `dbo.SyncEmailConfig` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.SyncEmailConfig` (idUsu) → `dbo.Usuario` (idUsu)
