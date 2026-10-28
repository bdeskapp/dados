---
gerado: sincronizacao
---
# Fato: dados adicionais


## 1. O que mede

Dados adicionais são os campos que cada formulário, atividade, subcategoria, categoria ou área acrescenta à requisição, além das colunas de `Req`. O que o usuário preenche nesses campos é o valor de dado adicional. Servem para perguntas como "qual o valor do campo X nas requisições do formulário Y" e "quantas requisições escolheram cada item de uma lista".

O modelo é de três camadas, e o valor sempre se lê pelo caminho inteiro:

```
DadoAdicional      o campo (nome, tipo)                         chave idDad
   │  idDad
DadContextoCampo   o campo num contexto (formulário, atividade…) chave idDadCon
   │  idDadCon
DadValor           o valor preenchido numa requisição            chave idDadVal
   │  idQQ                    │  idDadVal
Req / ReqConcluida            DadValorDominio → DadDominio       (campo de lista)
```

## 2. Granularidade

Uma linha de `DadValor` é um valor de um campo, num contexto, de uma requisição. A chave natural é (`idQQ`, `idDadCon`, `nSeq`, `flgAgenda`); nenhum índice a torna única: o único índice único é a chave primária, em `idDadVal`, e o outro índice, em `idQQ`, não é único. `idDadVal` é a chave técnica e identifica uma linha. Em campo de lista, o valor são as linhas de `DadValorDominio` (uma por item escolhido, chave `idDadVal` + `idDom`), e a leitura do valor de lista é feita nessas linhas, não nas colunas de valor da própria `DadValor` (uma troca de tipo pode deixar valor antigo nelas, como descrito adiante). Nos demais tipos, o produto grava o valor em uma só coluna, a que o `tpDado` indica, na inserção e na atualização. A atualização grava só a coluna do `tpDado` atual e não limpa as outras; se o tipo do campo mudar, o valor antigo permanece na coluna antiga. Leia só a coluna do `tpDado` atual do campo.

- **`nSeq`** numera as repetições de um conjunto múltiplo (`DadConjunto.flgMultiplo = 1`). Em campo fora de conjunto múltiplo, `nSeq` vale 1.
- **Mais de um contexto.** O mesmo campo (`idDad`) pode ter valor em mais de um contexto da mesma requisição, com valores diferentes. Por isso "uma linha por requisição e campo" exige escolher o contexto ou conferir a contagem de contextos (ver [pivô de campos](../receitas/pivo-de-campos.md)).

## 3. Tabelas

| Papel | Tabela | Observação |
|---|---|---|
| Campo | `DadoAdicional` | `dsDad` é o nome do campo; `tpDado` é o tipo; `flgDadAtivo` é o cadastro ativo |
| Campo num contexto | `DadContextoCampo` | liga o campo (`idDad`) a um escopo; `idEnt` diz a que entidade o contexto se refere |
| Entidade | `DadEntidade` | o domínio do produto traz `3` Requisição ([Valores definidos pelo produto](../dominios-do-produto.md)) |
| Valor | `DadValor` | uma única tabela para requisições abertas e encerradas |
| Item escolhido (lista) | `DadValorDominio` | várias linhas por `idDadVal` |
| Rótulo do item | `DadDominio` | `dsDom` é o texto do item |
| Conjunto | `DadConjunto` | agrupa campos; `flgMultiplo` indica conjunto repetível |

- **Abertas e encerradas.** `DadValor` guarda os valores dos dois estados e não tem tabela par: o encerramento não move nem copia dados adicionais, e a própria pesquisa de requisições do produto junta `DadValor` a `Req` e a `ReqConcluida` pela mesma condição `idReq = idQQ` e `flgAgenda = 0`.
- **Ligação com a requisição.** `DadValor` não tem coluna `idReq`: a requisição está em `idQQ`. `idQQ` é o id da instância da entidade do contexto (`DadContextoCampo.idEnt`): vale `Req.idReq` ou `ReqConcluida.idReq` quando `idEnt = 3` (Requisição); com outro `idEnt`, `idQQ` é o id da instância dessa outra entidade. O produto trata `idEnt = 3` como "a entidade é requisição" e grava em `idQQ` o `idReq` da requisição.
- **Quem grava.** Quando o usuário salva o formulário, o produto insere, atualiza e apaga `DadValor` e `DadValorDominio`, e registra cada alteração em `DadLog`. Nenhum gatilho está definido sobre `DadValor`, `DadValorDominio` nem `DadLog`; três gatilhos de outras tabelas gravam em tabelas de configuração de dados adicionais, como `DadFormAcao` e `DadFormPapelStatus`.

## 4. Colunas-chave

A lista completa fica no dicionário de colunas.

| Coluna | Significado | Unidade |
|---|---|---|
| `DadValor.idQQ` | instância da entidade do contexto; `idReq` quando `idEnt = 3` | |
| `DadValor.idDadCon` | contexto do campo (`DadContextoCampo`) | |
| `DadValor.flgAgenda` | `0` para valor de requisição; `1` para agenda de requisição | |
| `DadValor.nSeq` | repetição dentro de um conjunto múltiplo; `1` nos demais | |
| `DadValor.string`, `numero`, `data`, `boolean`, `dinheiro`, `texto` | o valor, na coluna que o `tpDado` indica (seção abaixo) | conforme o tipo |
| `DadContextoCampo.idEnt` | entidade do contexto (`3` = Requisição, em [Valores definidos pelo produto](../dominios-do-produto.md)) | |
| `DadContextoCampo.idFrm`, `idTar`, `idSca`, `idCat`, `idAre` | escopo do contexto: formulário, atividade, subcategoria, categoria ou área; cada contexto de requisição (`idEnt = 3`) preenche exatamente um | |
| `DadContextoCampo.idCon` | conjunto do campo, quando houver | |
| `DadContextoCampo.flgContextoAtivo` | o contexto está ativo para novos preenchimentos | |
| `DadoAdicional.tpDado` | tipo do dado | |
| `DadoAdicional.flgDadAtivo` | o campo está ativo no cadastro | |
| `DadDominio.dsDom` | texto do item de lista | texto |
| `DadDominio.idDad` | campo dono do item | |

### Tipo do dado e coluna do valor

`DadoAdicional.tpDado` segue a lista de tipos do produto, com os rótulos de [Valores definidos pelo produto](../dominios-do-produto.md) (os rótulos são descrições do tipo de dado, não os nomes exibidos na tela), e a tabela abaixo mostra a coluna em que cada tipo é gravado.

| `tpDado` | Tipo no produto | Coluna do valor em `DadValor` |
|---|---|---|
| `1` | Caractere | `string` |
| `2` | Data | `data` |
| `3` | Inteiro | `numero` |
| `4` | Decimal | `numero` |
| `5` | Lógico | `boolean` |
| `6` | Monetário | `dinheiro` |
| `7` | Texto longo | `texto` |
| `8` | Domínio | nenhuma: o valor está em `DadValorDominio` |
| `9` | Tabela | `texto` (o produto também consulta `DadValorTabela` para este tipo) |
| `10` | Marca de ação executada | `boolean` |
| `11` | Lista definida pelo usuário | `string` |
| `12` | Calculado por stored procedure (texto) | `texto` |
| `13` | Calculado por stored procedure (data) | `data` |
| `14` | Calculado por stored procedure (monetário) | `dinheiro` |
| `15` | Data e hora | `data` |

A coluna `texto` é do tipo `TEXT`; para comparar ou exibir, converta com `CAST(DadValor.texto AS VARCHAR(MAX))`. Em agregação, `MAX` não aceita `bit` nem `TEXT`: use `MAX(CAST(DadValor.boolean AS INT))` e `MAX(CAST(DadValor.texto AS VARCHAR(MAX)))` ([pivô de campos](../receitas/pivo-de-campos.md)).

## 5. Como cruzar com as dimensões

| Dimensão | Como cruzar |
|---|---|
| Requisição | `DadValor.idQQ` → `Req.idReq` ou `ReqConcluida.idReq`, com `DadContextoCampo.idEnt = 3` |
| Formulário | pelo contexto: `DadContextoCampo.idFrm` → `Formulario.idFrm`; pela requisição: `Req.idFrm` ou `ReqConcluida.idFrm` ([formulários que usam um campo](../receitas/formularios-que-usam-campo.md)) |
| Atividade, subcategoria, categoria e área | pelo contexto: `DadContextoCampo.idTar`, `idSca`, `idCat` e `idAre`; um contexto com esses escopos vale para a classificação inteira |
| Item de lista | `DadValorDominio.idDom` → `DadDominio.idDom` |
| Conjunto | `DadContextoCampo.idCon` → `DadConjunto.idCon` |

## 6. Regras de uso

#### R-dados-adicionais-01: Ligue `DadValor` à requisição por `idQQ` e filtre `DadContextoCampo.idEnt = 3`. {#r-dados-adicionais-01}
`DadValor` não tem `idReq`. `idQQ` é o id da instância da entidade do contexto, e `DadValor` não tem chave estrangeira para `Req`, de modo que o `idQQ` de contextos de outras entidades pode coincidir numericamente com um `idReq`; o filtro `idEnt = 3` seleciona só os valores de requisição.
Receita: [valores de um campo](../receitas/valores-de-um-campo.md)

#### R-dados-adicionais-02: Leia abertas e encerradas na mesma `DadValor`, juntando com `Req` e com `ReqConcluida`. {#r-dados-adicionais-02}
`DadValor` guarda os dois estados. `Req` e `ReqConcluida` não têm `idReq` em comum ([Abertas e encerradas](../mapa/abertas-e-encerradas.md)), então a união dos dois ramos devolve cada valor uma vez.
Receita: [valores de um campo](../receitas/valores-de-um-campo.md)

#### R-dados-adicionais-03: Chegue ao campo por `DadValor.idDadCon → DadContextoCampo.idDad → DadoAdicional`. {#r-dados-adicionais-03}
O valor está ligado ao contexto, e o contexto liga ao campo. Para "todos os valores do campo X", filtre `DadContextoCampo.idDad`; um campo pode ter vários contextos (um por formulário, atividade e assim por diante).
Receita: [valores de um campo](../receitas/valores-de-um-campo.md)

#### R-dados-adicionais-04: Leia o valor na coluna que o `tpDado` indica. {#r-dados-adicionais-04}
A tabela da seção 4 lista a coluna de cada tipo; leia só a coluna do `tpDado` atual do campo, porque a atualização não limpa as outras colunas. Os tipos `3` e `4` usam `numero`; `7`, `9` e `12` usam `texto`; o tipo `8` não usa coluna de `DadValor`. Em agregação, converta `boolean` com `CAST(DadValor.boolean AS INT)` e `texto` com `CAST(DadValor.texto AS VARCHAR(MAX))`, porque o SQL Server recusa `bit` e `TEXT` em `MAX`.
Receita: [pivô de campos](../receitas/pivo-de-campos.md)

#### R-dados-adicionais-05: Para campo de lista, leia os itens em `DadValorDominio`, o rótulo em `DadDominio.dsDom`, e conte requisições com `COUNT(DISTINCT idQQ)`. {#r-dados-adicionais-05}
Um valor de lista pode ter vários itens (várias linhas por `idDadVal`), e uma requisição com dois itens conta em cada um deles; a soma das contagens por item pode passar do número de requisições.
Receita: [distribuição de um campo de lista](../receitas/distribuicao-campo-lista.md)

#### R-dados-adicionais-06: Os valores gravados permanecem depois que o contexto é desativado. {#r-dados-adicionais-06}
`DadContextoCampo.flgContextoAtivo` diz se o contexto está ativo para novos preenchimentos, e `DadoAdicional.flgDadAtivo` diz se o campo está ativo no cadastro; são colunas diferentes, em tabelas diferentes. O valor continua gravado depois que o contexto é desativado (o produto mostra "inativos com valor já gravado"). Para a pergunta "o campo está disponível para preencher hoje", o produto combina três condições: `DadContextoCampo.flgContextoAtivo = 1`, `DadoAdicional.flgDisponivel = 1` e, quando há `idCon`, `DadConjunto.flgDisponivel = 1`.
Receita: [formulários que usam um campo](../receitas/formularios-que-usam-campo.md)

#### R-dados-adicionais-07: Use `flgAgenda = 0` para o valor de requisição. {#r-dados-adicionais-07}
`flgAgenda = 1` indica valor de agenda de requisição. A pesquisa de requisições do produto junta `DadValor` com `flgAgenda = 0`.
Receita: [valores de um campo](../receitas/valores-de-um-campo.md)

#### R-dados-adicionais-08: Trate `nSeq` como parte da chave do valor. {#r-dados-adicionais-08}
Num conjunto múltiplo, cada repetição tem seu `nSeq`. Para uma linha por requisição, filtre `nSeq = 1` (as repetições ficam de fora) ou agrupe por `idQQ` e `nSeq`; campos de conjuntos diferentes pedem um pivô por conjunto (`DadContextoCampo.idCon`).
Receita: [pivô de campos](../receitas/pivo-de-campos.md)

#### R-dados-adicionais-09: No pivô, confira a contagem de contextos de cada campo. {#r-dados-adicionais-09}
Quando o mesmo campo tem valores em contextos diferentes (`idDadCon`) da mesma requisição, valem todos, um por contexto (decisão do produto). O pivô devolve, para cada campo, uma coluna com a contagem de contextos, e o valor mostrado é o maior entre os contextos quando a contagem passa de 1; para ver cada valor, use a receita de valores de um campo.
Receita: [pivô de campos](../receitas/pivo-de-campos.md)

#### R-dados-adicionais-10: Para os formulários de um campo, combine o escopo do contexto com o formulário das requisições que têm valor. {#r-dados-adicionais-10}
Um contexto de formulário (`idFrm` preenchido) aponta direto para o formulário; contextos de atividade, subcategoria, categoria e área valem para a classificação, e o formulário aparece no `idFrm` das requisições que têm valor. Em valores de contexto de formulário, o `idFrm` do contexto pode diferir do `idFrm` da requisição; a receita traz os dois e a página não decide qual vale.
Receita: [formulários que usam um campo](../receitas/formularios-que-usam-campo.md)

## 7. Views recomendadas

Esta página parte das tabelas; nenhuma view é recomendada aqui.

## 8. Receitas

- [Valores de um campo](../receitas/valores-de-um-campo.md)
- [Pivô de campos](../receitas/pivo-de-campos.md)
- [Distribuição de um campo de lista](../receitas/distribuicao-campo-lista.md)
- [Formulários que usam um campo](../receitas/formularios-que-usam-campo.md)

## Veja também

- [Fato: requisição](requisicao.md)
- [Abertas e encerradas](../mapa/abertas-e-encerradas.md)
