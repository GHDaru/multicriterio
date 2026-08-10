# 14 — Agregação Estocástica Ordinal: decidir só com ordens

> **Estado da arte capturado em 2026-07** · última revisão 2026-08-10 · [histórico](../HISTORICO.md)
>
> **Capítulo de contribuição original do autor** — método em desenvolvimento
> (iteração 1); o artigo completo, com formalização, provas e experimentos, está no
> [Apêndice C](../apendice-c-artigo-aeo.md). Este capítulo é a via didática.

## Objetivos de aprendizagem

1. **Executar** a AEO: transformar rankings por critério (e, opcionalmente, uma ordem
   de importância) em uma matriz de aceitabilidade por simulação.
2. **Aplicar** o protocolo de decisão sobre as contagens de 1ºs, 2ºs, … — e
   **explicar** por que "quem tem mais 1ºs" não basta.
3. **Interpretar** os dois modos (com e sem ordem de pesos) e o vetor de pesos
   central — as "crenças" que elegem cada alternativa.
4. **Situar** o método na família SMAA e reconhecer o que é escolha de modelagem
   (prior de sorteio).

## O problema

Todos os métodos das Partes II–III pedem números que o decisor muitas vezes não tem.
O que ele tem, com conforto, são **ordens**: "no preço, A4 vem antes de A2, que vem
antes de A1…"; "preço importa mais que área". O cap. 03 mostrou o custo de inventar
números (rating direto ancora; ROC exagera); o cap. 11 mostrou que o vencedor pode
depender de 0,008 de peso. E se, em vez de escolher *um* número para cada lacuna, nós
sorteássemos **todos os números compatíveis com as ordens** — e contássemos os
resultados?

## De onde isto veio

**O aperto.** Aqui a história é testemunho, não arqueologia: o método é do autor deste
livro (2026), e a fonte primária é **este repositório** — specs 028–029 e ADR 0008
guardam, com data e diff, o esboço original, a pergunta aberta ("com as contagens de
1ºs, 2ºs…, como decido?") e até uma conjectura numérica que estava *errada por um
motivo interessante* (a média 0,75/0,25, que a Prop. 5 revelou pertencer a outro prior
— o do simplexo). É o único capítulo em que se pode auditar o aperto no controle de
versão.

**O que se fazia antes.** Inventar os números que faltam: transformar ordens em pesos
por ROC (cap. 03) e seguir com um método cardinal — um ponto escolhido no meio de um
contínuo de possibilidades. E, sem sabermos na concepção, a família **SMAA** (Finlândia,
anos 1990) já explorava o espaço de pesos por simulação — a literatura situa sua
origem em decisões públicas reais (localização de infraestrutura) em que os decisores
**se recusavam a declarar pesos**.

**A virada.** Não escolher ponto nenhum: sortear **todos os números compatíveis com as
ordens declaradas** e contar os resultados — "o sorteio simula infinitas funções de
importância" (Observação 1 do Apêndice C torna a frase literal). A independência da
concepção e o parentesco com a SMAA estão declarados no artigo (§2) — convergência é
evidência de que o aperto é real.

**A ideia reaproveitável.** Sob informação parcial, **não colapse a incerteza num
ponto: integre sobre o conjunto compatível e reporte a distribuição** — e declare o
prior, porque "não escolher" também é uma escolha (a Prop. 5 mede exatamente o preço
dela). O padrão serve a qualquer modelagem com insumo incompleto, de riscos a
elicitação de especialistas.

**O nome.** Descritivo e do autor: **Agregação Estocástica Ordinal** — agrega ordens,
por sorteio.

| Afirmação | Selo |
|---|---|
| Gênese da AEO (esboço, pergunta aberta, conjectura, iterações) | ✓ fonte primária = este repositório, versionado (specs 028–029, ADR 0008) |
| SMAA: Lahdelma, Hokkanen & Salminen (1998) e família (SMAA-2, SMAA-O, survey) | ✓ᵐ (DOIs na bibliografia; conteúdo não lido) |
| Origem da SMAA em decisões públicas finlandesas com recusa de pesos | ⏳ atribuição corrente |
| Posto esperado ≡ Borda média; ROC ≡ média do prior do simplexo | ✓ provas próprias testadas em código (Apêndice C, Props. 2 e 5) |

## Fundamentos

A ideia (do autor; parentesco com a família SMAA — ver Apêndice C, §2): a cada
rodada, sorteie valores $U(0,1)$ para cada critério, **ordene-os conforme o ranking
declarado** (maior valor ao mais preferido), normalize a coluna para somar 1; faça o
mesmo com os pesos (com ou sem ordem declarada); agregue por soma ponderada e anote o
ranking. Após $N$ rodadas:

- a **matriz de aceitabilidade** $b_i^r$ diz a fração das rodadas em que a
  alternativa $i$ ficou em $r$-ésimo — o histograma de destinos possíveis;
- o **posto esperado** $\bar{r}_i$ resume a distribuição (e equivale à Borda média —
  Apêndice C, Prop. 2);
- os **duelos** $p_{ik} = \Pr[s_i > s_k]$ dão o vencedor de Condorcet estocástico,
  quando existe;
- o **vetor de pesos central** de cada alternativa é a média dos pesos nas rodadas em
  que ela venceu — *o que é preciso acreditar para elegê-la*.

A frase fundadora do método — "o sorteio simula infinitas funções de importância" —
é literal, não metáfora: as frações que o torneio devolve convergem (lei dos grandes
números) para as probabilidades calculadas sobre o **contínuo** de todas as funções
de valor e peso compatíveis com as ordens declaradas (Apêndice C, Observação 1).

Um detalhe que parece técnico e é decisão: **o jeito de sortear é um prior**. O
esquema original (uniformes ordenadas divididas pela soma) induz, para dois itens,
média exata $(\ln 2;\ 1-\ln 2) \approx (0{,}69;\ 0{,}31)$; o prior alternativo do
simplexo (o da SMAA clássica) dá $(0{,}75;\ 0{,}25)$ — os pesos ROC do cap. 03. O
motor aceita os dois (`prior=`), e o Apêndice C (Prop. 5 e §7.4) prova a diferença e
mede o impacto: no caso âncora, o campeão não muda, mas a aceitabilidade dele quase
dobra. Declare o prior como declara a normalização.

Duas garantias valem a pena conhecer (provas no Apêndice C): dominância ordinal é
respeitada com probabilidade 1 (dominada nunca sobe), e o erro de Monte Carlo com
$N = 20.000$ é de no máximo ±0,35 ponto percentual — diferenças menores são empate.

## O método passo a passo

**Passo 1 — só as ordens do caso âncora** (extraídas da matriz do cap. 01, sem os
números): Preço: A4 ≻ A2 ≻ A1 ≻ A3 · Área: A3 ≻ A2 ≻ A1 ≻ A4 · Deslocamento: A1 ≻
A4 ≻ A3 ≻ A2 · Bairro: A3 ≻ A1 ≻ A2 ≻ A4; importância: Preço ≻ Área ≻ Deslocamento ≻
Bairro.

**Passo 2 — 20.000 rodadas** (semente 42):

| Alternativa | 1º | 2º | 3º | 4º | posto esp. |
|---|---|---|---|---|---|
| **A4 — Estação** | **36,4%** | 24,3% | 19,5% | 19,8% | **2,226** |
| A2 — Jardim | 19,3% | 31,3% | 28,9% | 20,6% | 2,508 |
| A1 — Centro | 23,4% | 24,7% | 28,1% | 23,7% | 2,522 |
| A3 — Parque | 20,9% | 19,7% | 23,5% | 35,9% | 2,744 |

**Passo 3 — o protocolo** (a resposta à pergunta "com as contagens, quem ficou em
primeiro?"):

1. a matriz completa é o resultado — publique-a;
2. **ordem final pelo posto esperado** (desempate: lexicográfico nos 1ºs, 2ºs, …);
3. **selo de robustez**: o vencedor de Condorcet estocástico existe e coincide?
   Aqui sim (A4 vence todos os duelos) — selo fechado;
4. **empate técnico** quando o duelo fica em [45%; 55%]: A1 × A2 deu **50,04%** —
   empate puro; o relatório diz "A4 primeiro; A1 e A2 empatados na sequência".

**Passo 4 — sem ordem de pesos (força intrínseca).** Repetindo sem declarar
importância: A3 tem mais 1ºs (42,8%) **e** é o vencedor de Condorcet, mas A1 tem
melhor posto esperado (1,993 × 2,019). **As regras divergem** — e é exatamente por
isso que o protocolo manda reportar a divergência em vez de escondê-la: sob
ignorância de pesos, A3 é a aposta de pico, A1 a de consistência; escolher entre eles
é escolher um perfil de risco. (De quebra: A3, lanterna nos métodos cardinais do
livro, é intrinsecamente forte — eram os *pesos do livro* que o desfavoreciam.)

**Passo 5 — crenças.** O vetor central de A4 é (0,452; 0,288; 0,183; 0,077): eleger
A4 é acreditar que quase metade da importância está no Preço. O de A1 é mais
equilibrado (0,379; 0,292; 0,219; 0,110). Mostre isso a quem defende cada candidato
e a reunião muda de assunto: de alternativas para crenças. *Todos os números deste
capítulo são testes da etapa 14.*

## Quando usar (e quando não)

Use a AEO quando os números não existem ou não merecem confiança — fases iniciais,
comitês que só concordam em ordens, triagem de portfólio — e como **complemento de
robustez** dos métodos cardinais (o passo 4 do protocolo do cap. 11 ganha uma versão
ordinal). Não use como substituto quando há medidas reais e confiáveis: jogar fora
cardinalidade legítima é desperdiçar informação (o caso fornecedor no Apêndice C
mostra a AEO *confirmando* o resultado cardinal — é esse o uso conjunto ideal).
Declare sempre: o prior de sorteio (Apêndice C, Prop. 3), o $N$ e a semente — são as
escolhas de modelagem do método.

### Leitura executiva

A AEO responde com distribuições o que os outros métodos respondem com um número:
em vez de "A1 venceu com 0,5444", ela diz "A4 vence em 36% dos mundos compatíveis
com o que você declarou; A1 e A2 estão empatados; eleger A4 é acreditar ~45% em
preço". **O que levar** hoje: quando só houver ordens, não invente números — simule
todos; decida pelo posto esperado, sele com Condorcet estocástico, declare empates
técnicos e use os pesos centrais para transformar briga de candidatos em conversa
sobre crenças.

## Mão na massa — decisor-zero, etapa 14

Em `decisor-zero/etapas/14-simulacao-ordinal/`, nasce `motor/ordinal.py`
(`simular_aeo`: imputação ordinal, torneio, aceitabilidade, duelos, Condorcet
estocástico, pesos centrais — tudo com semente reprodutível) e a rota
`POST /api/aeo`; a página roda os três cenários deste capítulo. Exercício de
completar: implemente o suporte a **empates** no ranking de um critério (alternativas
no mesmo grupo recebem a média dos valores sorteados do grupo) e escreva o teste que
mostra o efeito na aceitabilidade — é o item 2 da agenda do artigo.

## Verificação

1. Por que uma alternativa dominada ordinalmente nunca aparece à frente do seu
   dominador em nenhuma rodada? (Dica: objetivo 1 — Apêndice C, Prop. 1.)
2. No passo 4, "mais 1ºs" e "melhor posto esperado" apontam alternativas diferentes.
   O que cada regra privilegia, e por que o protocolo manda reportar as duas? (Dica:
   objetivo 2 — pico × consistência.)
3. O que significa, em português, o vetor de pesos central de A4 concentrar 45% no
   Preço? (Dica: objetivo 3 — crenças.)

---

## Apêndice A — a AEO no ecossistema

- A família **SMAA** é o parente direto — implementações abertas existem no pacote R
  `smaa` (Tervonen) e em ferramentas acadêmicas; o survey de Tervonen & Figueira
  (2008) mapeia variantes (ver Apêndice C, referências ✓).
- **pymcdm/pyDecision** não trazem SMAA-O — a etapa 14 é, por ora, a implementação
  de referência do livro, validada por propriedades (dominância, simetria,
  reprodutibilidade por semente).
- O artigo completo, com provas e agenda de iterações, é o
  [Apêndice C](../apendice-c-artigo-aeo.md) — um artigo **vivo**, versionado como o
  resto do livro.

## Apêndice B — gabarito comentado da Verificação

1. Em cada rodada, o dominador recebe valor estritamente maior em **todos** os
   critérios (os sorteios ordenados são distintos quase certamente); com pesos
   positivos, sua soma ponderada é estritamente maior — em toda rodada, logo em 100%
   delas.
2. "Mais 1ºs" privilegia o **pico** (chegar ao topo em muitos mundos, ainda que caia
   em outros); o posto esperado privilegia a **consistência** (nunca ir mal). São
   perfis de risco diferentes e legítimos; esconder a divergência escolheria um perfil
   pelo leitor sem avisar.
3. Que entre todos os mundos sorteados em que A4 vence, o peso médio do Preço é
   ~0,45: defender A4 equivale a defender que o Preço carrega quase metade da
   importância total. Se a decisora rejeita essa crença, deve rejeitar A4 — coerência
   entre escolha e crença.
