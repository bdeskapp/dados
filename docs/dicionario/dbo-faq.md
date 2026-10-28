---
gerado: sincronizacao
---

# dbo.FAQ

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idFAQ` | INT | não | sim | não |
| `cdFaq` | INT | sim | não | não |
| `dsVersao` | VARCHAR(50) | sim | não | não |
| `dsPergunta` | VARCHAR(300) | sim | não | não |
| `dsResposta` | TEXT | não | não | não |
| `idUsu` | INT | não | não | não |
| `flgDisponivel` | BIT | não | não | não |
| `flgSistema` | BIT | não | não | não |
| `idNivelSup` | INT | sim | não | não |
| `dtEdicao` | DATETIME | sim | não | não |
| `flgRevisao` | BIT | não | não | não |
| `dtRevisao` | DATETIME | sim | não | não |
| `idRev` | INT | sim | não | não |
| `flgNivelInf` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.FAQAcao` (idFAQ) → `dbo.FAQ` (idFAQ)
- `dbo.FAQImagem` (idFAQ) → `dbo.FAQ` (idFAQ)
- `dbo.FAQObjeto` (idFAQ) → `dbo.FAQ` (idFAQ)
- `dbo.FAQRelac` (idFAQ) → `dbo.FAQ` (idFAQ)
- `dbo.FAQRelac` (idFAQRelac) → `dbo.FAQ` (idFAQ)
- `dbo.FAQ` (idNivelSup) → `dbo.FAQ` (idFAQ)
