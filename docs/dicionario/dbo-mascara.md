---
gerado: sincronizacao
---

# dbo.Mascara

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idMascara` | INT | não | sim | não |
| `nmMascara` | VARCHAR(50) | não | não | não |
| `obsMascara` | VARCHAR(500) | sim | não | não |
| `txtMascara` | TEXT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `idGruAdm` | INT | não | não | não |

## Chaves estrangeiras

- `dbo.Formulario` (idMascara) → `dbo.Mascara` (idMascara)
- `dbo.KBClasse` (idMas) → `dbo.Mascara` (idMascara)
- `dbo.Mascara` (idGruAdm) → `dbo.Grupo` (idGru)
- `dbo.SubCategoria` (idMascara) → `dbo.Mascara` (idMascara)
- `dbo.Tarefa` (idMascara) → `dbo.Mascara` (idMascara)
