---
gerado: sincronizacao
---
# Fora de escopo: CMDB (itens de configuração e patrimônio)


**O que é.** O cadastro de itens de configuração (ICs), também chamados de patrimônio: equipamentos, licenças e seus relacionamentos e movimentos. Esta documentação do banco não detalha o domínio.

## Tabelas principais

| Tabela | Papel |
|---|---|
| `Patrimonio` | o item (`idPat`, `idTpp`, `nmPat`, `idStatusPat`, `idUsuResp`, `idLoc`) |
| `TipoPatrimonio` | o tipo do item (`idTpp`, `dsTpp`) |
| `StatusPatrimonio` | o status do item (`idStatusPat`, `dsStatusPat`) |
| `PatMovimento` | o histórico de movimentos do item (`idPat`, `idStatusAnt`, `idStatusAtual`, `idReq`) |
| `PatrimonioAssociado` | relação entre itens (`idPat`, `idPatAss`, `idPatRel`) |
| `ListaIC`, `ListaICUsuario`, `ListaICClasseTipo` | listas de ICs usadas para papéis relacionados e atribuição a usuários |
| `PatrimonioSolicitacao`, `PatrimonioAtributoSolicitacao`, `PatrimonioAssociadoSolicitacao` (e as variantes `...Temp`) | dados de IC capturados em uma solicitação, com `idReq` |


## Onde toca a requisição

- `Req.idPat` tem FK para `Patrimonio.idPat`: o IC ao qual a requisição se refere.
- `PatMovimento.idReq`, `PatAlerta.idReq`, `PatrimonioSolicitacao.idReq` e `PatrimonioAtributoSolicitacao.idReq` guardam a requisição como coluna; essas colunas não têm FK para `Req` no banco.
- `ListaIC` liga-se ao formulário por `FormPapelRelacionado.idListaIC`.

## Veja também

[Requisição](../fatos/requisicao.md) · [Índice](../busca.md)
