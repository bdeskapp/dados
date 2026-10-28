---
gerado: sincronizacao
---
# Glossário: termo na tela e coluna no banco


Cada linha liga um **rótulo fixo do produto** à coluna que o alimenta. Só entram termos cujo caminho da tela até a coluna foi conferido no código. Quando a tela trata o valor antes de mostrá-lo, a coluna `tabela.coluna` diz como. Nesta entrega o glossário cobre só a tela clássica; os rótulos do portal e do app ficam para uma próxima onda (decisão do produto), e as telas mais antigas do produto seguem fora.

## Fora do glossário

Os rótulos que o cliente configura vêm do formulário e variam de uma instalação para outra: o nome da ação (`FormAcao.dsAcao`), o nome do papel (`FormPapel.dsPapel`) e o texto do status (`FormStatus.dsSta`). Esses textos aparecem nas telas, e a página [ação](dimensoes/acao.md), a página [papéis e participação](mapa/papeis-e-participacao.md) e a página [status e fase](dimensoes/status-fase.md) dizem de onde cada um vem.

## Lista de requisições (tela "Lista de requisições")


| termo na tela | onde aparece | tabela.coluna | página |
|---|---|---|---|
| Requisição (número no item da lista) | dica "Requisição: n" do item | `Req.idReq` (`ReqConcluida.idReq` nas encerradas) | [requisição](fatos/requisicao.md) |
| Assunto | título do item e dica "Assunto:" | `Req.dsTitulo` (`ReqConcluida.dsTitulo` nas encerradas). A tela mostra o título com as quebras de linha, as tabulações e os espaços não separáveis trocados por espaço, e sem espaços nas pontas | [requisição](fatos/requisicao.md) |
| Classificação (categoria - subcategoria - atividade) | linha pequena do item (subcategoria-atividade) e dica "Classificação:", três valores separados por " - " | `Tarefa.dsTar` (atividade), `Categoria.dsCat`, `SubCategoria.dsSca`, alcançadas por `Req.idTar` (`ReqConcluida.idTar` nas encerradas) → `Tarefa.idCat` e `Tarefa.idSca`. Nas encerradas, a tela mostra o nome atual da atividade, da categoria e da subcategoria, e não o retrato gravado em `ReqConcluida` no encerramento; ver [R-classificacao-03](dimensoes/classificacao.md) | [classificação](dimensoes/classificacao.md) |
| Término previsto | dica do relógio no item | `Req.dtFimPrev` (`ReqConcluida.dtFimPrev`) | [marcos](fatos/marcos.md) |
| Anexos | contador com clipe | linhas de `ReqDocumento` (aberta) ou de `ReqDocConcluida` (encerrada) | [abertas e encerradas](mapa/abertas-e-encerradas.md) |
| Registros | contador de balão | linhas de `ReqHistorico` (aberta) ou de `ReqHistConcluida` (encerrada), contadas após um filtro por `tpRegistro` e `flgPublico` e pelo acesso do usuário logado a cada registro; o número da tela depende do usuário e não se reproduz sem ele | [eventos do histórico](fatos/eventos-historico.md) |

## Filtros da coluna de filtros


| termo na tela | onde aparece | tabela.coluna | página |
|---|---|---|---|
| Grupos Solucionadores | opção "Filtrar por" | `Req.idGruAtual` | [grupo e área](dimensoes/grupo-area.md) |
| Prioridade | opção "Filtrar por" | `Req.nPrioridade` | [prioridade e SLA](dimensoes/prioridade-sla.md) |
| Rotinas | opção "Filtrar por" | `Req.idFrm`, o formulário da requisição | [requisição](fatos/requisicao.md) |

O filtro "Status" compara o texto do status com `FormStatus.dsSta`, que é rótulo do formulário e fica na seção "Fora do glossário".

## Detalhe da requisição (painel da requisição)


| termo na tela | onde aparece | tabela.coluna | página |
|---|---|---|---|
| Abertura | rótulo no bloco de datas | `Req.dtAbertura` (`ReqConcluida.dtAbertura`) | [requisição](fatos/requisicao.md) |
| Início Previsto | rótulo no bloco de datas | `Req.dtIniPrev` (`ReqConcluida.dtIniPrev`) | [marcos](fatos/marcos.md) |
| Fim Previsto | rótulo no bloco de datas | `Req.dtFimPrev` (`ReqConcluida.dtFimPrev`) | [marcos](fatos/marcos.md) |

## Veja também

[Requisição](fatos/requisicao.md) · [Classificação](dimensoes/classificacao.md) · [Índice](busca.md)
