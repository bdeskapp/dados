---
gerado: sincronizacao
---

# dbo.Metrica

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `cdMetrica` | INT | não | sim | não |
| `nmMetrica` | VARCHAR(100) | não | não | não |
| `dsMetrica` | VARCHAR(100) | não | não | não |
| `dsAbrev` | VARCHAR(15) | não | não | não |
| `obsMetrica` | VARCHAR(1000) | sim | não | não |
| `flgMensal` | BIT | não | não | não |
| `flgSemanal` | BIT | não | não | não |
| `flgDiaria` | BIT | não | não | não |
| `cdRef` | VARCHAR(6) | não | não | não |
| `flgSistema` | BIT | não | não | não |
| `flgAtiva` | BIT | não | não | não |
| `flgCalc` | BIT | não | não | não |
| `dsProcCalc` | VARCHAR(100) | não | não | não |

## Chaves estrangeiras

- `dbo.MetricaCalc_Are` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_Ger` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_Gru` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_Hie` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_KBUtil` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_KB` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.MetricaCalc_Pat` (cdMetrica) → `dbo.Metrica` (cdMetrica)
- `dbo.Metrica` (cdRef) → `dbo.MetricaRef` (cdRef)
