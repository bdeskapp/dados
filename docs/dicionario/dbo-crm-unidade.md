---
gerado: sincronizacao
---

# dbo.CRM_Unidade

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idUni` | INT | não | sim | não |
| `dsUni` | VARCHAR(20) | não | não | não |
| `idGestor` | INT | não | não | não |
| `flgUniAtivo` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CRM_Contrato` (idUni) → `dbo.CRM_Unidade` (idUni)
- `dbo.CRM_Empresa` (idUni) → `dbo.CRM_Unidade` (idUni)
- `dbo.CRM_FatAcesso` (idUni) → `dbo.CRM_Unidade` (idUni)
- `dbo.CRM_Gestor` (idUni) → `dbo.CRM_Unidade` (idUni)
