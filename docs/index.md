# Bdesk: Dados

Documentação do banco de dados do Bdesk para engenheiros de dados. Aqui você encontra o modelo, as regras de leitura de cada tabela e receitas de SQL prontas para montar indicadores, seja qual for a sua ferramenta de consumo: consulta direta ou réplica, pipeline para um lakehouse ou carga para um data warehouse.

## O que você quer fazer?

| Objetivo | Página |
|---|---|
| **Medir SLA:** percentual no prazo, fora do prazo e requisições atrasadas agora | Regras: [estourou o prazo (R-marcos-02)](fatos/marcos.md#r-marcos-02), [o "agora" da carga (R-marcos-07)](fatos/marcos.md#r-marcos-07), [prazo em minutos de calendário (R-prioridade-sla-04)](dimensoes/prioridade-sla.md#r-prioridade-sla-04) e [calendário do grupo (R-tempo-calendario-01)](dimensoes/tempo-calendario.md#r-tempo-calendario-01). Receitas: [SLA por grupo](receitas/sla-por-grupo.md), [fora do SLA por prioridade](receitas/fora-do-sla-por-prioridade.md) e [atrasadas agora](receitas/atrasadas-agora.md). Contexto: [calendário e tempos](consumo/calendario-e-tempos.md) |
| Entender o modelo antes de começar | [O modelo em 5 minutos](comece-aqui/modelo-em-5-minutos.md) |
| Evitar os erros que mais distorcem os números | [Regras de ouro](comece-aqui/regras-de-ouro.md) e [regras essenciais](mapa/regras-essenciais.md) |
| Montar uma carga incremental no seu pipeline | [Carga incremental](consumo/carga-incremental.md) |
| Calcular minutos de calendário fora do banco | [Calendário e tempos](consumo/calendario-e-tempos.md) |
| Ler o banco sem atrapalhar a operação | [Acesso e leitura](consumo/acesso-e-leitura.md) |
| Adaptar uma receita para outro motor de SQL | [Traduzindo as receitas](consumo/traduzindo-as-receitas.md) |
| Medir volume de requisições | [Volume por mês](receitas/volume-por-mes.md), [por canal](receitas/volume-por-canal.md) e [por classificação](receitas/volume-por-classificacao.md) |
| Medir tempos de atendimento | [Tempo até a primeira resposta](receitas/tempo-ate-primeira-resposta.md), [tempo de atendimento por grupo](receitas/tempo-atendimento-por-grupo.md) e [tempo total por requisição](receitas/tempo-total-por-requisicao.md) |
| Achar uma tabela, uma coluna ou um termo de tela | [Dicionário de dados](dicionario/index.md), [busca](busca.md) e [glossário](glossario-tela-banco.md) |
| Saber o que ainda não está documentado | [Limitações conhecidas](limitacoes-conhecidas.md) e [versão da documentação](sobre/versao.md) |

## Como ler os avisos

!!! note "Selos do dicionário e o aviso Em revisão"
    Cada tabela e view do [dicionário](dicionario/index.md) tem um selo. **Explicada** quer dizer que uma página de fato, de dimensão ou do modelo descreve o significado dela. **Citada** quer dizer que ela aparece em receitas ou páginas de referência, mas não tem página de negócio própria. **Só estrutura** traz só as colunas e os tipos: não deduza o significado pelo nome da coluna.

    Uma receita com o aviso **Em revisão** ainda não teve a definição verificada por completo: use-a com cautela e confira os resultados. O mesmo rótulo ao lado do título de uma regra indica uma regra ainda em revisão.
