---
gerado: sincronizacao
---

# dbo.SyncUsu

**Selo:** Só estrutura

!!! warning "Só estrutura"
    O significado das colunas desta tabela não está documentado. Não deduza o significado pelo nome da coluna.

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `chave` | VARCHAR(50) | não | não | não |
| `login` | VARCHAR(52) | sim | não | não |
| `dominio` | VARCHAR(30) | sim | não | não |
| `nome` | VARCHAR(150) | sim | não | não |
| `email` | VARCHAR(100) | sim | não | não |
| `matricula` | VARCHAR(50) | sim | não | não |
| `fone` | VARCHAR(17) | sim | não | não |
| `ramal` | VARCHAR(5) | sim | não | não |
| `celular` | VARCHAR(18) | sim | não | não |
| `cargo` | VARCHAR(250) | sim | não | não |
| `empresa` | VARCHAR(50) | sim | não | não |
| `ccusto` | VARCHAR(1000) | sim | não | não |
| `descCusto` | VARCHAR(1200) | sim | não | não |
| `superior` | VARCHAR(50) | sim | não | não |
| `nivSupHie` | SMALLINT | sim | não | não |
| `localizacao` | VARCHAR(1200) | sim | não | não |
| `codEmpresa` | VARCHAR(15) | sim | não | não |
| `codLocal` | VARCHAR(15) | sim | não | não |
| `superiorAlternativo` | VARCHAR(50) | sim | não | não |
| `flgIgnorar` | BIT | não | não | não |
