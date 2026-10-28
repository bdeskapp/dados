---
gerado: sincronizacao
---
# Fora de escopo: push e notificações


**O que é.** Notificações em tela (sino) e web push (VAPID) enviadas aos usuários quando uma ação acontece na requisição ou quando um alerta de prazo dispara. Esta documentação do banco não detalha o domínio.

## Tabelas principais

| Tabela | Papel |
|---|---|
| `Notificacao` | a mensagem a entregar; guarda o destinatário (`idUsu`), a requisição (`idReq`) e o estado do envio por push (`dtEnvioPush`, `dsErroPush`, `nTentativasPush`, `dtResumoPush`) |
| `PushSubscription` | assinatura de push de um usuário em um sistema (`idUsu`, `dsSistema`, `flgAtivo`) |
| `Dispositivo` | tabela legada de tokens de dispositivo |
| `FormNotificacao`, `FormNotificacaoAlerta`, `FormNotMensagem`, `TipoNotificacao` | configuração por formulário que decide se uma notificação existe (`Notificacao.idFrmNot` e `Notificacao.idFrmNotAlerta` apontam para elas) |


## Onde toca a requisição

- `Notificacao.idReq` guarda a requisição da notificação. A coluna não tem chave estrangeira no banco; a linha é gravada pelo produto quando uma ação acontece na requisição e pela rotina de alerta de prazo.
- `Notificacao.idFrmAcao` leva à ação do formulário; ver [ação](../dimensoes/acao.md).
- Como a coluna `idReq` é sem FK, a ligação entre `Notificacao` e a requisição aberta ou encerrada se faz por `idReq` nas duas tabelas ([abertas e encerradas](../mapa/abertas-e-encerradas.md)).

## Veja também

[Requisição](../fatos/requisicao.md) · [Índice](../busca.md)
