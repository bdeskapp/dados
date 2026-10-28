# Traduzindo as receitas

As receitas estão escritas em T-SQL, o SQL do SQL Server, compatível com o nível 130. Esta página explica como uma receita é montada e o que cada padrão recorrente significa, para você levar a mesma conta para o motor de SQL do seu destino, para o seu pipeline ou para a linguagem de transformação que você usa.

## Anatomia de uma receita

Toda receita tem as mesmas seções, nesta ordem. Veja, por exemplo, [SLA por grupo](../receitas/sla-por-grupo.md):

1. **Pergunta e indicador.** A pergunta de negócio e a fórmula do indicador, com numerador, denominador e recorte.
2. **Definição usada.** As escolhas que mudam o número: o que conta como "no prazo", se as canceladas entram, qual grupo é usado. Quando a definição vem do produto, o texto diz "decisão do produto".
3. **SQL.** A consulta, precedida de uma nota sobre parâmetros e compatibilidade, e seguida da granularidade do resultado (uma linha por quê).
4. **Exemplo de resultado.** Uma tabela fictícia com o formato da saída.
5. **Regras aplicadas.** As regras `R-…` que a receita segue. Ao adaptar a receita, preserve essas regras: são elas que garantem o mesmo número.

Uma receita com o aviso **Em revisão** ainda não teve a definição verificada por completo; confira os resultados antes de usá-la num indicador oficial.

!!! tip "Traduza a definição, não só o SQL"
    Se o seu número não bater com o da receita, compare primeiro a seção "Definição usada" e as regras aplicadas. A diferença costuma estar no recorte, por exemplo canceladas ou abertas sem status, e não na sintaxe.

## Abertas mais encerradas: `UNION ALL`

Muitas receitas leem a tabela das abertas e a das encerradas e juntam as duas com `UNION ALL`, às vezes com uma coluna que diz de qual lado veio a linha. A junção é necessária porque cada requisição está em uma só das duas tabelas ([R-requisicao-01](../fatos/requisicao.md#r-requisicao-01) e [R-tempo-requisicao-01](../fatos/tempo-requisicao.md#r-tempo-requisicao-01)).

Como levar para outro motor:

- Use a união que **mantém todas as linhas**, sem eliminar repetições. A união com eliminação de repetições pode apagar linhas legítimas, como duas passagens iguais pelo mesmo status.
- Os dois ramos precisam ter as mesmas colunas, na mesma ordem e com tipos compatíveis. Colunas que só existem de um lado entram como vazias no outro.
- Se você já guarda as duas partes no destino, a união pode virar uma única tabela com a coluna de origem. Mantenha a coluna: o estado da requisição é a tabela de origem ([R-requisicao-02](../fatos/requisicao.md#r-requisicao-02)).

## Divisão: `CAST` para decimal

No SQL Server, a divisão entre dois inteiros devolve um inteiro e descarta a parte fracionária: 180 dividido por 200 dá 0. Por isso as receitas de proporção convertem o numerador para decimal antes de dividir, e convertem o resultado de novo para fixar as casas decimais, como em [SLA por grupo](../receitas/sla-por-grupo.md). Pelo mesmo motivo, as médias convertem o valor para um tipo fracionário antes de calcular, e as somas de minutos convertem para um inteiro maior, para evitar estouro, como em [tempo em cada status](../receitas/tempo-em-cada-status.md).

Como levar para outro motor:

- Confira como o seu motor divide inteiros. Alguns devolvem fração, outros truncam como o SQL Server.
- Converta explicitamente sempre que o resultado precisar de fração, mesmo que o seu motor não exija.
- Arredonde só no final, com o mesmo número de casas da receita, para comparar os resultados.
- A proporção da receita vai de 0 a 1. Multiplique por cem só na apresentação.

## Texto de tamanho fixo: `RTRIM` em `CHAR`

Colunas do tipo `CHAR` têm tamanho fixo e são completadas com espaços à direita. O código de vínculo, por exemplo, é `CHAR(5)` e é lido com `RTRIM` ([R-vinculos-03](../fatos/vinculos.md#r-vinculos-03)). O SQL Server ignora esses espaços na comparação com `=`, mas muitos motores e linguagens não ignoram: depois de copiado, `'REF  '` deixa de ser igual a `'REF'`.

Como levar para outro motor:

- Remova os espaços à direita das colunas `CHAR` na extração, ou antes de qualquer comparação ou agrupamento.
- O tipo de cada coluna está no [dicionário de dados](../dicionario/index.md).

## Contagem de requisições: `COUNT(DISTINCT)`

Quando a tabela tem mais de uma linha por requisição, como passagens por status ou participações, a receita conta linhas com `COUNT(*)` e requisições com `COUNT(DISTINCT idReq)` ([R-tempo-por-status-02](../fatos/tempo-por-status.md#r-tempo-por-status-02) e [R-participacao-06](../fatos/participacao.md#r-participacao-06)).

Como levar para outro motor:

- Use a contagem distinta **exata**. Alguns motores oferecem uma contagem distinta aproximada, mais rápida, que não serve para indicador oficial.
- A contagem distinta não pode ser somada entre grupos: a soma das requisições de cada status pode passar do total de requisições, porque a mesma requisição passa por vários status. Para um total, conte de novo sobre o conjunto inteiro.

## Parâmetros: o comentário com o valor 0

As receitas trazem cada parâmetro como um comentário com o nome dele seguido do valor provisório `0`, como neste filtro de [SLA por grupo](../receitas/sla-por-grupo.md):

```sql
SELECT c.idReq
FROM ReqConcluida c
WHERE c.dtFimReal >= /* @dtInicio */ 0 AND c.dtFimReal < /* @dtFim */ 0;
```

O `0` só existe para a consulta compilar. Substitua cada um pelo valor real antes de rodar: com `0`, um filtro de data devolve vazio, porque o SQL Server lê o número 0 como a data de 1º de janeiro de 1900.

Como levar para outro motor:

- Troque cada placeholder pelo mecanismo de parâmetro da sua ferramenta de consumo ou do seu pipeline. Não concatene valores no texto da consulta.
- Nos filtros de período, mantenha o intervalo aberto no fim: maior ou igual ao início e menor que o fim.

## Outros padrões frequentes

| Na receita | O que significa | No seu motor |
|---|---|---|
| `GETDATE()` | data e hora do servidor de banco no momento da consulta | troque por um horário de carga capturado uma vez e gravado no resultado ([R-marcos-07](../fatos/marcos.md#r-marcos-07); veja [acesso e leitura](acesso-e-leitura.md)) |
| `WITH(NOLOCK)` | leitura sem esperar por bloqueios, específica do SQL Server | remova; veja [acesso e leitura](acesso-e-leitura.md#o-que-withnolock-significa) |
| `LEFT JOIN` no status, na atividade e no grupo | mantém as requisições em que a ligação está vazia | mantenha a junção externa; a junção interna muda a contagem ([R-status-fase-02](../dimensoes/status-fase.md#r-status-fase-02) e [R-requisicao-04](../fatos/requisicao.md#r-requisicao-04)) |
| `ISNULL(s.cdSta, '') <> 'CL'` | exclui as canceladas e mantém as requisições sem status | use a função de valor padrão do seu motor; sem ela, a comparação com vazio exclui as requisições sem status ([R-status-fase-04](../dimensoes/status-fase.md#r-status-fase-04)) |
| `DATEDIFF(mi, início, fim)` | minutos corridos entre duas datas, contados pelas viradas de minuto | confira como o seu motor calcula a diferença; alguns contam o tempo decorrido e descartam os segundos incompletos, e o resultado pode diferir em 1 minuto |
| colunas terminadas em `Cal` | minutos do calendário do grupo, gravados pelo produto | leia como estão; para refazer a conta, veja [calendário e tempos](calendario-e-tempos.md) ([R-tempo-requisicao-03](../fatos/tempo-requisicao.md#r-tempo-requisicao-03)) |
