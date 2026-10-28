---
gerado: sincronizacao
---

# dbo.DadContextoCampo

**Selo:** Explicada

Explicada em:

- [dados adicionais](../fatos/dados-adicionais.md)

## Colunas

| Coluna | Tipo | Aceita nulo | Chave primária | Calculada |
|---|---|---|---|---|
| `idDadCon` | INT | não | sim | não |
| `idEnt` | INT | não | não | não |
| `idDad` | INT | não | não | não |
| `idCon` | INT | sim | não | não |
| `idFrm` | INT | sim | não | não |
| `idAre` | INT | sim | não | não |
| `idCat` | INT | sim | não | não |
| `idSca` | INT | sim | não | não |
| `idTar` | INT | sim | não | não |
| `nOrdem` | SMALLINT | não | não | não |
| `flgObrigatorio` | BIT | não | não | não |
| `flgContextoAtivo` | BIT | não | não | não |
| `flgEditavelConclusao` | BIT | não | não | não |

## Chaves estrangeiras

- `dbo.CondDadAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.CondDadDominioAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.CondDad` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadContextoAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadContextoCampoEditabilidade` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadContextoCampo` (idAre) → `dbo.Area` (idAre)
- `dbo.DadContextoCampo` (idCat) → `dbo.Categoria` (idCat)
- `dbo.DadContextoCampo` (idCon) → `dbo.DadConjunto` (idCon)
- `dbo.DadContextoCampo` (idEnt) → `dbo.DadEntidade` (idEnt)
- `dbo.DadContextoCampo` (idDad) → `dbo.DadoAdicional` (idDad)
- `dbo.DadContextoCampo` (idFrm) → `dbo.Formulario` (idFrm)
- `dbo.DadContextoCampo` (idSca) → `dbo.SubCategoria` (idSca)
- `dbo.DadContextoCampo` (idTar) → `dbo.Tarefa` (idTar)
- `dbo.DadContextoDesd` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadContextoVinc` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadDefault` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadDomTabDefault` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadDominioDefault` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadFormAcao` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadFormPapelStatus` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadProcesso` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadRelacionamento` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadRelacionamento` (idDadConRel) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.DadValor` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.FormPapelObrigatorioDadoAdicional` (idDadCon) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.RelacaoAtribuicao` (idDadConOrigem) → `dbo.DadContextoCampo` (idDadCon)
- `dbo.RelacaoAtribuicao` (idDadConDestino) → `dbo.DadContextoCampo` (idDadCon)
