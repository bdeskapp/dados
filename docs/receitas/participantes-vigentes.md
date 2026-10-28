---
gerado: sincronizacao
---
# Receita: participantes vigentes de uma requisição


## 1. Pergunta e indicador

- **Pergunta:** quem participa agora de uma requisição, em que papel e com que nome?
- **Indicador:** participantes vigentes = participações da requisição com `dtFim IS NULL`, com código e rótulo do papel, tipo e nome exibido.

## 2. Definição usada

- Vigente = `dtFim IS NULL`; o filtro é escrito por quem consulta ([Papéis e participação](../mapa/papeis-e-participacao.md)).
- Papel: `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`; o rótulo é `FormPapel.dsPapel` nas abertas e, nas encerradas, `ReqPartConcluida.dsPapel`, o rótulo gravado no encerramento (decisão do produto). Tipo: `idTpPapel → TipoPapel.dsTpPapel`.
- Nome: nas abertas, `PartTipoPapel.nmPart` por `LEFT JOIN` no par (`idTpPapel`, `idPart`); nas encerradas, `ReqPartConcluida.nmPart`, o nome gravado no encerramento (decisão do produto).

## 3. SQL

Compatível com SQL Server em nível 130; parâmetro `@idReq` como placeholder fictício; `WITH(NOLOCK)`. A requisição está em uma das duas tabelas; a outra metade devolve zero linhas. A coluna `encerrada` vale `0` nas abertas e `1` nas encerradas.

```sql
SELECT rp.idReqPart, p.cdPapel, fp.dsPapel AS rotulo_no_formulario, rp.idTpPapel, tp.dsTpPapel, rp.idPart, ptp.nmPart AS nome_exibido, rp.dtInicio, 0 AS encerrada
FROM ReqParticipante rp WITH(NOLOCK)
    JOIN FormPapel fp WITH(NOLOCK) ON fp.idFrmPapel = rp.idFrmPapel
    JOIN Papel p WITH(NOLOCK) ON p.idPapel = fp.idPapel
    JOIN TipoPapel tp WITH(NOLOCK) ON tp.idTpPapel = rp.idTpPapel
    LEFT JOIN PartTipoPapel ptp WITH(NOLOCK) ON ptp.idTpPapel = rp.idTpPapel AND ptp.idPart = rp.idPart
WHERE rp.idReq = /* @idReq */ 0 AND rp.dtFim IS NULL
UNION ALL
SELECT rp.idReqPart, p.cdPapel, rp.dsPapel, rp.idTpPapel, tp.dsTpPapel, rp.idPart, rp.nmPart, rp.dtInicio, 1
FROM ReqPartConcluida rp WITH(NOLOCK)
    JOIN FormPapel fp WITH(NOLOCK) ON fp.idFrmPapel = rp.idFrmPapel
    JOIN Papel p WITH(NOLOCK) ON p.idPapel = fp.idPapel
    JOIN TipoPapel tp WITH(NOLOCK) ON tp.idTpPapel = rp.idTpPapel
WHERE rp.idReq = /* @idReq */ 0 AND rp.dtFim IS NULL;
```

Granularidade do resultado: uma linha por participação vigente (`idReqPart`). A cópia de participantes no encerramento exige cadastro em `PartTipoPapel` e papel ativo no formulário (`FormPapel.flgAtivo = 1`): quem não tem esse cadastro, ou não tem papel ativo no formulário, falta na parte encerrada (limite documentado, decisão do produto; ver [Abertas e encerradas](../mapa/abertas-e-encerradas.md), seção 3.1).

## 4. Exemplo de resultado

!!! example "Exemplo fictício"
    | idReqPart | cdPapel | rotulo_no_formulario | idTpPapel | dsTpPapel | idPart | nome_exibido | encerrada |
    |---|---|---|---|---|---|---|---|
    | 9001 | ANTE | Solicitante | 1 | Usuário | 501 | Pessoa Exemplo A | 0 |
    | 9002 | ADO | Solicitado | 2 | Grupo | 77 | Grupo Exemplo A | 0 |

## 5. Regras aplicadas

- [R-participacao-01](../fatos/participacao.md): leia o papel por `idFrmPapel → FormPapel.idPapel → Papel.cdPapel`.
- [R-participacao-02](../fatos/participacao.md): filtre o participante vigente com `dtFim IS NULL`.
- [R-participacao-03](../fatos/participacao.md): leia `idPart` conforme o tipo.
- [R-participacao-04](../fatos/participacao.md): leia o nome exibido por `LEFT JOIN` em `PartTipoPapel`.

## Veja também

- [Fato: participação](../fatos/participacao.md)
- [Papéis e participação](../mapa/papeis-e-participacao.md)
