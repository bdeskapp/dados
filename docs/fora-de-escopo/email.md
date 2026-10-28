---
gerado: sincronizacao
---
# Fora de escopo: e-mail


**O que é.** O envio de e-mails do sistema e a leitura de caixas de entrada que abrem ou atualizam requisições a partir de mensagens recebidas. Esta documentação do banco não detalha o domínio.

## Tabelas principais

| Tabela | Papel |
|---|---|
| `EnvioEmail` | fila de e-mails a enviar (`EmailDestinatario`, `Assunto`, `Mensagem`, `nTentativas`, `dtEnvio`) |
| `SyncEmail` | e-mail recebido e seu processamento (`dsFrom`, `dsSubject`, `dtReceived`, `dtProcess`, `sStatus`, `dsErro`, `idReq`) |
| `SyncEmailConnect`, `SyncEmailAddress` | conexão e endereço de cada caixa lida |
| `SyncEmailConfig`, `SyncEmailNewReq`, `SyncEmailUpdateReq`, `SyncEmailNewReqCat`, `SyncEmailActionUpdate` | regras de abertura e de atualização de requisição por e-mail |


## Onde toca a requisição

- `SyncEmail.idReq` guarda a requisição criada ou atualizada pelo e-mail; o produto grava a coluna ao terminar o processamento. A coluna não tem FK para `Req` no banco.
- `SyncEmailNewReq.idFrm`, `idTar`, `idTpPapelAdo` e `idPartAdo` definem o formulário, a atividade e o solicitado das requisições abertas por e-mail.
- O código `E` de `Req.tpAgenteReg` marca a requisição aberta por e-mail ([canal de origem](../dimensoes/canal-origem.md)).
- `EnvioEmail` não tem coluna de requisição.

## Veja também

[Requisição](../fatos/requisicao.md) · [Canal de origem](../dimensoes/canal-origem.md) · [Índice](../busca.md)
