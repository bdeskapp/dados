---
gerado: sincronizacao
---
# Dimensão: status


## 1. O que é na tela

O **Status** aparece nas listas e no detalhe da requisição como um texto curto (por exemplo, o equivalente a "aberta", "em andamento" ou "concluída"). O texto exibido é o rótulo do status **no formulário** da requisição (`FormStatus.dsSta`). O que o sistema entende como status é o **código** `Status.cdSta`.

## 2. Estrutura: código fixo, rótulo por formulário

```
Req.idFrmStatus --> FormStatus.idFrmStatus --> FormStatus.idSta --> Status.idSta --> Status.cdSta
                    (um conjunto por formulário)                    (catálogo do produto)
```

| Tabela | O que guarda | Chaves |
|---|---|---|
| `Status` | catálogo de códigos (`cdSta`). Cada linha tem `flgSistema` (1 = definido pelo produto, 0 = criado pela instalação) | `idSta` |
| `FormStatus` | o conjunto de status **de cada formulário**: liga o formulário (`idFrm`) a um código (`idSta`) e dá o rótulo do formulário (`dsSta`). Traz também `flgContaSLA` (o status conta no prazo) e `tpCongelamento` | `idFrmStatus` |
| `FormTransicao` | as transições permitidas: ação (`idFrmAcao`) + status atual (`idFrmStatusAtual`) leva a um próximo status (`idFrmStatusProx`) | `idFrmTrans` |

- O mesmo código `cdSta` pode ter rótulos diferentes em formulários diferentes, porque `FormStatus.dsSta` é do formulário. O texto de `Status.dsSta` pode ser editado pela instalação.
- Por isso toda leitura de "em que status está" usa o **código** `Status.cdSta`, alcançado por `Req.idFrmStatus → FormStatus.idSta → Status.cdSta`.
- A instalação pode criar novos status (o código gravado é `U` seguido de um número, sem teto, e a linha nasce com `flgSistema = 0`). Eles não fazem parte da lista do produto.
- `tpCongelamento` existe em `FormStatus` e é gravado pelo cadastro do formulário; quando o status conta no prazo (`flgContaSLA = 1`) a coluna fica vazia (NULL); quando o status congela o prazo (`flgContaSLA = 0`) ela guarda um código que distingue o congelamento definitivo do temporário. Quando a requisição sai de um status de congelamento definitivo, o produto soma ao prazo o tempo que ela ficou parada nesse status.

## 3. Como a requisição aponta para o status

| Coluna | Em `Req` (aberta) | Em `ReqConcluida` (encerrada) |
|---|---|---|
| `idFrmStatus` | status atual do formulário; **pode vir vazia** | status em que a requisição terminou; não vem vazia; sem chave estrangeira |
| `dsSta` | não existe (o rótulo vem de `FormStatus`) | **retrato**: o `FormStatus.dsSta` do momento do encerramento |

- A encerrada guarda `dsSta` como estava ao terminar; o rótulo do formulário pode ter mudado depois.
- Em `Req`, `idFrmStatus` aceita vazio. Uma ligação com `FormStatus` por `INNER JOIN` deixa de fora essas requisições; use `LEFT JOIN`.

## 4. Valores do produto

Os códigos `Status.cdSta` definidos pelo produto (`flgSistema = 1`) estão em [Valores definidos pelo produto](../dominios-do-produto.md), seção "Status": `AA`, `AB`, `AG`, `AP`, `AT`, `AV`, `CL`, `CN`, `DIR`, `EA`, `EC`, `EN`, `EP`, `IND`, `NT`, `PN`, `REC`, `REJ`, `RP`. A página lista só os códigos, porque o texto de cada um é editável por instalação.

- **Cancelada é o status `CL`.** O produto marca a requisição como cancelada pelo código `CL` com `flgSistema = 1`. A requisição cancelada não tem tabela própria: está em `Req` ou em `ReqConcluida`.
- `CN` e `CL` aparecem em requisições das duas tabelas.

## 5. Status terminal e encerramento

A requisição passa de `Req` para `ReqConcluida` quando chega a um **status terminal**, não por uma ação específica:

1. Uma ação sobre a requisição (qualquer ação do formulário) faz a transição de status: o produto procura em `FormTransicao` o próximo status para o par (ação, status atual).
2. O status é **terminal** quando **não existe** linha de `FormTransicao` com esse status como `idFrmStatusAtual`.
3. Se o próximo status é terminal, o produto encerra a requisição: grava `Req.dtFimReal` e executa o procedimento de encerramento. Antes, o produto faz algumas validações. Por exemplo, quando o próprio sistema executa a ação `CONC` na requisição centralizadora do fluxo (`idReq = idFlu`), a conclusão é impedida se o fluxo tem etapas abertas e o processo tem `tpCalcPrazo = 'I'`.
4. O resultado: o status de toda requisição encerrada é terminal, e `ReqConcluida` guarda esse status em `idFrmStatus`.

Qualquer ação com transição para status terminal encerra a requisição, com a exceção descrita adiante, e a ação depende do formulário. O status seguinte de `CONC` em cada formulário vem de `FormTransicao`. Uma `Req` pode ficar parada num status sem transição de saída sem ter sido encerrada; a causa não está documentada aqui. Ela continua aberta, porque aberta é estar em `Req` (decisão do produto). A página [Ação](acao.md) descreve o vocabulário das ações; `CONC` e `ENC` têm o mesmo efeito (encerram quando levam a status final) e só o rótulo muda (decisão do produto).

## 6. Ativo e inativo

`Status.flgStaAtivo = 0` marca o código como desativado; a linha continua no banco. A leitura do histórico não depende desse campo: a requisição guarda o `idFrmStatus` em que está. `FormStatus.flgDisponivel = 1` filtra a lista de status do formulário.

## 7. Regras de uso

#### R-status-fase-01: Leia o status pelo código `Status.cdSta` (`Req.idFrmStatus → FormStatus.idSta → Status.cdSta`). {#r-status-fase-01}
`FormStatus.dsSta` é o rótulo do formulário e `Status.dsSta` é editável pela instalação; o código é o que o sistema entende.

#### R-status-fase-02: Ligue `Req.idFrmStatus` a `FormStatus` com `LEFT JOIN`. {#r-status-fase-02}
`idFrmStatus` aceita vazio em `Req`, e o `LEFT JOIN` mantém essas requisições na contagem.

#### R-status-fase-03: Leia o status de uma encerrada em `ReqConcluida.idFrmStatus` e o rótulo gravado em `ReqConcluida.dsSta`. {#r-status-fase-03}
O rótulo é o retrato do encerramento.

#### R-status-fase-04: Leia a requisição cancelada pelo código `CL`. {#r-status-fase-04}
Cancelada é um status; a requisição cancelada está em `Req` ou em `ReqConcluida`, e entra nas duas leituras de volume.

#### R-status-fase-05: Leia o estado pela tabela: aberta é estar em `Req`, mesmo em status terminal; a passagem para `ReqConcluida` acontece no status terminal. {#r-status-fase-05}
Status terminal é o que não tem transição de saída em `FormTransicao`. A passagem para `ReqConcluida` acontece quando a transição leva a um status sem saída, qualquer que seja a ação; o estado da requisição, aberta ou encerrada, é a tabela em que ela está (R-requisicao-02 e R-requisicao-06 em [Fato: requisição](../fatos/requisicao.md)). Exceção: uma `Req` parada num status final, sem ter passado para `ReqConcluida`, é aberta, porque aberta é estar em `Req` (decisão do produto).

## 8. Views recomendadas

`vwReq` e `vwReqTotal` trazem `dsSta` (rótulo atual na aberta, rótulo gravado na encerrada) e a coluna `ReqStatus` com a origem da linha ([Fato: requisição](../fatos/requisicao.md)). Para a leitura pelo código, junte `FormStatus` e `Status` como na seção 2.

## 9. Receitas

Receita desta dimensão: [tempo em cada status](../receitas/tempo-em-cada-status.md), que usa a cadeia da seção 2.

## Veja também

- [Ação](acao.md)
- [Fato: requisição](../fatos/requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
- [Classificação](classificacao.md)
