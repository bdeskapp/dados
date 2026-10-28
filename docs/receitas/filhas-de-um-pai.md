---
gerado: sincronizacao
---
# Receita: filhas de um pai


## 1. Pergunta e indicador

- **Pergunta:** quais requisições são filhas diretas (um nível; etapas de processo, desdobramentos e desdobramentos com dependência) de uma requisição pai?
- **Indicador:** filhas diretas do pai = linhas de `ReqVinculada` cujo `idReq` é o pai informado, mais as linhas de `ReqVinculadaRef` com `cdVinc = 'DESDD'` cujo `idReqVinculo` é o pai informado. As filhas das filhas não entram.

## 2. Definição usada

- Em `ReqVinculada`, `idReq` é o pai e `idReqVinculo` a filha.
- O desdobramento com dependência (`DESDD`) fica em `ReqVinculadaRef`, no sentido inverso: `idReq` é a desdobrada (a filha) e `idReqVinculo` a original (o pai). `ReqVinculadaRef` não tem `idFlu` nem `nivel`; nesse ramo as duas colunas vêm vazias.
- As duas tabelas servem a abertas e encerradas e não têm versão encerrada; o estado de cada filha vem de `LEFT JOIN` em `Req` e em `ReqConcluida`. A coluna `encerrada` vale `0` para filha aberta e `1` para filha encerrada; fica vazia, junto com o título, quando a filha não está em `Req` nem em `ReqConcluida`.
- O código do vínculo é `RTRIM(cdVinc)` (a coluna é `char(5)`) e pode vir vazio; o tipo é `idTpVinculo`, com a descrição em `TipoVinculo.dsTpVinculo` (cadastro do cliente). `nivel` é o nível da filha dentro do fluxo `idFlu`.
- Para o pai de uma filha, troque o filtro do primeiro ramo para a coluna `ReqVinculada.idReqVinculo` e o do segundo para a coluna `ReqVinculadaRef.idReq`. Os `JOIN` de título e de estado continuam na filha (`ReqVinculada.idReqVinculo` e `ReqVinculadaRef.idReq`); para ver o título e o estado do pai, ligue `Req` e `ReqConcluida` a `ReqVinculada.idReq` e a `ReqVinculadaRef.idReqVinculo`.

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro `@idReq` como placeholder fictício; `WITH(NOLOCK)`. A receita cobre pai e filha em qualquer estado. O primeiro ramo lê `ReqVinculada` e o segundo os desdobramentos com dependência de `ReqVinculadaRef`.

```sql
SELECT v.idReq AS idReqPai, v.idReqVinculo AS idReqFilha, RTRIM(v.cdVinc) AS cdVinc, v.idTpVinculo, tv.dsTpVinculo, v.idFlu, v.nivel,
    COALESCE(a.dsTitulo, c.dsTitulo) AS dsTituloFilha,
    CASE WHEN a.idReq IS NULL AND c.idReq IS NULL THEN NULL WHEN c.idReq IS NOT NULL THEN 1 ELSE 0 END AS encerrada
FROM ReqVinculada v WITH(NOLOCK)
    LEFT JOIN Req a WITH(NOLOCK) ON a.idReq = v.idReqVinculo
    LEFT JOIN ReqConcluida c WITH(NOLOCK) ON c.idReq = v.idReqVinculo
    LEFT JOIN TipoVinculo tv WITH(NOLOCK) ON tv.idTpVinculo = v.idTpVinculo
WHERE v.idReq = /* @idReq */ 0
UNION ALL
SELECT d.idReqVinculo, d.idReq, RTRIM(d.cdVinc), d.idTpVinculo, tv.dsTpVinculo, NULL, NULL,
    COALESCE(a.dsTitulo, c.dsTitulo),
    CASE WHEN a.idReq IS NULL AND c.idReq IS NULL THEN NULL WHEN c.idReq IS NOT NULL THEN 1 ELSE 0 END
FROM ReqVinculadaRef d WITH(NOLOCK)
    LEFT JOIN Req a WITH(NOLOCK) ON a.idReq = d.idReq
    LEFT JOIN ReqConcluida c WITH(NOLOCK) ON c.idReq = d.idReq
    LEFT JOIN TipoVinculo tv WITH(NOLOCK) ON tv.idTpVinculo = d.idTpVinculo
WHERE d.cdVinc = 'DESDD' AND d.idReqVinculo = /* @idReq */ 0;
```

Granularidade do resultado: uma linha por filha direta do pai informado.

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReqPai | idReqFilha | cdVinc | dsTpVinculo | nivel | dsTituloFilha | encerrada |
    |---|---|---|---|---|---|---|
    | 5001 | 5002 | DESD | Tipo Exemplo A | 2 | Filha Exemplo A | 0 |
    | 5001 | 5003 | | Tipo Exemplo B | 2 | Filha Exemplo B | 1 |
    | 5001 | 5004 | DESDD | Tipo Exemplo C | | Filha Exemplo C | 0 |

## 5. Regras aplicadas

- [R-vinculos-01](../fatos/vinculos.md): as filhas de um pai são as linhas de `ReqVinculada` com o pai em `idReq` e a filha em `idReqVinculo`, mais as linhas de `ReqVinculadaRef` com `cdVinc = 'DESDD'`, no sentido inverso (`idReqVinculo` = original, `idReq` = desdobrada).
- [R-vinculos-02](../fatos/vinculos.md): resolva o estado com `LEFT JOIN` em `Req` e em `ReqConcluida`.
- [R-vinculos-03](../fatos/vinculos.md): leia o código com `RTRIM(cdVinc)` e o tipo em `idTpVinculo`.

## Veja também

- [Fato: vínculos](../fatos/vinculos.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
