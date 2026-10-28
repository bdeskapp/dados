---
gerado: sincronizacao
---

# dbo.RelCust

**Selo:** Citada

!!! info "Citada"
    Esta tabela é citada em receitas ou páginas de referência, mas não tem página de negócio própria.

Citada em:

- [motor de relatórios](../fora-de-escopo/motor-de-relatorios.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idRelCust` | INT | não | sim | não |
| `nmRelCust` | VARCHAR(30) | não | não | não |
| `dsTitulo` | VARCHAR(100) | não | não | não |
| `dsSubTitulo` | VARCHAR(100) | sim | não | não |
| `dsQuery` | VARCHAR(3500) | não | não | não |
| `dsQueryCat` | VARCHAR(2500) | sim | não | não |
| `dsQueryCal` | VARCHAR(1000) | sim | não | não |
| `cdGrafico` | CHAR(10) | não | não | não |
| `dsPrefixo` | VARCHAR(10) | sim | não | não |
| `dsSufixo` | VARCHAR(10) | sim | não | não |
| `nDecimalPrecision` | TINYINT | não | não | não |
| `dsEixoX` | VARCHAR(30) | sim | não | não |
| `dsEixoY` | VARCHAR(30) | sim | não | não |
| `dsPar` | VARCHAR(100) | sim | não | não |
| `dsParLink` | VARCHAR(100) | sim | não | não |
| `idRelCustFilho` | INT | sim | não | não |
| `flgMenu` | BIT | não | não | não |
| `colorIndex` | TINYINT | não | não | não |

## Chaves estrangeiras

- `dbo.RelCustPerfil` (idRelCust) → `dbo.RelCust` (idRelCust)
- `dbo.RelCustRelac` (idRelCust) → `dbo.RelCust` (idRelCust)
- `dbo.RelCustRelac` (idRelCustRelac) → `dbo.RelCust` (idRelCust)
- `dbo.RelCust` (cdGrafico) → `dbo.Grafico` (cdGrafico)
- `dbo.RelCust` (idRelCustFilho) → `dbo.RelCust` (idRelCust)
