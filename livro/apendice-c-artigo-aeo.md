# Apêndice C — Artigo (vivo): Agregação Estocástica Ordinal

> **Artigo em desenvolvimento — iteração 2** · 2026-07-31 · contribuição original do
> autor do livro; redação e formalização assistidas por IA (Claude Code, Anthropic),
> com curadoria humana. Nome do método é provisório. Todos os números desta versão são
> reproduzidos pelos testes da etapa 14 do `decisor-zero` (semente 42, N = 20.000).
>
> **Novidades da iteração 2**: Proposição 5 (caracterização exata do prior induzido,
> com o corolário fechado $E = (\ln 2,\ 1-\ln 2)$ para $m=2$), resolução da
> conjectura do autor sobre os valores médios, prior alternativo (`simplexo`)
> implementado no motor e experimento comparativo §7.4.

## Agregação Estocástica Ordinal: ranqueamento multicritério com informação puramente ordinal via simulação de funções de importância

### Resumo

Propomos um método de apoio à decisão multicritério para o cenário em que **toda a
informação disponível é ordinal**: o decisor sabe ordenar as alternativas dentro de
cada critério e, opcionalmente, ordenar os critérios por importância — mas não sabe
(ou não quer) atribuir números. O método simula um grande número de **funções de
importância** compatíveis com essas ordens: em cada rodada, valores e pesos são
sorteados de U(0,1), ordenados conforme as preferências declaradas, normalizados e
agregados por soma ponderada; o ranking resultante é registrado. O agregado das
rodadas produz a **matriz de aceitabilidade** (alternativa × posição), probabilidades
de vitória par a par e, por alternativa, o **vetor de pesos central** — as "crenças"
que a elegem. Provamos consistência com dominância ordinal, equivalência entre posto
esperado e contagem de Borda, e caracterizamos o prior de imputação cardinal induzido.
Propomos um protocolo de decisão para a matriz de aceitabilidade e o ilustramos em
dois estudos de caso nos quais as regras clássicas de escolha **divergem entre si** —
evidenciando por que o protocolo é necessário. Posicionamos o método em relação à
família SMAA (Stochastic Multicriteria Acceptability Analysis), da qual é parente
próximo com escolhas de prior e de protocolo distintas.

**Palavras-chave**: decisão multicritério; informação ordinal; simulação de Monte
Carlo; SMAA; aceitabilidade de posição; elicitação de preferências.

---

### 1. Introdução

Os métodos multicritério clássicos (Parte II deste livro) exigem insumos cardinais:
desempenhos mensurados, pesos que somam um, funções de valor. A prática, porém,
frequentemente só oferece **ordens**: "neste critério, A é melhor que B, que é melhor
que C"; "preço importa mais que área". Forçar números sobre ordens — o rating direto
do cap. 03, a escala 1–9 do cap. 05 — introduz precisão espúria: o decisor assina
dígitos que não possui.

A ideia central deste trabalho inverte o fluxo: em vez de comprimir a incerteza numa
única atribuição numérica, **deixamos a incerteza correr solta e a medimos**. Cada
sorteio de valores e pesos compatível com as ordens declaradas é uma "função de
importância" legítima; simular milhares delas equivale a perguntar: *entre todos os
decisores que concordam com estas ordens, quantos elegeriam cada alternativa, e em
que posição?* O resultado não é um ranking seco — é uma distribuição de rankings, da
qual se extraem conclusões com grau de certeza explícito.

Duas leituras adicionais emergem de graça: (i) rodando **sem** a ordem de pesos,
mede-se a *força intrínseca* de cada alternativa — sua performance perante o decisor
desconhecido; (ii) o conjunto dos vetores de peso que elegem uma alternativa revela
as **crenças** necessárias para preferi-la — uma via de elicitação inversa: observe o
que a decisora escolhe, e saiba em que ela acredita.

### 2. Trabalhos relacionados

A ideia pertence à família **SMAA** (*Stochastic Multicriteria Acceptability
Analysis*). Lahdelma, Hokkanen & Salminen (1998) introduziram a exploração do espaço
de pesos por simulação para decisões com informação incompleta; **SMAA-2** (Lahdelma
& Salminen, 2001) definiu os *rank acceptability indices* — a fração de rodadas em
que cada alternativa ocupa cada posição, exatamente a nossa matriz de aceitabilidade
— e o *central weight vector*, que reencontramos na leitura de "crenças". **SMAA-O**
(Lahdelma, Miettinen & Salminen, 2003) trata critérios ordinais, convertendo ordens
em valores cardinais estocásticos consistentes. O survey de Tervonen & Figueira
(2008) mapeia a família. Fora dela, Butler, Jia & Dyer (1997) usaram simulação de
pesos para análise de sensibilidade, e Barron & Barrett (1996) estudaram a qualidade
de decisões tomadas só com pesos ordinais (ROC — que é o *valor esperado* dos pesos
ordenados sob o prior uniforme no simplexo; nosso método, em vez de usar o valor
esperado, usa a distribuição inteira).

**Posição desta contribuição.** O método foi concebido de forma independente pelo
autor e coincide, no espírito, com SMAA-2 + SMAA-O. As diferenças documentadas nesta
iteração: (a) o **prior de imputação cardinal** — uniformes i.i.d. ordenadas e
normalizadas pela soma, para valores *e* pesos (§4, Prop. 3), distinto do prior
uniforme no simplexo da SMAA; (b) o **protocolo de decisão** sobre a matriz de
aceitabilidade (§5), que trata explicitamente o caso em que as regras clássicas
divergem; (c) o uso **duplo** do mesmo motor com e sem ordem de pesos para separar
força intrínseca de preferência do decisor. A comparação sistemática com SMAA-O é
agenda da iteração 2 (§8).

### 3. O método

**Definição 1 (problema ordinal).** Um problema AEO é uma tripla
$\langle A, \Sigma, \tau \rangle$ onde $A = \{a_1, \dots, a_m\}$ são alternativas,
$\Sigma = (\sigma_1, \dots, \sigma_n)$ são permutações de $A$ — $\sigma_j$ ordena as
alternativas da melhor à pior no critério $j$ — e $\tau$, opcional, é uma permutação
de $\{1, \dots, n\}$ ordenando os critérios do mais ao menos importante.

**Definição 2 (imputação cardinal estocástica).** Em cada rodada: para cada critério
$j$, sorteiam-se $u_1, \dots, u_m \sim U(0,1)$ i.i.d.; sejam $u_{(1)} \ge \dots \ge
u_{(m)}$ os valores ordenados. A alternativa na $k$-ésima posição de $\sigma_j$
recebe $v_{kj} = u_{(k)} / \sum_i u_{(i)}$ (coluna soma 1, maior valor ao mais
preferido). Os pesos são gerados da mesma forma: $w_1, \dots, w_n \sim U(0,1)$; se
$\tau$ foi declarada, os valores ordenados são atribuídos conforme $\tau$; em ambos
os casos normaliza-se $\sum_j w_j = 1$.

**Definição 3 (torneio e índices).** O escore da rodada é $s_i = \sum_j w_j v_{ij}$ e
o ranking da rodada ordena $s$ decrescente (empates têm probabilidade zero). Após $N$
rodadas definem-se: o **índice de aceitabilidade** $b_i^r$ = fração das rodadas em
que $a_i$ ficou em $r$-ésimo; o **posto esperado** $\bar{r}_i = \sum_r r \, b_i^r$; a
**probabilidade de duelo** $p_{ik} = \Pr[s_i > s_k]$; o **vencedor de Condorcet
estocástico**, se existir: $a_i$ com $p_{ik} > 1/2$ para todo $k \ne i$; e o **vetor
de pesos central** $w^c_i$ = média (renormalizada) dos vetores de peso das rodadas em
que $a_i$ venceu.

**Observação 1 (interpretação populacional — "infinitas funções de importância").**
A intuição fundadora do método — *o sorteio simula infinitas funções de importância* —
tem enunciado preciso: cada par (matriz de valores imputada, vetor de pesos) gerado
pela Def. 2 é uma função de importância compatível com $\langle \Sigma, \tau
\rangle$, e os índices da Def. 3 são **estimativas Monte Carlo de integrais sobre o
contínuo de todas essas funções**:
$$b_i^r \;=\; \Pr_{(V,W)\sim \text{prior}}\big[\text{posto de } a_i = r\big],
\qquad p_{ik} \;=\; \Pr_{(V,W)\sim \text{prior}}\big[s_i > s_k\big],$$
com as frequências empíricas convergindo a essas probabilidades quando $N \to
\infty$ (LGN; taxa na Prop. 4). A ressalva que dá conteúdo à frase: "infinitas
funções compatíveis" só define probabilidades depois que se escolhe uma **medida**
sobre elas — o prior da Prop. 5. Sortear-e-ordenar é, portanto, integrar sobre todas
as funções de importância compatíveis, *ponderadas pelo prior declarado*.

**Algoritmo 1 (AEO).**

```
entrada: A, Σ, τ (opcional), N, semente, prior ∈ {uniforme, simplexo}
para t = 1..N:
    para cada critério j: sorteie m uniformes, ordene desc,
        atribua via σ_j, normalize a coluna (soma 1)
    sorteie n uniformes; se τ: ordene desc e atribua via τ; normalize
    s_i ← Σ_j w_j v_ij ; registre o ranking, os duelos e, para o
        vencedor, o vetor de pesos
saída: {b_i^r}, {r̄_i}, {p_ik}, Condorcet estocástico, {w^c_i}
```

Custo: $O(N \cdot (mn + m \log m + n \log n))$ — 20.000 rodadas dos casos deste
livro executam em ~1 s em Python puro.

### 4. Propriedades

**Proposição 1 (consistência com dominância ordinal).** *Se $a$ precede $b$ em toda
$\sigma_j$, então $\Pr[s_a > s_b] = 1$; em particular, $b$ nunca ocupa posição melhor
que $a$.* Prova: os sorteios são distintos quase certamente, logo em cada critério a
alternativa mais bem posicionada recebe valor estritamente maior: $v_{aj} > v_{bj}$
para todo $j$. Como $w_j > 0$ q.c., $s_a - s_b = \sum_j w_j (v_{aj} - v_{bj}) > 0$. ∎
(Corolário: o método herda o filtro de dominância do cap. 02 sem precisar executá-lo.
Teste: `test_dominancia_ordinal_e_respeitada_com_probabilidade_1`.)

**Proposição 2 (posto esperado ≡ Borda).** *Ordenar por $\bar{r}_i$ equivale a
ordenar pela contagem de Borda média das rodadas.* Prova: em cada rodada, o posto
$r_i^t$ e a pontuação de Borda $B_i^t$ satisfazem $B_i^t = m - r_i^t$; médias
preservam a relação afim, logo $\bar{B}_i = m - \bar{r}_i$ e as ordens induzidas são
inversas uma da outra. ∎ (Consequência: a regra "posto esperado" traz para o contexto
probabilístico as propriedades — e as limitações — da contagem de Borda do cap. 12.)

**Proposição 3 (valores esperados antes da normalização).** Para $m$ uniformes
i.i.d., $\mathbb{E}[u_{(k)}] = (m+1-k)/(m+1)$ — para $m = 4$: $(0{,}8;\ 0{,}6;\
0{,}4;\ 0{,}2)$. A normalização pela soma introduz dependência entre as componentes,
e $\mathbb{E}[u_{(k)}/S] \ne \mathbb{E}[u_{(k)}]/\mathbb{E}[S]$ — a razão das
esperanças ($2/3$ para o maior com $m=2$) **não** é a esperança da razão. O valor
correto é dado pela Prop. 5.

**Proposição 5 (caracterização exata do prior AEO — nova na iteração 2).** *Seja
$V = (u_1, \dots, u_m)/S$ com $u_i \sim U(0,1)$ i.i.d. A densidade de $V$ no
simplexo é*
$$p(v) \;\propto\; \big(\max_i v_i\big)^{-m}.$$
*Prova.* Mude variáveis $u = s\,v$ com $s = S$ e $v$ no simplexo. O jacobiano é
$s^{m-1}$ e a restrição $u_i \le 1$ equivale a $s \le 1/\max_i v_i$. Integrando a
densidade (constante) do cubo em $s$: $\int_0^{1/\max v} s^{m-1}\,ds =
\frac{1}{m}(\max_i v_i)^{-m}$. ∎

Consequências: (i) o prior AEO **penaliza vetores concentrados** (densidade cai com
$\max v$) — é mais igualitário que o prior uniforme no simplexo (Dirichlet(1)) usado
pela SMAA clássica, cujas médias ordenadas são os pesos ROC do cap. 03; (ii)
**corolário fechado para $m = 2$**: com densidade $\propto t^{-2}$ para o maior
componente $t \in [1/2, 1]$, $\mathbb{E}[V_{(1)}] = \int_{1/2}^{1} t\cdot
t^{-2}dt \big/ \int_{1/2}^{1} t^{-2}dt = \ln 2 \approx 0{,}6931$, logo
$\mathbb{E} = (\ln 2,\ 1-\ln 2) \approx (0{,}693;\ 0{,}307)$.

**Resolução da conjectura do autor.** O esboço original do método conjecturou média
"$0{,}75 \times 0{,}25$, ou algo assim" para $m=2$. A conjectura acerta um prior
legítimo — $(0{,}75;\ 0{,}25)$ é **exatamente** a média sob o prior uniforme no
simplexo (ROC) — mas o esquema de sorteio proposto (uniformes normalizadas) induz
outro: $(\ln 2;\ 1-\ln 2)$. Os três candidatos a "média do 1º" com $m=2$ ficam
assim separados: $0{,}75$ (simplexo/ROC), $0{,}693$ (AEO), $0{,}667$ (falácia da
razão das esperanças). Médias estimadas por Monte Carlo (N = 200.000, ±0,2 p.p.):

| $m$ | prior AEO (uniformes/soma) | prior simplexo (= ROC, exato) |
|---|---|---|
| 2 | 0,693 · 0,307 | 0,750 · 0,250 |
| 3 | 0,523 · 0,324 · 0,153 | 0,611 · 0,278 · 0,111 |
| 4 | 0,418 · 0,299 · 0,191 · 0,092 | 0,521 · 0,271 · 0,146 · 0,063 |
| 5 | 0,347 · 0,269 · 0,196 · 0,127 · 0,062 | 0,457 · 0,257 · 0,157 · 0,090 · 0,040 |

Ambos os priors respeitam a ordem declarada; nenhum é "o correto" — desde a iteração
2 o motor aceita `prior="uniforme"` (default) e `prior="simplexo"`, e a escolha deve
ser reportada (eco direto da lição de normalização do cap. 03). O impacto prático é
medido na §7.4.

**Proposição 4 (convergência e erro de Monte Carlo).** Cada índice é média de
variáveis de Bernoulli i.i.d.; pela lei dos grandes números converge ao valor
populacional, com erro padrão $\le 1/(2\sqrt{N})$. Com $N = 20.000$: no máximo
$\pm 0{,}35$ ponto percentual (1 σ) — diferenças menores que isso, como as do estudo
de caso a seguir, devem ser tratadas como empate.

**Observação (ciclos).** A relação "vence o duelo" ($p_{ik} > 1/2$) não é transitiva
em geral — herda a possibilidade de ciclos de Condorcet (cap. 12). O protocolo da §5
existe precisamente porque vencedor de Condorcet estocástico, plusalidade de 1ºs e
posto esperado podem discordar — como de fato discordam nos nossos dados (§7).

### 5. Do dossiê à decisão: o protocolo

A pergunta prática central: *com as contagens de 1ºs, 2ºs, …, quem "ficou em
primeiro"?* As regras candidatas têm perfis distintos:

- **Plusalidade de 1ºs** ($\max b_i^1$): intuitiva, mas ignora o resto da
  distribuição — pode premiar uma alternativa polarizadora que também acumula últimos
  lugares.
- **Posto esperado** ($\min \bar{r}_i$): usa a distribuição inteira e é transitiva
  por construção; pela Prop. 2 é uma Borda probabilística — herda o perfil
  "consensual" (e a manipulabilidade teórica) da Borda.
- **Condorcet estocástico**: quando existe, é o campeão dos duelos; pode não existir
  (ciclos) e pode divergir do posto esperado.
- **Lexicográfica de aceitabilidade** (mais 1ºs; empate → mais 2ºs; …): útil como
  desempate determinístico.

**Protocolo AEO** (recomendação desta iteração):

1. **Publique a matriz de aceitabilidade completa** — ela é o resultado; qualquer
   ranking é resumo dela.
2. **Ordem final pelo posto esperado**, com desempate lexicográfico de
   aceitabilidade.
3. **Selo de robustez**: verifique o vencedor de Condorcet estocástico. Se existe e
   coincide com o 1º do posto esperado, a escolha é robusta às três leituras; se
   diverge ou não existe, **reporte a divergência** — ela é informação sobre o
   problema, não defeito do método.
4. **Empate técnico**: trate $p_{ik} \in [0{,}45;\ 0{,}55]$ como empate (cap. 10) e
   diga-o explicitamente; nunca decida um empate técnico pelo dígito.

### 6. Crenças: a leitura inversa

O vetor de pesos central $w^c_i$ resume "o que é preciso acreditar" para eleger
$a_i$ (Lahdelma & Salminen, 2001, o chamam *central weight vector*). Dois usos:

- **Prescritivo**: apresente a cada stakeholder o $w^c$ do seu candidato — "defender
  F3 é defender que Custo vale ~0,45 do peso total"; a discussão migra das
  alternativas (posições entrincheiradas) para as crenças (negociáveis).
- **Diagnóstico/inverso**: observadas as escolhas repetidas de uma decisora, o $w^c$
  das alternativas escolhidas estima a região de pesos em que suas preferências
  vivem — elicitação sem perguntar pesos. No modo **sem ordem de critérios**, o
  método vira instrumento neutro: mede a força de cada alternativa sob total
  ignorância sobre o decisor, e $b_i^1$ é a medida natural de "força intrínseca".

### 7. Experimentos

Casos dos caps. 00–13 (rankings ordinais extraídos das matrizes; $N = 20.000$,
semente 42; erro MC ≤ 0,35 p.p.).

**Caso 1 — apartamento, com ordem de pesos** (Preço ≻ Área ≻ Deslocamento ≻ Bairro):

| Alternativa | 1º | 2º | 3º | 4º | posto esp. |
|---|---|---|---|---|---|
| **A4 — Estação** | **36,4%** | 24,3% | 19,5% | 19,8% | **2,226** |
| A2 — Jardim | 19,3% | 31,3% | 28,9% | 20,6% | 2,508 |
| A1 — Centro | 23,4% | 24,7% | 28,1% | 23,7% | 2,522 |
| A3 — Parque | 20,9% | 19,7% | 23,5% | 35,9% | 2,744 |

A4 vence pelas três leituras (1ºs, posto esperado e Condorcet estocástico) — o selo
de robustez fecha. Achados finos: (i) A1 × A2 é **empate técnico puro**
($p = 50{,}04\%$) — o posto esperado os separa por 0,014, abaixo de qualquer
significância decisória; (ii) comparado ao ranking cardinal do cap. 04 (A1 vence com
os pesos 0,35/0,25/0,25/0,15), o resultado expõe que aquele vetor específico é
atípico dentro da classe ordinal Preço ≻ Área ≻ Desloc ≻ Bairro — coerente com a
varredura do cap. 11, em que A1 reinava numa janela de 4,2 p.p.

**Caso 2 — apartamento, sem ordem de pesos** (força intrínseca):

| Alternativa | 1º | posto esp. |
|---|---|---|
| A3 — Parque | **42,8%** | 2,019 |
| A1 — Centro | 35,6% | **1,993** |
| A4 — Estação | 14,9% | 2,939 |
| A2 — Jardim | 6,7% | 3,049 |

**As regras divergem**: A3 tem mais 1ºs *e* é o vencedor de Condorcet estocástico;
A1 tem o melhor posto esperado — por 0,026. Pelo protocolo: a ordem final (posto
esperado) abre com A1, o selo de robustez **não** fecha, e o relatório diz
exatamente isso: *sob ignorância total de pesos, A3 é a aposta mais frequente para o
topo, A1 a mais consistentemente bem colocada; a escolha entre os dois é uma escolha
de perfil (pico × consistência), não de cálculo.* Note ainda a utilidade do modo sem
ordem: A3, sempre 3º–4º nos métodos cardinais com os pesos do livro, é
intrinsecamente forte — os pesos do livro é que o desfavorecem.

**Caso 3 — fornecedor, com ordem** (Custo ≻ SLA ≻ Latência ≻ Suporte): F2 — Regional
vence pelas três leituras (52,999% de 1ºs, posto 1,567, Condorcet), reproduzindo em
regime puramente ordinal a robustez cardinal do cap. 11 — evidência de que a
robustez de F2 não depende de números finos. Crenças: eleger F3 exige concentrar
~0,45 do peso em Custo ($w^c_{F3} = (0{,}447; 0{,}174; 0{,}287; 0{,}092)$); as de F2
são mais equilibradas — mais um ângulo do mesmo diagnóstico.

**§7.4 — Experimento da iteração 2: o efeito do prior.** Caso âncora com ordem de
pesos, mesmos rankings, mesma semente, dois priors:

| Índice | prior AEO | prior simplexo |
|---|---|---|
| $b^1$ de A4 (fração de 1ºs) | 36,4% | **65,1%** |
| posto esperado de A4 | 2,226 | 1,557 |
| vencedor de Condorcet | A4 | A4 |
| ordem final | A4 ≻ A2 ≻ A1 ≻ A3 | A4 ≻ A2 ≻ A3 ≻ A1 |

Leitura: o prior do simplexo concentra os pesos no critério mais importante (Preço,
média 0,521 contra 0,418) e quase **dobra** a aceitabilidade de primeiro lugar de A4
— sem mudar o campeão nem o selo de Condorcet, mas invertendo a cauda (A1 cai de 3º
para 4º). Conclusão registrada: conclusões *qualitativas* (campeão, selo) foram
estáveis ao prior neste caso; conclusões *quantitativas* (magnitudes, cauda) não são
— reporte sempre o prior junto com o resultado. *Números em
`test_troca_de_prior_muda_magnitude_mas_nao_o_campeao_no_ancora`.*

### 8. Limitações e agenda de iterações

Esta é a **iteração 1** de um artigo vivo. Limitações conhecidas e agenda:

1. ~~**Prior**: comparar com o uniforme-no-simplexo e quantificar o impacto~~ —
   **concluído na iteração 2** (Prop. 5, tabela de médias e §7.4; Dirichlet genérico
   como prior paramétrico segue em aberto).
2. **Empates e ordens parciais**: a Def. 1 exige permutações completas; decisores
   reais têm empates e pares incomparáveis — estender σ e τ a pré-ordens.
3. **Correlação entre critérios**: os sorteios por critério são independentes;
   critérios correlacionados (preço × área) pedem cópulas ou sorteio conjunto.
4. **Elicitação híbrida**: aceitar informação parcial cardinal ("peso do preço está
   entre 0,3 e 0,5") restringindo a região de sorteio — aproximação com a SMAA
   clássica.
5. **Validação empírica** da leitura de crenças com decisores reais (inversão:
   escolhas → região de pesos), e estudo de identificabilidade.
6. **Produto**: expor a AEO no Decisor (`/api/aeo` já existe na etapa 14; o catálogo
   do produto aguarda a UI de entrada ordinal).

### Referências

- Lahdelma, R.; Hokkanen, J.; Salminen, P. (1998). "SMAA — Stochastic
  Multiobjective Acceptability Analysis." *EJOR*, 106(1), 137–143. DOI
  10.1016/S0377-2217(97)00163-X. ✓
- Lahdelma, R.; Salminen, P. (2001). "SMAA-2: Stochastic Multicriteria Acceptability
  Analysis for Group Decision Making." *Operations Research*, 49(3), 444–454. DOI
  10.1287/opre.49.3.444.11220. ✓
- Lahdelma, R.; Miettinen, K.; Salminen, P. (2003). "Ordinal Criteria in Stochastic
  Multicriteria Acceptability Analysis (SMAA)." *EJOR*, 147(1), 117–127. DOI
  10.1016/S0377-2217(02)00267-9. ✓
- Tervonen, T.; Figueira, J. R. (2008). "A Survey on Stochastic Multicriteria
  Acceptability Analysis Methods." *J. Multi-Criteria Decision Analysis*, 15(1–2),
  1–14. DOI 10.1002/mcda.407. ✓
- Butler, J.; Jia, J.; Dyer, J. (1997). "Simulation Techniques for the Sensitivity
  Analysis of Multi-Criteria Decision Models." *EJOR*, 103(3), 531–546. DOI
  10.1016/S0377-2217(96)00307-4. ✓
- Barron, F. H.; Barrett, B. E. (1996). "Decision Quality Using Ranked Attribute
  Weights." *Management Science*, 42(11), 1515–1523. DOI 10.1287/mnsc.42.11.1515. ✓
- Demais referências do livro: `livro/bibliografia.md`.
