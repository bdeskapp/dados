---
gerado: sincronizacao
---
# Fora de escopo: base de conhecimento


**O que é.** Os artigos e perguntas frequentes que o usuário consulta, e as soluções de conhecimento ligadas às requisições. Esta documentação do banco não detalha o domínio.

## Tabelas principais

| Tabela | Papel |
|---|---|
| `Conteudo` | artigo ou FAQ do portal (`Titulo`, `Corpo`, `EhFaq`, `Ativo`, `Categoria_id`) |
| `ConteudoCategoria`, `Tag`, `Tag_Conteudo`, `Conteudo_Relacionados` | categoria, etiquetas e relacionamentos dos conteúdos |
| `KBase` | base de conhecimento (`idKB`, `nmKB`, `dsKB`, `idReqOrigem`) |
| `ReqKB`, `ReqKBConcluida` | conhecimento aplicado a uma requisição aberta e a uma encerrada |

A tabela `ConteudoCategoria` é a categoria de conteúdo; a classificação de requisição é a tabela `Categoria` ([classificação](../dimensoes/classificacao.md)).


## Onde toca a requisição

- `ReqKB.idReq` tem FK para `Req` e `ReqKB.idKB` para `KBase`; `ReqKBConcluida` tem as FKs equivalentes para `ReqConcluida` e `KBase`.
- `KBase.idReqOrigem` é uma coluna com a requisição de origem do conhecimento.
- `Conteudo` e as tabelas do portal não têm coluna de requisição nem FK para `Req`.

## Veja também

[Requisição](../fatos/requisicao.md) · [Abertas e encerradas](../mapa/abertas-e-encerradas.md) · [Índice](../busca.md)
