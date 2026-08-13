# 08 — PROMETHEE: preferência par a par e fluxos

> **Estado da arte capturado em 2026-07** · última revisão 2026-08-13 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Explicar** o que muda de escola: sobreclassificação compara alternativas **entre
   si**, par a par — não contra uma escala absoluta de valor.
2. **Calcular** o PROMETHEE II completo: funções de preferência, índice π, fluxos
   φ⁺, φ⁻ e o fluxo líquido φ.
3. **Avaliar** o efeito da função de preferência (degrau × V-shape): como limiares de
   indiferença mudam o pódio sem tocar em pesos nem desempenhos.

## O problema

Nos métodos compensatórios, R$ 1 de vantagem é R$ 1 de vantagem — o degrau entre
"empate" e "preferência" não existe. Mas pergunte a um decisor real: um apartamento
R$ 2 mil mais barato é *preferível*, ou é *a mesma coisa*? A escola europeia
(outranking) leva a sério a ideia de que preferência **nasce da comparação entre duas
alternativas concretas** e pode ser fraca, forte ou nula conforme o tamanho da
diferença.

## De onde isto veio

**O aperto.** O outranking já existia (o ELECTRE, cap. 09, é quinze anos mais velho) —
e era esse o problema. A literatura conta que **Jean-Pierre Brans**, da escola belga,
apresentou o PROMETHEE em **1982**, numa conferência na Université Laval (Québec)
chamada, apropriadamente, *L'ingénierie de la décision*: a segunda geração de um campo
respondendo à crítica que a primeira acumulara — limiares de concordância e
discordância que o decisor aceitava sem entender.

**O que se fazia antes.** ELECTRE: sobreclassificação com parâmetros globais ($c^*$,
$d^*$, vetos) potentes, mas opacos — mexa em $d^*$ de 0,4 para 0,65 (nosso cap. 09 faz
isso) e explique a um comitê o que exatamente mudou na *preferência* de alguém.

**A virada.** Colocar os parâmetros **onde o decisor tem intuição**: por critério, uma
função que traduz a *diferença de desempenho* em preferência — com limiares que
significam algo dizível ("abaixo de R$ 2 mil é a mesma coisa"; "acima de R$ 200 mil a
preferência satura"). Seis formas de função, escolhidas pelo dono do problema, não
pelo analista.

**A ideia reaproveitável.** **Interpretabilidade de parâmetro é requisito, não
cosmética**: um modelo cujos parâmetros o dono da decisão consegue discutir é um
modelo que sobrevive à reunião. E a meta-lição da segunda geração: aceitar a crítica
ao antecessor e responder **dentro** do paradigma (o PROMETHEE não abandona o
outranking — o conserta onde doía).

**O nome.** A expansão consta do título do paper de 1985: *Preference Ranking
Organisation METHod (for Enrichment Evaluations)* — e o acrônimo pisca para o titã
que roubou o fogo; a intenção mitológica é corrente, mas não a encontramos afirmada
pelos autores em fonte primária. Detalhe de registro que rima com o SAW: o título
completo no catálogo da *Management Science* começa com "**Note**—" — o paper de
referência do PROMETHEE entrou na revista como nota, assim como a axiomatização de
Fishburn entrou na *Operations Research* como carta ao editor (cap. 04). Duas peças
fundadoras do campo, publicadas pela porta lateral.

| Afirmação | Selo |
|---|---|
| Apresentação em 1982, conferência "L'ingénierie de la décision", Université Laval (Québec) | ⏳ atribuição corrente; atas na fila (esforço alto) |
| Brans & Vincke (1985), *Management Science* — paper de referência, catalogado como "Note—…" | ✓ᵐ (registro na bibliografia; título completo conferido no Unpaywall/Semantic Scholar em 2026-08-13; conteúdo não lido) |
| Motivação "responder à opacidade do ELECTRE" | 📖 leitura editorial (coerente com a arquitetura do método) |
| Alusão mitológica intencional no nome | ⏳ corrente, não confirmada |

## Fundamentos

Brans & Vincke (1985) definem o PROMETHEE sobre a matriz $X$, pesos $w$ e, por
critério, uma **função de preferência** $P_j(d)$ que traduz a diferença de desempenho
$d$ (ajustada pela direção) em preferência $[0,1]$. Das seis funções do paper, este
livro implementa duas (ADR 0006): **usual** (degrau — qualquer $d>0$ vira preferência
total) e **V-shape** (linear até o limiar $p$: $P = \min(d/p, 1)$ — diferenças pequenas
valem pouco). Agregando, $\pi(a,b) = \sum_j w_j P_j(d_j)$ mede o quanto $a$ supera $b$.
Os **fluxos** resumem o torneio: $\phi^+(a)$ (média do que $a$ faz com os rivais),
$\phi^-(a)$ (o que sofre) e o líquido $\phi = \phi^+ - \phi^-$. PROMETHEE II ordena por
$\phi$ (ordem total); PROMETHEE I, mais prudente, só declara preferência quando φ⁺ e
φ⁻ concordam — e admite incomparabilidade.

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

Caso âncora, pesos 0,35/0,25/0,25/0,15, função **usual**:

| Alternativa | φ⁺ | φ⁻ | φ |
|---|---|---|---|
| **A1 — Centro** | 0,5500 | 0,4500 | **+0,1000** |
| A4 — Estação | 0,5167 | 0,4833 | +0,0333 |
| A3 — Parque | 0,4833 | 0,5167 | −0,0333 |
| A2 — Jardim | 0,4500 | 0,5500 | −0,1000 |

(Σφ = 0 sempre — todo ganho é perda de alguém; propriedade testada.) Pódio igual ao
SAW/TOPSIS com estes pesos.

Agora **V-shape** com limiares $p = (200\text{k}, 30, 20, 3)$: cada φ⁺ e φ⁻ encolhe
(preferências fracas evaporam), mas o líquido pode **crescer** — A3 salta de
φ = −0,0333 para **+0,0406**: suas vantagens são *grandes* (30 m² a mais que A4, bairro
5 contra 2) e sobrevivem ao limiar, enquanto as vantagens miúdas dos rivais viram
quase-indiferença. A função de preferência é parte do modelo, tão decisiva quanto o
vetor $w$. *Ambos os cenários são testes da etapa 08, com o "usual" validado contra a
pymcdm a 10⁻⁶.*

## Quando usar (e quando não)

PROMETHEE II é a porta de entrada do outranking: pesos familiares, resultado em escala
única (φ), e a chance de declarar indiferença por limiar — coisa que nenhum método das
Partes I–II oferece. Exige, porém, calibrar as funções de preferência (limiares mal
postos distorcem tanto quanto pesos mal postos) e continua **quase** compensatório no
II (o φ líquido soma tudo); para vetos de verdade ("bairro 2 é inaceitável, ponto"), o
instrumento é o ELECTRE (cap. 09). Como os fluxos dependem do conjunto de alternativas,
o rank reversal também ronda aqui (cap. 11).

### Leitura executiva

PROMETHEE troca a pergunta "quanto vale?" por "quem supera quem, e por quanto?" — e dá
ao decisor um dial novo: o limiar a partir do qual uma diferença *importa*. No caso
âncora, o degrau confirma A1; um V-shape razoável promove A3. **O que levar** hoje:
quando o time discute se "R$ 5 mil de diferença é relevante", pare de discutir pesos —
o instrumento certo é a função de preferência, e o PROMETHEE a torna explícita.

## Mão na massa — decisor-zero, etapa 08

Em `decisor-zero/etapas/08-promethee/`, nasce `motor/promethee.py` (funções usual e
V-shape, fluxos) e a rota `POST /api/matriz/promethee`; a página compara as duas
funções — veja A3 mudar de lado. O produto ganhou `promethee2` (função usual) no
catálogo. Exercício de completar: implemente o **PROMETHEE I** (pré-ordem parcial:
$a$ supera $b$ só se φ⁺ e φ⁻ concordarem) e escreva o teste mostrando qual par do caso
âncora fica **incomparável**.

## Segundo domínio — fluxos na decisão B2B

Fornecedores, função usual: **φ = F2 +0,20 > F3 +0,10 > F1 −0,30**. A leitura par a
par é instrutiva: F1 (a Hiperescala) perde os dois duelos — só vence no SLA, cujo peso
(0,25) não monta coalizão contra custo + latência + suporte. Em três alternativas, o
PROMETHEE II é quase uma eleição de dois turnos por critério — e a Σφ = 0 continua
valendo (+0,20 + 0,10 − 0,30). *Teste `test_segundo_dominio_f1_perde_os_duelos` da
etapa 08.*

## Verificação

1. Por que Σφ = 0 sempre? (Dica: objetivo 2 — cada π(a,b) aparece uma vez como ganho e
   uma como perda.)
2. Com a função usual, uma vantagem de R$ 10 e uma de R$ 100 mil pesam igual no
   critério Preço. Isso é defeito ou escolha? (Dica: objetivo 3.)
3. No V-shape do capítulo, por que A3 sobe? Reconstrua o argumento com os tamanhos das
   diferenças. (Dica: objetivo 3 — vantagens grandes × miúdas.)

---

## Apêndice A — o PROMETHEE nas ferramentas

- **pymcdm**: `PROMETHEE_II('usual' | 'vshape' | ...)` — nossa validação cruzada usa
  o `usual` (<https://github.com/kotbaton/pymcdm>).
- **pyDecision** traz PROMETHEE I–VI com notebooks
  (<https://github.com/Valdecy/pyDecision>).
- **Visual PROMETHEE / GAIA** é a ferramenta histórica da escola (plano GAIA para
  visualização) — hoje o ecossistema aberto cobre o essencial.

## Apêndice B — gabarito comentado da Verificação

1. Cada índice π(a,b) entra uma vez em φ⁺(a) e uma vez em φ⁻(b), com o mesmo valor —
   ao somar os líquidos, todo termo aparece com sinal + e sinal −, e a soma colapsa em
   zero. É um invariante bom para testes automatizados (e a etapa o testa).
2. Escolha — e das mais importantes do método. A função usual declara que qualquer
   diferença é preferência total ("degrau"); se isso incomoda no critério Preço, o
   modelo está pedindo um limiar (V-shape ou similar). O erro seria usar o degrau sem
   perceber que ele é uma declaração.
3. Com limiares, as vantagens *miúdas* dos rivais (poucos milhares de reais, poucos
   minutos) encolhem para quase zero, enquanto as vantagens *grandes* de A3 (30 m²
   sobre A4, bairro 5 contra 2) continuam rendendo preferência quase total — o φ⁺ de
   A3 resiste, o dos rivais derrete, e o líquido de A3 sobe.
