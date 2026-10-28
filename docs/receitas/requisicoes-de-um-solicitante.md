---
gerado: sincronizacao
---
# Receita: requisições de um solicitante


## 1. Pergunta e indicador

- **Pergunta:** quais requisições, abertas e encerradas, tiveram um determinado usuário como solicitante?
- **Indicador:** requisições do solicitante = requisições em que o usuário informado tem a participação vigente no papel Solicitante.

## 2. Definição usada

- Solicitante é o papel `ANTE` (rótulo do produto: "Solicitante", em [Valores definidos pelo produto](../dominios-do-produto.md)), lido por `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`.
- O participante é um usuário: `idTpPapel` = 1 e `idPart` = `Usuario.idUsu`; a participação de tipo 1 sem usuário real guarda um marcador `idPart <= 0`, que não aponta para `Usuario`. O papel `ANTE` também pode ser de tipo Externo (`idTpPapel` = 13); esta receita cobre o solicitante usuário.
- Vigente = `dtFim IS NULL` ([Papéis e participação](../mapa/papeis-e-participacao.md)).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro `@idUsu` como placeholder fictício; `WITH(NOLOCK)`. A coluna `encerrada` vale `0` nas abertas e `1` nas encerradas.

```sql
SELECT DISTINCT r.idReq, r.dsTitulo, r.dtAbertura, 0 AS encerrada
FROM Req r WITH(NOLOCK)
    JOIN ReqParticipante rp WITH(NOLOCK) ON rp.idReq = r.idReq
    JOIN FormPapel fp WITH(NOLOCK) ON fp.idFrmPapel = rp.idFrmPapel
    JOIN Papel p WITH(NOLOCK) ON p.idPapel = fp.idPapel
WHERE rp.idTpPapel = 1 AND rp.idPart = /* @idUsu */ 0 AND rp.dtFim IS NULL AND p.cdPapel = 'ANTE'
UNION ALL
SELECT DISTINCT c.idReq, c.dsTitulo, c.dtAbertura, 1
FROM ReqConcluida c WITH(NOLOCK)
    JOIN ReqPartConcluida rp WITH(NOLOCK) ON rp.idReq = c.idReq
    JOIN FormPapel fp WITH(NOLOCK) ON fp.idFrmPapel = rp.idFrmPapel
    JOIN Papel p WITH(NOLOCK) ON p.idPapel = fp.idPapel
WHERE rp.idTpPapel = 1 AND rp.idPart = /* @idUsu */ 0 AND rp.dtFim IS NULL AND p.cdPapel = 'ANTE';
```

Granularidade do resultado: uma linha por requisição. O `DISTINCT` garante uma linha por requisição mesmo quando o usuário tem duas participações vigentes `ANTE` na mesma requisição. A cópia de participantes no encerramento exige cadastro em `PartTipoPapel` e papel ativo no formulário (`FormPapel.flgAtivo = 1`): quem não tem esse cadastro, ou não tem papel ativo no formulário, falta na parte encerrada (limite documentado, decisão do produto; ver [Abertas e encerradas](../mapa/abertas-e-encerradas.md), seção 3.1).

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | dsTitulo | dtAbertura | encerrada |
    |---|---|---|---|
    | 1001 | Título de exemplo A | 2030-01-10 | 1 |
    | 1002 | Título de exemplo B | 2030-02-03 | 0 |

## 5. Regras aplicadas

- [R-participacao-01](../fatos/participacao.md): leia o papel por `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`.
- [R-participacao-02](../fatos/participacao.md): filtre o participante vigente com `dtFim IS NULL`.
- [R-requisicao-01](../fatos/requisicao.md): some abertas e encerradas.

## Veja também

- [Fato: participação](../fatos/participacao.md)
- [Fato: requisição](../fatos/requisicao.md)
