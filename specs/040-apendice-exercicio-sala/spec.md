# Spec 040 — Apêndice D: o método do autor em sala (exercício do carro)

- **Status**: Aprovada (ditado ao vivo pelo Steward, passo a passo) · **Raia**:
  Plena · **Data**: 2026-08-14
- **O quê**: consolidar em apêndice o exercício conduzido em sala — a escolha de um
  carro popular zero, do enunciado à recomendação — junto com o **método de oito
  passos** do autor e a explicação de cada um. Nasce a etapa 15 (`15-criterizacao`)
  com o motor puro do método e 20 testes que reproduzem todos os números.
- **Conteúdo**: passos 1–8 (definir o problema · alternativas · atributos · ir a
  campo · criterização · ponderação · medida resumo · sensibilidade); três formas de
  criterizar (de-para, interpolação com o "I" do quadro, fórmula do máximo); pesos
  por grafo de dominância com autodominância; resultado (Mobi 7,87 > Onix 7,59 >
  Kwid 6,69 > 208 5,44) e as três descobertas de sensibilidade.
- **Achados registrados** (o que o exercício produziu e não estava nos capítulos):
  1. **Regra do piso levantado** — ancore no zero real quando ele existir e a faixa
     for larga; levante o piso quando o intervalo observado for estreito demais
     para justificar a régua inteira.
  2. **Influência efetiva = peso × amplitude** — a Segurança foi declarada o 2º
     critério e exerce o 4º (9,5%), porque sua coluna varia só de 7,86 a 10,00.
  3. **A criterização é decisão de peso disfarçada** — o piso 4 da Confiança decide
     o vencedor: com 10/5/0 o Onix passa o Mobi por 0,011.
- **Constitution Check**: I ✅ (todo número do apêndice é fixture — `20 passed`) ·
  II ✅ (motor puro, sem I/O) · III ✅ (esqueleto adaptado a apêndice; verificação +
  gabarito) · IV ✅ (edição 0.40; captura 2026-08) · V ✅ · VI ✅ (nenhum método
  apresentado como "o melhor"; a compensação da soma ponderada é explicitada e
  contrastada com o veto do cap. 09) · VII ✅ · **VIII ⚠ parcial**: a seção "De onde
  isto veio" está **deliberadamente incompleta** — o autor declarou que indicará
  depois de onde adaptou cada passo. O que está escrito é leitura editorial (📖) do
  parentesco com os caps. 02/03/04/07/11, explicitamente marcada como tal, sem
  nenhuma atribuição em nome do autor. **Pendência registrada, não escondida.**
- **DoD**: [x] etapa 15 `20 passed` · [x] mkdocs --strict · [x] apêndice no nav ·
  [x] HISTORICO 0.40 + CHANGELOG · [ ] rodada de proveniência com o autor ·
  [ ] gate do autor.
