# Acesso e leitura

Esta página trata de como ler o banco do Bdesk sem atrapalhar quem usa o produto e sem distorcer o resultado. Ela vale para a consulta direta, para a réplica e para a extração de um pipeline.

## Usuário só de leitura

Peça ao administrador da instalação um usuário de banco **só de leitura**, exclusivo para a extração de dados. Com ele:

- nenhuma consulta sua altera dados do produto, nem por engano;
- o administrador consegue identificar e limitar a carga que vem da extração;
- você não precisa de nenhuma permissão de escrita: as receitas desta documentação só leem.

## Réplica

Sempre que possível, leia de uma **réplica** do banco, e não do banco que atende o produto. A réplica recebe as mesmas tabelas e isola as consultas pesadas da operação. Combine com o administrador:

- o atraso típico da réplica em relação ao banco principal, que passa a fazer parte da defasagem dos seus números;
- o fuso dos servidores, porque as datas são gravadas em hora local, sem fuso, por dois relógios: o do servidor que executa o produto e o do servidor de banco ([R-marcos-06](../fatos/marcos.md#r-marcos-06)). A regra traz a consulta que mostra se os dois coincidem.

!!! note "Na réplica, o 'agora' é o do servidor da réplica"
    Numa réplica atrasada, a data e hora do servidor no momento da consulta podem estar à frente dos dados replicados. Leve isso em conta ao medir atraso nas abertas (veja a seção sobre o horário da carga, abaixo).

## O que `WITH(NOLOCK)` significa

As receitas escrevem `WITH(NOLOCK)` depois de cada tabela. No SQL Server, essa dica faz a consulta ler sem esperar por bloqueios, no nível de isolamento de leitura não confirmada. A consulta não trava quem está gravando, e quem está gravando não trava a consulta. O preço é a consistência:

- a consulta pode ler uma alteração que ainda não foi confirmada e que depois é desfeita;
- durante gravações intensas, a mesma linha pode ser lida duas vezes ou ser pulada.

### Abertas e encerradas na mesma consulta

O encerramento copia a requisição para `ReqConcluida` e apaga a de `Req` numa só transação ([R-abertas-e-encerradas-02](../mapa/abertas-e-encerradas.md#r-abertas-e-encerradas-02)). Isso não basta para um corte consistente:

- **Com `WITH(NOLOCK)`**, a consulta pode ver a requisição nas duas tabelas ou pular a linha.
- **Sem a dica**, no isolamento padrão do SQL Server (leitura confirmada), cada tabela de um `UNION ALL` de `Req` e `ReqConcluida` é lida num momento diferente. Uma requisição encerrada durante a consulta pode ser contada em dobro ou ficar de fora.

Por isso, deduplique sempre por `idReq`, com a linha de `ReqConcluida` prevalecendo, como em [carga incremental](carga-incremental.md#chaves-de-deduplicacao). Para um corte consistente, leia as duas tabelas no mesmo snapshot: use o isolamento SNAPSHOT, se o administrador o tiver habilitado no banco, ou leia de uma cópia que não muda durante a leitura, como um snapshot do banco ou uma réplica com a aplicação das alterações pausada.

### Quando remover

- **Fora do SQL Server.** Se você roda a receita em outro motor, sobre os dados já copiados, remova a dica: ela é específica do SQL Server.
- **Em números que precisam fechar.** Para um fechamento de período ou uma conciliação, remova a dica, para que a consulta leia só dados confirmados, e leia no mesmo snapshot, como descrito acima.
- **Quando o banco já lê versões confirmadas.** Se o administrador informar que o banco ou a réplica usa leitura por versão de linha, a consulta sem a dica já não trava quem grava; nesse caso a dica só traz o risco descrito acima.

Mantenha a dica quando a consulta roda no banco do produto em horário de uso e um número aproximado basta, como num painel de acompanhamento.

## O horário da carga: `GETDATE()`

As receitas de abertas comparam o prazo com `GETDATE()`, a data e hora do servidor de banco no momento em que a consulta roda ([R-marcos-07](../fatos/marcos.md#r-marcos-07)). Num pipeline, esse momento é o horário da carga. "Atrasada agora" e "no prazo" valem para aquele instante, e duas cargas dos mesmos dados dão resultados diferentes.

Faça assim:

1. Leia a data e hora do servidor **uma vez**, no início da carga, e guarde o valor numa variável.
2. Use essa variável no lugar de `GETDATE()` em todas as consultas da carga, para que todas falem do mesmo instante.
3. Grave o valor numa coluna do resultado.
4. No destino, recalcule o atraso a partir dessa coluna, e não do relógio da sua ferramenta, que pode estar em outro fuso ([R-marcos-06](../fatos/marcos.md#r-marcos-06)).

!!! note "O prazo e o horário da carga vêm de relógios diferentes"
    O prazo calculado na abertura parte do relógio do servidor que executa o produto, e o horário da carga lido no banco vem do relógio do servidor de banco. Se os dois relógios diferem, o corte entre "atrasada" e "no prazo" se desloca pela mesma diferença ([R-marcos-07](../fatos/marcos.md#r-marcos-07) e [R-marcos-06](../fatos/marcos.md#r-marcos-06)).

```sql
DECLARE @agora DATETIME = GETDATE();

SELECT r.idReq, r.dtFimPrev, @agora AS dt_carga,
       CASE WHEN r.dtFimPrev < @agora THEN 1 ELSE 0 END AS atrasada
FROM Req r WITH(NOLOCK);
```

Os tempos gravados das abertas são de outro instante, o do último cálculo (`dtCalc`). Grave `dtCalc` também e meça a defasagem de cada linha como o horário da carga menos `dtCalc` ([R-tempo-requisicao-07](../fatos/tempo-requisicao.md#r-tempo-requisicao-07)).

## Consultas pesadas

As tabelas de requisição, de histórico e de participação crescem com o uso do produto, e as encerradas acumulam todos os anos de operação. Para não pesar no banco:

- **Selecione só as colunas de que você precisa.** Evite `SELECT *`, principalmente em tabelas com colunas de texto longo e em tabelas de pessoas ([R-pessoa-organizacao-07](../dimensoes/pessoa-organizacao.md#r-pessoa-organizacao-07)).
- **Filtre por intervalo de datas aberto no fim**, como `>= início` e `< fim`, e não aplique funções sobre a coluna filtrada. Assim o banco pode usar índices.
- **Divida as cargas completas em faixas** de `idReq` ou de período, em vez de uma única consulta sobre todo o histórico.
- **Agende as cargas completas** para horários de pouco uso do produto, de preferência na réplica.
- **Prefira as receitas de abertas para o acompanhamento frequente.** As abertas são uma fração do total; as encerradas podem ser lidas com menos frequência, conforme a [janela de reprocessamento](carga-incremental.md#janela-de-reprocessamento).
