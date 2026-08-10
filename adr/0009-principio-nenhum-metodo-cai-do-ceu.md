# ADR 0009 — Princípio VIII: "Nenhum método cai do céu" (emenda constitucional)

- **Status**: Aceito · **Data**: 2026-08-10 · **Spec**: 030 · **Autoria da decisão**:
  Steward (texto do princípio fornecido integralmente pelo autor); operacionalização
  pelo agente.

## Contexto

O livro ensina onze métodos com fórmula, worked example e código — mas nenhum capítulo
conta **de onde o método veio**: quem estava preso em quê, contra o que o método
competia, qual ideia destravou. O autor diagnosticou o risco: capítulo sem história
entrega procedimento, e procedimento se decora — não se transfere. Pior: história é o
terreno mais fácil do livro para **inventar sem perceber**, porque atribuição plausível
com data errada passa em qualquer revisão apressada (e as ferramentas de busca devolvem
resumos, não fontes).

## Decisão

1. **Emenda constitucional** (v1.0.0 → v1.1.0, MINOR): entra o Princípio VIII,
   NÃO-NEGOCIÁVEL, com o texto do autor na íntegra — seção obrigatória "De onde isto
   veio" (5 elementos: aperto → o que se fazia antes → virada → ideia reaproveitável →
   nome) em todo capítulo de método, entre "O problema" e "Fundamentos"; selos
   obrigatórios por afirmação histórica (✓ · ✓ᵐ · ⏳ · ❌ · 📖) com tabela de fechamento;
   três proibições (gênio solitário, curiosidade decorativa, mistura de registro);
   pesquisa concentrada em sessão própria com nota + fila de verificação; duas
   armadilhas (resumo de busca não é fonte; ler acha o que não se sabia estar lá).
2. **Esqueleto v3 atualizado** (`livro/GUIA-EDITORIAL.md`): "De onde isto veio" vira o
   item 3 do esqueleto, obrigatório em capítulo de método (00/panoramas/infra omitem).
3. **Nota de pesquisa única** (`estudos/nota-pesquisa-historia-mcda.md`): produzida
   nesta sessão, cobre os métodos dos caps. 02–10, 12 e 14, termina com a fila de
   verificação. Regra de consumo: os capítulos afirmam **no máximo** o que o selo da
   nota autoriza.
4. **Calibração de selos**: o "✓" da `bibliografia.md` (URL/DOI verificado) equivale a
   **✓ᵐ** na régua do Princípio VIII. Os dois sistemas coexistem: bibliografia valida
   *existência/identidade* da obra; os selos do capítulo validam *afirmações* sobre o
   conteúdo e a história.

## Alternativas avaliadas

- **Guia editorial sem emenda constitucional** — rejeitada: regra só editorial não
  obriga as rodadas futuras nem protege contra a tentação de inventar história; o
  autor pediu força de constituição.
- **Pesquisar a história capítulo a capítulo** (dentro da spec de cada um) —
  rejeitada pelo processo do próprio princípio: as histórias se conectam (ex.: Borda
  1781 ↔ ROC ↔ AEO; SEMA ↔ escola europeia), e quem pesquisa separado publica os dois
  lados sem a conexão.
- **Selos só na bibliografia, não no capítulo** — rejeitada: o leitor do capítulo não
  abre a bibliografia; a honestidade precisa estar na página em que a afirmação é
  feita.

## Consequências

- Positivas: transferência (o leitor reconhece o *aperto* em contextos novos);
  proteção contra história inventada; as conexões entre métodos viram conteúdo (o fio
  ordinal 1781→2026 já apareceu na primeira sessão de pesquisa).
- Custos: toda rodada de capítulo de método ganha uma dependência (a nota de
  pesquisa); afirmações ⏳ obrigam o registro "a literatura atribui", menos fluido que
  afirmação direta. Aceitos.
- Evidência imediata do valor do processo (mesma sessão): a leitura integral de Roy
  (1968) rendeu o que nenhum resumo trazia — ELECTRE nasce como nota interna da SEMA
  em 1966, em coautoria (Benayoun/Roy/Sussmann), com manual de programa *anterior* à
  nota do método, rodando em CDC para ≤100 objetos; e o acrônimo famoso **não está**
  no artigo de 1968 (achado negativo selado).

## Fontes

- Texto do princípio: mensagem do autor, 2026-08-10 (verbatim na constituição v1.1.0).
- Roy (1968), RAIRO — lido; INFORMS In Memoriam T. Saaty — lido; demais na nota de
  pesquisa com selos.
