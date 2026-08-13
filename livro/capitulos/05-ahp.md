# 05 — AHP: pesos por comparações par a par (e o detector de incoerência)

> **Estado da arte capturado em 2026-07** · última revisão 2026-08-13 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Construir** uma matriz de julgamentos par a par na escala 1–9 de Saaty e
   **calcular** o vetor de prioridades pelo autovetor principal.
2. **Avaliar** a coerência dos julgamentos com $\lambda_{max}$, CI e a razão de
   consistência CR — e **explicar** por que CR > 0,10 manda revisar, não calcular.
3. **Analisar** o debate crítico do AHP: rank reversal (Belton & Gear) e a objeção de
   fundamento (Dyer) — e a decisão deste livro de usá-lo como técnica de pesos.

## O problema

O cap. 04 terminou com uma constatação incômoda: o vencedor pertence ao vetor $w$. Mas
pedir "distribua 100 pontos entre 4 critérios" já se mostrou frágil (cap. 03) — pessoas
ancoram, chutam, mudam. O que um decisor *consegue* responder com confiança é uma
pergunta de cada vez: "entre Preço e Área, qual importa mais — e quanto?". O AHP
(*Analytic Hierarchy Process*) transforma um conjunto dessas perguntas simples num
vetor de pesos — e, melhor, **denuncia quando as respostas se contradizem**.

## De onde isto veio

**O aperto.** No fim dos anos 1960, **Thomas Saaty** dirigia projetos de pesquisa da
Arms Control and Disarmament Agency, no Departamento de Estado americano — as
negociações de desarmamento com a União Soviética. Tinha uma agenda ambiciosa e, nas
palavras de quem contou a história depois, um orçamento generoso: recrutou alguns dos
maiores teóricos dos jogos e da utilidade do mundo. **Três deles ganhariam o Nobel de
Economia** — Gerard Debreu, John Harsanyi e Reinhard Selten.

E não funcionou. O próprio Saaty, relembrando o episódio anos mais tarde, apontou duas
coisas: as teorias e modelos dos cientistas eram gerais e abstratos demais para se
adaptarem à necessidade concreta de **trocar um sistema de armas por outro**; e a
posição americana era redigida por advogados que dominavam o direito, mas não eram
melhores que os cientistas na hora de dizer **quanto valia** cada arma em negociação.
Guarde a cena: os melhores modelos do planeta, uma sala cheia de futuros laureados, e
ninguém capaz de responder à pergunta que a mesa fazia. Anos depois, já lecionando na
Wharton, ele continuava incomodado com a ausência de um jeito prático e sistemático de
estabelecer prioridades — e foi isso que o levou a construir um.

**O que se fazia antes.** Dois caminhos, ambos falhando na mesa de negociação: pedir
números absolutos a especialistas (que eles não têm — o cap. 03 mostrou o chute que
sai disso) ou construir funções de utilidade axiomáticas (que o decisor não entende
nem reconhece como suas).

**A virada.** Ninguém sabe dizer "o preço pesa 0,35" — mas qualquer um diz, com
convicção, "o preço importa umas 3× mais que a área". Saaty trocou a pergunta
impossível por muitas perguntas fáceis (**pares**, não absolutos) e tomou a decisão de
projeto que define o método: em vez de proibir a contradição humana, **medi-la**. O
artigo de 1977 (que lemos) enuncia a premissa sem rodeios — apesar do melhor esforço
das pessoas, seus sentimentos e preferências permanecem inconsistentes e intransitivos;
o modelo, portanto, tem de acomodar a inconsistência, não pressupor sua ausência. A
redundância dos julgamentos (6 comparações para extrair 4 pesos) é o que permite
calcular o quanto o decisor se contradisse.

Duas escolhas do artigo saem da mesma raiz cognitiva: a **hierarquia** existe para
partir um problema grande em conjuntos pequenos, e a **escala 1–9** tem esse teto
porque Saaty a ancora em Miller (1956) — a pessoa não compara mais de sete objetos
(±2) ao mesmo tempo. O limite da mente não é queixa; é parâmetro de projeto.

**A ideia reaproveitável.** Quando o insumo direto é inacessível, **colete julgamentos
relativos redundantes e extraia deles duas coisas: o consenso interno (autovetor) e o
grau de contradição (CR)**. O padrão serve fora daqui: avaliação por comparação pareada
com checagem de consistência aparece hoje de ranqueamento de LLMs a priorização de
backlog. E um segundo padrão, do mesmo artigo: **valide o método subjetivo contra
problemas cuja resposta você já conhece.** Antes de aplicar a hierarquia a decisões
reais, Saaty pediu a pessoas que comparassem aos pares coisas mensuráveis — as
distâncias de seis cidades a Filadélfia, a intensidade luminosa de objetos a
distâncias conhecidas de uma lâmpada — e comparou o autovetor com o valor real
(Cairo: 0,263 estimado contra 0,278 verdadeiro; Tóquio: 0,397 contra 0,361). É o
teste que quase nenhum método de elicitação faz de si mesmo.

**O nome.** Descritivo: uma **hierarquia** (objetivo → critérios → alternativas)
percorrida por um **processo analítico**. Sem lenda de batismo conhecida.

| Afirmação | Selo |
|---|---|
| Afiliação **Wharton School**, University of Pennsylvania (folha de rosto do artigo de 1977) | ✓ Saaty (1977) lido |
| Inconsistência humana como premissa de projeto; hierarquia e escala 1–9 ancoradas em Miller (1956), 7±2 | ✓ Saaty (1977) lido |
| Validação contra respostas conhecidas (distâncias a Filadélfia, lei do inverso do quadrado, riqueza de nações) | ✓ Saaty (1977) lido, §exemplos |
| Plano nacional de transporte do **Sudão** entre as aplicações recentes (junto com trabalho para a Marinha dos EUA e uma corporação mexicana) | ✓ Saaty (1977), conclusões |
| ACDA 1961–1969 (Kennedy/Johnson); saída em 1969 para a Penn; frustração com modelos ignorados; livro 1980 | ✓ obituário INFORMS (fonte secundária aberta, lida na íntegra) |
| Antes das cátedras, passagens pela ACDA, pelo **Office of Naval Research**, pela embaixada americana em Londres e pelo Navy Management Office; doutorado em Yale; Wharton até ser recrutado pela Katz School (Pittsburgh) em 1979 | ✓ obituário da IJAHP (Assad, 2017 — acesso aberto, lido) |
| ACDA no fim dos anos 1960; orçamento generoso e recrutamento de Debreu, Harsanyi e Selten (futuros Nobel); o relato de Saaty (1996) sobre modelos abstratos demais para trocas de armamento e sobre os advogados que redigiam a posição americana; o incômodo persistente na Wharton como motivação | ✓ Forman & Gass (2001), *Operations Research* 49(4) — exposição histórica lida, citando Saaty (1996) |
| Cena fundadora "outono de 1971, planejamento de contingência (DoD)" | ⏳ **achado negativo em quatro fontes**: não aparece no artigo de 1977, nem em Saaty (1990), nem em Saaty (2013), nem na exposição histórica de Forman & Gass — que conta a origem sem essa cena. A versão documentada acima **substitui** a atribuição corrente no corpo do capítulo |

## Fundamentos

Saaty (1977; 1980) propõe: julgue cada par de critérios na escala 1 (igual importância)
a 9 (importância extrema), monte a matriz recíproca $A$ (com $a_{ji} = 1/a_{ij}$) e
extraia as prioridades do **autovetor principal**: $A w = \lambda_{max} w$. Se os
julgamentos fossem perfeitamente coerentes ($a_{ij} = w_i/w_j$ exato), teríamos
$\lambda_{max} = n$; o desvio mede a incoerência:

$$CI = \frac{\lambda_{max} - n}{n - 1}, \qquad CR = \frac{CI}{RI_n}$$

com $RI_n$ tabelado por Saaty a partir de matrizes aleatórias ($RI_4 = 0{,}90$). Regra
prática (Saaty, 1980): **CR ≤ 0,10** — acima disso, os julgamentos se contradizem
demais para produzir pesos confiáveis; a resposta certa é voltar ao decisor, nunca
"usar assim mesmo".

O AHP completo de Saaty também compara as *alternativas* par a par em cada critério e
agrega tudo. É aí que mora a crítica clássica: Belton & Gear (1983) mostraram que
acrescentar uma alternativa irrelevante pode **inverter o ranking** das demais (rank
reversal), e Dyer (1990) questionou o fundamento da agregação — debate respondido por
Saaty no mesmo volume e vivo até hoje.

Detalhe que a leitura da fonte revelou e que a literatura raramente conta: o
**mecanismo** do rank reversal está descrito no artigo de 1977, seis anos antes da
crítica. Saaty registra que tirar uma atividade da matriz de comparações **não
redistribui o peso dela proporcionalmente** entre as demais, e ilustra com uma medição
de riqueza de nações — removida a URSS (0,230), os pesos restantes não são apenas
reescalonados: a razão EUA/Japão sai de 3,47 para 2,74. Ele documentou a instabilidade
como propriedade da matriz; Belton & Gear mostraram que ela chega a virar o pódio.
Achado e crítica são a mesma estrutura vista com sinais opostos. Posição deste livro (ADR 0006): usar o AHP no
que ele tem de mais sólido — **derivar pesos de critérios** — e alimentar com eles os
métodos de ranking cujas premissas já conhecemos (SAW, cap. 04); o rank reversal volta
em detalhe no cap. 11.

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**Passo 1 — os julgamentos** para os critérios do caso âncora ("Preço importa 2× mais
que Área, 2× mais que Deslocamento, 3× mais que Bairro; Área e Deslocamento empatam e
valem 2× Bairro"):

$$A = \begin{bmatrix} 1 & 2 & 2 & 3 \\ 1/2 & 1 & 1 & 2 \\ 1/2 & 1 & 1 & 2 \\ 1/3 & 1/2 & 1/2 & 1 \end{bmatrix}$$

**Passo 2 — prioridades** (autovetor pelo método das potências):

| Preço | Área | Deslocamento | Bairro |
|---|---|---|---|
| 0,4236 | 0,2270 | 0,2270 | 0,1223 |

(Área e Deslocamento receberam julgamentos idênticos — e o autovetor devolve pesos
idênticos, como deve.)

**Passo 3 — diagnóstico**: $\lambda_{max} = 4{,}0104$ → $CI = 0{,}0035$ →
$CR = 0{,}0038 \le 0{,}10$: julgamentos coerentes, pesos utilizáveis.

**Passo 4 — o contraexemplo.** Julgamentos cíclicos ($a_{12}=3$, $a_{23}=1/5$,
$a_{13}=5$: "1 > 2, 3 ≫ 2, 1 ≫ 3" — mas $3 \times 1/5 = 0{,}6 \neq 5$) produzem
$CR = 0{,}4488$: **reprovado**. É o superpoder do AHP sobre o rating direto — notas
soltas não têm como se contradizer; comparações par a par têm, e o CR flagra.

**Passo 5 — fechando o ciclo**: os pesos AHP no SAW do cap. 04 dão
**A4 (0,5939) > A1 (0,5263) > A2 (0,4838) > A3 (0,4629)** — terceiro vetor defensável,
terceiro pódio diferente. A pergunta "então qual ranking vale?" é o assunto do cap. 11.
*Todos os números são reproduzidos pelos testes da etapa 05.*

## Quando usar (e quando não)

Use o AHP quando os pesos precisam de **processo auditável com defesa contra
incoerência** — comitês, decisões públicas, muitos critérios ($n \le 9$; acima disso a
carga de comparações, $n(n-1)/2$, cansa e a qualidade cai). Evite o AHP completo
(alternativas par a par) quando as alternativas mudam com frequência — é o cenário do
rank reversal (Belton & Gear, 1983); com desempenhos mensuráveis, prefira medir
(matriz de decisão) e usar o AHP só nos pesos. E jamais reporte pesos AHP sem o CR ao
lado — pesos sem diagnóstico são rating direto com cerimônia.

### Leitura executiva

O AHP converte perguntas fáceis ("qual dos dois importa mais?") num vetor de pesos com
**controle de qualidade embutido** — o CR reprova julgamentos que se contradizem, coisa
que nenhuma técnica do cap. 03 faz. **O que levar** hoje: eleve seus pesos de rating
direto a AHP quando a decisão exigir defesa formal; publique sempre CR junto com $w$; e
se o CR passar de 0,10, a reunião certa é sobre julgamentos, não sobre planilha.

## Mão na massa — decisor-zero, etapa 05

Em `decisor-zero/etapas/05-ahp/`, nasce `motor/ahp.py` (validação de reciprocidade,
autovetor por potências, CI/CR) e a rota `POST /api/ahp/prioridades`; a página deixa
editar a metade superior da matriz (a inferior é recíproca automática) e ver pesos + CR
na hora — provoque um ciclo e veja a reprovação. No produto, `/api/pesos` ganhou o
método `ahp`, que **recusa** julgamentos com CR > 0,10. Exercício de completar:
implemente o cálculo de prioridades pela **média geométrica das linhas** (atalho
clássico) e escreva o teste que mede o quanto ela se afasta do autovetor nesta matriz.

## Segundo domínio — AHP na decisão B2B

O CTO julga os critérios do fornecedor: "Custo importa 3× mais que Latência, 2× mais
que SLA, 3× mais que Suporte; SLA vale 2× Latência e 2× Suporte; Latência e Suporte
empatam". A matriz recíproca resultante dá prioridades **(0,4554; 0,1409; 0,2628;
0,1409)** com $\lambda_{max}$ próximo de 4 e $CR = 0{,}0038$ — consistente. Repare no
padrão já visto no âncora: julgamentos idênticos (Latência e Suporte) ⇒ pesos
idênticos, agora com valores diferentes dos do apartamento — a mesma técnica, elicitada
em outro domínio, entrega outro vetor. *Teste `test_segundo_dominio_prioridades_do_cto`
da etapa 05.*

## Verificação

1. Por que Área e Deslocamento terminaram com o mesmo peso? O que isso diz sobre o
   autovetor? (Dica: objetivo 1 — linhas idênticas.)
2. $CR = 0{,}25$: o que fazer — normalizar, cortar um critério ou reentrevistar o
   decisor? (Dica: objetivo 2.)
3. Por que este livro evita o AHP completo para ranquear alternativas que mudam toda
   semana? (Dica: objetivo 3 — Belton & Gear.)

---

## Apêndice A — o AHP nas ferramentas

- **pyDecision** traz AHP e fuzzy-AHP com notebooks (método `ahp_method`, incluindo
  CR) — bom para conferir nossos números (<https://github.com/Valdecy/pyDecision>).
- **pymcdm** não traz AHP clássico (foco em métodos que consomem matriz de decisão
  pronta) — coerente com a nossa decisão de tratá-lo como técnica de pesos
  (<https://github.com/kotbaton/pymcdm>).
- O exemplar de Saaty (1980) está acessível no Internet Archive
  (<https://archive.org/details/analytichierarch0000saat>).

## Apêndice B — gabarito comentado da Verificação

1. Porque receberam **linhas idênticas** na matriz de julgamentos: para o autovetor,
   dois critérios com o mesmo perfil de comparações são indistinguíveis — e o método
   devolve exatamente o mesmo peso, como deve ser (é um bom teste de sanidade de
   qualquer implementação).
2. Reentrevistar o decisor. $CR = 0{,}25$ diz que os julgamentos **se contradizem**
   (há ciclos de preferência); normalizar não remove a contradição e cortar critério
   trata o sintoma. O protocolo de Saaty: localizar o julgamento mais inconsistente e
   pedir revisão.
3. Porque no AHP completo as alternativas são comparadas **entre si**, e a entrada de
   uma nova muda todas as comparações relativas — o cenário de rank reversal de
   Belton & Gear (1983). Com desempenhos mensuráveis e alternativas voláteis, matriz
   de decisão + AHP só nos pesos evita o problema estrutural.
