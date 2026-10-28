---
gerado: sincronizacao
---
# Fora de escopo: CRM (contratos e faturamento)


**O que é.** O cadastro comercial de empresas, contratos e itens de contrato, com o cálculo de faturamento sobre as horas apontadas nas requisições. Esta documentação do banco não detalha o domínio.

## Tabelas principais

| Tabela | Papel |
|---|---|
| `CRM_Empresa` | empresa do CRM (`idEmp`, `nmEmp`, `idEmpCliente`, `idGruEmp`, `idSeg`) |
| `CRM_Contrato`, `CRM_ContratoItem`, `CRM_ContratoDoc` | contrato, seus itens e documentos (`CRM_ContratoItem.idContrato` tem FK para `CRM_Contrato`) |
| `CRM_Faturamento` | fechamento de faturamento (`idFat`, `idItemContrato`, `valFatTotal`) |
| `CRM_ApontCalc` | cálculo por apontamento: `idReq`, `idSeq`, `idFat`, `idItemContrato`, horas e valores |
| `CRM_Contato`, `CRM_Gestor`, `CRM_Unidade`, `CRM_Segmento`, `CRM_Produto`, `CRM_GrupoEmpresarial` | cadastros de apoio |


## Onde toca a requisição

- `CRM_ApontCalc` liga-se ao apontamento de horas da requisição pelo par (`idReq`, `idSeq`) e ao faturamento (`CRM_Faturamento`) por `idFat`. O banco não traz FK de `CRM_ApontCalc` para `Req`; as FKs da tabela vão para `CRM_ContratoItem` e `CRM_Faturamento`.
- `Req.idEmp` tem FK para `Empresa.idEmp`, a tabela de empresas do cadastro geral, que é outra tabela que `CRM_Empresa`. O produto relaciona as duas por `CRM_Empresa.idEmpCliente = Empresa.idEmp`.

## Veja também

[Requisição](../fatos/requisicao.md) · [Pessoa e organização](../dimensoes/pessoa-organizacao.md) · [Índice](../busca.md)
