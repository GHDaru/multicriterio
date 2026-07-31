# 09 — ELECTRE: concordância, discordância e o direito de veto

> **Estado da arte capturado em 2026-07** · última revisão 2026-07-31 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Calcular** os índices de concordância e discordância de um par de alternativas e
   **aplicar** os limiares c* e d* para construir a relação de sobreclassificação.
2. **Explicar** o veto — o mecanismo que nenhum método compensatório tem — e o kernel
   como shortlist defensável.
3. **Avaliar** quando "não ranquear" é a resposta metodologicamente honesta.

## O problema

Todos os métodos até aqui — até o PROMETHEE II — terminam somando algo. Consequência:
um apartamento em bairro inaceitável pode vencer se for barato o bastante. Para muitas
decisões reais isso é inadmissível ("segurança não se negocia", "abaixo do mínimo
legal não entra"). O ELECTRE nasce exatamente desta recusa: **preferência global não
precisa ser uma soma** — pode ser um sistema de votação com direito de veto.

## Fundamentos

Roy (1968) — o paper que funda o outranking, com PDF aberto na Numdam — propõe aceitar
a afirmação "$a$ sobreclassifica $b$" ($a\,S\,b$: "$a$ é pelo menos tão boa quanto
$b$") quando duas condições valem:

- **Concordância**: a coalizão de critérios em que $a \succeq b$ pesa o suficiente —
  $C(a,b) = \sum_{j:\, a \succeq_j b} w_j \ge c^*$. Os pesos aqui são **votos**, não
  taxas de troca (Belton & Stewart, 2002): nada é multiplicado por desempenho.
- **Não-discordância**: nenhum critério contrário protesta alto demais —
  $D(a,b) = \max_{j:\, b \succ_j a} \dfrac{\text{vantagem de } b}{\text{amplitude}_j}
  \le d^*$.

O **veto** é a versão dura: se em algum critério a vantagem de $b$ sobre $a$ atinge o
limiar $v_j$, então $a\,S\,b$ é bloqueado — não importa a concordância. Da relação $S$
extrai-se o **kernel**: as alternativas que ninguém sobreclassifica estritamente — uma
*shortlist*, não um pódio. Ordenar tudo é tarefa das variantes posteriores (ELECTRE
II–IV; ver Greco et al., 2016).

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

Caso âncora, pesos 0,35/0,25/0,25/0,15. Amostra do par **A1 vs A4**: A1 é melhor em
Área, Deslocamento e Bairro → $C = 0{,}25+0{,}25+0{,}15 = 0{,}65$; contra, só o Preço,
onde A4 vence por 110 mil sobre amplitude de 180 mil → $D = 0{,}6111$.

**Cenário 1 — limiares exigentes** ($c^*=0{,}6$, $d^*=0{,}4$): **nenhum par passa**.
Toda coalizão forte carrega um protesto alto. Relação vazia, kernel = {A1, A2, A3, A4}
— o ELECTRE está dizendo: *o conflito deste problema é real; nenhuma escolha é
incontestável*. Nenhum método anterior sabia dizer isso.

**Cenário 2 — tolerando protesto** ($d^*=0{,}65$): surgem $A1\,S\,A4$ e $A4\,S\,A2$;
o kernel encolhe para **{A1, A3}** — a shortlist dos que ninguém supera. Note o
resultado qualitativo: A3, sempre 3º/4º nos métodos compensatórios, entra na shortlist
— caro, mas **incomparável** (ninguém monta coalizão contra seus 85 m² e bairro 5).

**Cenário 3 — veto**: com veto de 1 ponto no Bairro, $A4\,S\,A2$ morre (bairro 2
contra 3 atinge o veto) mesmo com $C = 0{,}6$ — e A2 volta à shortlist. *Os três
cenários são testes da etapa 09.*

## Quando usar (e quando não)

ELECTRE é o instrumento quando há **critérios inegociáveis**, quando pesos só fazem
sentido como votos (comitês, regulação, licitação) ou quando o entregável honesto é uma
shortlist para negociação humana. Custos: mais parâmetros para calibrar (c*, d*,
vetos — e o resultado é sensível a eles, como os cenários mostram), saída não-escalar
(difícil de plotar num painel) e possível intransitividade da relação $S$ — que é
informação, não defeito. Para ordenar tudo com espírito de outranking, PROMETHEE II
(cap. 08) ou as variantes ELECTRE de ordenação.

### Leitura executiva

O ELECTRE inverte o contrato dos métodos anteriores: em vez de "todo déficit tem
preço", vale "coalizão forte + nenhum protesto alto + nenhum veto". O resultado é uma
shortlist com uma propriedade rara — ela sabe dizer "ninguém vence de forma
incontestável". **O que levar** hoje: quando um stakeholder disser "isso é
inegociável", pare de ajustar pesos — modele um veto; e quando o comitê empacar, rode
um ELECTRE e negocie só dentro do kernel.

## Mão na massa — decisor-zero, etapa 09

Em `decisor-zero/etapas/09-electre/`, nasce `motor/electre.py` (concordância,
discordância normalizada pela amplitude, vetos, kernel) e a rota
`POST /api/matriz/electre`; a página tem controles para c*, d* e veto no Bairro —
reproduza os três cenários. Decisão da rodada: o ELECTRE **não** entra no catálogo de
ranking do produto (a saída não é ranking); a exposição como análise, ao lado da
dominância, fica para a spec do cap. 11. Exercício de completar: implemente a
**concordância parcial** (crédito proporcional quando a diferença é pequena) e mostre
em teste como o cenário 1 muda.

## Segundo domínio — sobreclassificação na decisão B2B

Fornecedores com $c^* = 0{,}6$ e $d^* = 0{,}5$: a única relação que passa é
**F2 S F1** — a coalizão de F2 (custo + latência + suporte = 0,75) é forte e o único
protesto (SLA) fica abaixo do limiar. Kernel: **{F2, F3}**. Note quem sobrou: F3, o
mais barato, não sobreclassifica ninguém — mas ninguém o sobreclassifica (seu SLA de
99,0% e latência de 60 ms geram protestos altos em qualquer coalizão contra ele). A
shortlist honesta é "Regional ou Nicho"; a Hiperescala sai da mesa por veredito, não
por opinião. *Teste `test_segundo_dominio_kernel_f2_f3` da etapa 09.*

## Verificação

1. Calcule à mão $C(A3, A2)$ e explique por que, mesmo com 0,65 de concordância, A3
   não sobreclassifica A2 no cenário 1. (Dica: objetivo 1 — quem protesta?)
2. Qual a diferença conceitual entre peso-voto (ELECTRE) e peso-taxa-de-troca (SAW)?
   (Dica: objetivo 1 — o que multiplica o quê.)
3. Por que "kernel com 4 alternativas" é um resultado útil, e não um fracasso do
   método? (Dica: objetivo 3.)

---

## Apêndice A — o ELECTRE nas ferramentas

- **pyDecision** implementa ELECTRE I, I_s, I_v, II, III e IV com notebooks — a
  referência aberta mais completa (<https://github.com/Valdecy/pyDecision>).
- **pymcdm** não traz ELECTRE I clássico (foco em métodos de escore) — por isso a
  validação desta etapa é por propriedades e cenários, não cruzada
  (<https://github.com/kotbaton/pymcdm>).
- O PDF do paper fundador está aberto na Numdam:
  <https://www.numdam.org/item/RO_1968__2_1_57_0.pdf>.

## Apêndice B — gabarito comentado da Verificação

1. $C(A3, A2) = 0{,}25 + 0{,}25 + 0{,}15 = 0{,}65$ (área, deslocamento, bairro). Mas o
   protesto do Preço — A2 é 140 mil mais barata, sobre amplitude de 180 mil —
   dá $D = 0{,}7778 > d^* = 0{,}4$: coalizão forte, veto informal do bolso. Não passa.
2. No SAW, o peso multiplica desempenho normalizado — é **taxa de troca** (quanto de
   um critério compensa quanto de outro). No ELECTRE, o peso só entra somado na
   coalizão de quem está a favor — é **voto**: não existe "quanto", só "quem". Por
   isso pesos iguais produzem comportamentos diferentes nos dois mundos.
3. Porque encolher a shortlist não é o único serviço: kernel cheio diz que, nos seus
   limiares, **nenhuma escolha é incontestável** — informação que protege o decisor de
   falsas certezas e direciona a conversa para os limiares (ou para coletar mais
   dados), em vez de forçar um vencedor.
