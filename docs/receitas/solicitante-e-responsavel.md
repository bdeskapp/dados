---
gerado: sincronizacao
---
# Receita: solicitante e responsável das requisições de um grupo


## 1. Pergunta e indicador

- **Pergunta:** para as requisições de um grupo, quem é o solicitante e quem é o responsável?
- **Indicador:** pessoas da requisição = participações vigentes nos papéis Solicitante, Solicitado e Responsável, com o nome exibido.

## 2. Definição usada

- Os papéis são lidos por `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`, com os códigos e rótulos do produto de [Valores definidos pelo produto](../dominios-do-produto.md): `ANTE` (Solicitante), `ADO` (Solicitado, o atendente) e `RESP` (Responsável). O responsável do negócio é o participante `RESP` vigente (decisão do produto); a requisição sem `RESP` vigente fica sem responsável, e a receita não devolve linha `RESP` para ela.
- A receita devolve os três papéis, uma linha por participação, e o código `cdPapel` indica qual é qual. Uma requisição pode ter mais de uma entidade vigente num mesmo papel; o participante `ADO` é de tipo Grupo (`idTpPapel` = 2) ou de outro tipo, como Usuário (`idTpPapel` = 1), e `idTpPapel` diz qual em cada linha. O cálculo de tempos trata só o tipo 2 como grupo ao escolher o calendário do tempo de resposta; os demais tipos usam o calendário padrão.
- O recorte é o grupo atual (`idGruAtual`) da requisição; troque o filtro por outro critério de requisição quando a pergunta pedir.
- Vigente = `dtFim IS NULL`. Nome: nas abertas, `PartTipoPapel.nmPart` por `LEFT JOIN`; nas encerradas, `ReqPartConcluida.nmPart`, o nome gravado no encerramento (decisão do produto).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro `@idGru` como placeholder fictício; `WITH(NOLOCK)`. A coluna `encerrada` vale `0` nas abertas e `1` nas encerradas.

```sql
SELECT r.idReq, rp.idReqPart, p.cdPapel, rp.idTpPapel, rp.idPart, ptp.nmPart AS nome_exibido, 0 AS encerrada
FROM Req r WITH(NOLOCK)
    JOIN ReqParticipante rp WITH(NOLOCK) ON rp.idReq = r.idReq
    JOIN FormPapel fp WITH(NOLOCK) ON fp.idFrmPapel = rp.idFrmPapel
    JOIN Papel p WITH(NOLOCK) ON p.idPapel = fp.idPapel
    LEFT JOIN PartTipoPapel ptp WITH(NOLOCK) ON ptp.idTpPapel = rp.idTpPapel AND ptp.idPart = rp.idPart
WHERE r.idGruAtual = /* @idGru */ 0 AND rp.dtFim IS NULL AND p.cdPapel IN ('ANTE', 'ADO', 'RESP')
UNION ALL
SELECT c.idReq, rp.idReqPart, p.cdPapel, rp.idTpPapel, rp.idPart, rp.nmPart, 1
FROM ReqConcluida c WITH(NOLOCK)
    JOIN ReqPartConcluida rp WITH(NOLOCK) ON rp.idReq = c.idReq
    JOIN FormPapel fp WITH(NOLOCK) ON fp.idFrmPapel = rp.idFrmPapel
    JOIN Papel p WITH(NOLOCK) ON p.idPapel = fp.idPapel
WHERE c.idGruAtual = /* @idGru */ 0 AND rp.dtFim IS NULL AND p.cdPapel IN ('ANTE', 'ADO', 'RESP');
```

Granularidade do resultado: uma linha por requisição × participação vigente (`idReqPart`) nos três papéis. A cópia de participantes no encerramento exige cadastro em `PartTipoPapel` e papel ativo no formulário (`FormPapel.flgAtivo = 1`): quem não tem esse cadastro, ou não tem papel ativo no formulário, falta na parte encerrada (limite documentado, decisão do produto; ver [Abertas e encerradas](../mapa/abertas-e-encerradas.md), seção 3.1).

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReq | idReqPart | cdPapel | idTpPapel | idPart | nome_exibido | encerrada |
    |---|---|---|---|---|---|---|
    | 3001 | 8001 | ANTE | 1 | 501 | Pessoa Exemplo A | 0 |
    | 3001 | 8002 | ADO | 2 | 77 | Grupo Exemplo A | 0 |
    | 3001 | 8003 | RESP | 1 | 502 | Pessoa Exemplo B | 0 |

## 5. Regras aplicadas

- [R-participacao-01](../fatos/participacao.md): leia o papel por `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`.
- [R-participacao-02](../fatos/participacao.md): filtre o participante vigente com `dtFim IS NULL`.
- [R-participacao-06](../fatos/participacao.md): conte participações por `idReqPart` e requisições por `COUNT(DISTINCT idReq)`.
- [R-requisicao-05](../fatos/requisicao.md): leia o grupo atual em `idGruAtual`.

## Veja também

- [Fato: participação](../fatos/participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)
