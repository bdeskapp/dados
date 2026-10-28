---
gerado: sincronizacao
---
# Receita: requisições do grupo atual


## 1. Pergunta e indicador

- **Pergunta:** quais requisições, abertas e encerradas, têm um determinado grupo como grupo atual?
- **Indicador:** requisições do grupo = requisições cujo `idGruAtual` é o grupo informado.

## 2. Definição usada

- Grupo atual é a coluna `idGruAtual` de `Req` e de `ReqConcluida`. O produto a grava na abertura (igual a `idGru`), no direcionamento e na devolução, com o grupo do novo solicitado quando ele é de tipo Grupo e `NULL` quando é de outro tipo, como um usuário; grava também na categorização e na alteração do grupo solucionador, que escrevem o grupo solucionador. Na encerrada guarda o último valor.
- A requisição cujo solicitado atual é um usuário tem `idGruAtual` vazio e não entra na lista de nenhum grupo.
- O nome do grupo vem de `Grupo.dsGru` por `LEFT JOIN` em `idGruAtual`.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro `@idGru` como placeholder fictício; `WITH(NOLOCK)`. A coluna `encerrada` vale `0` nas abertas e `1` nas encerradas.

```sql
SELECT r.idReq, g.dsGru, r.dtAbertura, 0 AS encerrada
FROM Req r WITH(NOLOCK)
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = r.idGruAtual
WHERE r.idGruAtual = /* @idGru */ 0
UNION ALL
SELECT c.idReq, g.dsGru, c.dtAbertura, 1
FROM ReqConcluida c WITH(NOLOCK)
    LEFT JOIN Grupo g WITH(NOLOCK) ON g.idGru = c.idGruAtual
WHERE c.idGruAtual = /* @idGru */ 0;
```

Granularidade do resultado: uma linha por requisição.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | dsGru | dtAbertura | encerrada |
    |---|---|---|---|
    | 2001 | Grupo Exemplo A | 2030-03-01 | 0 |
    | 2002 | Grupo Exemplo A | 2030-03-02 | 1 |

## 5. Regras aplicadas

- [R-requisicao-05](../fatos/requisicao.md): leia o grupo atual em `idGruAtual` e o nome em `Grupo.dsGru`.
- [R-requisicao-01](../fatos/requisicao.md): some abertas e encerradas.

## Veja também

- [Fato: requisição](../fatos/requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
