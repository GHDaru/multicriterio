# 11 — Sensibilidade, robustez e rank reversal: quando confiar no ranking

> **Estado da arte capturado em 2026-07** · última revisão 2026-08-13 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Executar** uma varredura de peso e **interpretar** a faixa de estabilidade do
   vencedor.
2. **Comparar** rankings de métodos diferentes com a correlação de Spearman e
   **distinguir** robustez de método de robustez de pesos.
3. **Demonstrar** o rank reversal em métodos com normalização relativa ao conjunto —
   e **explicar** por que uma alternativa de último lugar consegue mexer no pódio.
4. **Montar** o protocolo de robustez do livro: o que reportar junto com qualquer
   ranking.

## O problema

O livro inteiro vem plantando desconfianças: o pódio virou com o vetor de pesos (cap.
04), com julgamentos AHP (cap. 05), com funções de valor (cap. 07), com funções de
preferência (cap. 08) — e o VIKOR institucionalizou o empate técnico (cap. 10). A
pergunta que falta responder com instrumento, não com opinião: **o ranking que vou
reportar sobrevive a perturbações razoáveis?**

## Fundamentos

Três instrumentos, todos baratos:

- **Varredura de peso**: varie o peso de um critério de 0 a 1 (renormalizando os
  demais proporcionalmente) e registre em que faixas cada vencedor reina. A largura da
  faixa do vencedor atual é sua margem de segurança (prática padrão em MCDA; Belton &
  Stewart, 2002).
- **Concordância entre métodos**: rode SAW, TOPSIS, PROMETHEE II e VIKOR com os mesmos
  insumos e meça a correlação de Spearman entre os rankings — é o desenho experimental
  dos estudos comparativos (Wątróbski et al., 2018; Nguyen et al., 2025 mostram que a
  divergência entre métodos é comum, não patologia).
- **Ensaio de rank reversal**: acrescente uma alternativa e verifique se a ordem
  *relativa* das originais muda. A vulnerabilidade nasce de toda referência **relativa
  ao conjunto**: min/max da normalização (SAW), ideal/anti-ideal (TOPSIS —
  García-Cascales & Lamata, 2012), estrutura de comparações (AHP — Belton & Gear,
  1983; o mecanismo já aparece descrito no próprio Saaty de 1977, cap. 05).

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**Passo 1 — varredura do peso do Preço (SAW, caso âncora):**

| peso do Preço | vencedor |
|---|---|
| 0,000 – 0,315 | A3 — Parque |
| **0,316 – 0,357** | **A1 — Centro** |
| 0,358 – 1,000 | A4 — Estação |

O reinado de A1 é uma janela de **4,2 pontos percentuais** — e o nosso 0,35 está a
0,008 da fronteira. A leitura executiva do cap. 04 ("a corrida é apertada") agora tem
número.

**Passo 2 — concordância entre métodos**: com os pesos do rating direto, os quatro
métodos devolvem exatamente A1 > A4 > A3 > A2 — $\rho = 1{,}0$ em todos os pares.
Robustez **de método**: total. Mas o passo 1 mostrou que a robustez **de pesos** é
estreita — são perguntas diferentes, e é por isso que se reportam as duas.

**Passo 3 — o ensaio de rank reversal.** Entra A5 — Colinas (R$ 430 mil, 59 m², 24
min, bairro 1), que termina em **último** em qualquer método. Ainda assim:

- **TOPSIS**: antes A1 > A4 > A3 > A2; depois **A1 > A3 > A4 > A2** — A3 e A4 trocam
  de lugar. O bairro 1 de A5 moveu o anti-ideal, e a régua de todo mundo mudou.
- **SAW**: o mesmo A5 estica a amplitude da coluna Bairro no min-max e o **vencedor
  troca** — A4 assume a frente.

Uma alternativa irrelevante não é inofensiva: ela muda as âncoras. *Todos os números
dos passos 1–3 são testes da etapa 11.*

**Passo 4 — o protocolo do livro.** Todo ranking reportado vem com: (a) o vetor de
pesos e sua origem (cap. 03); (b) a faixa de estabilidade do vencedor; (c) a
concordância entre ≥ 2 métodos de famílias diferentes; (d) o veredito do VIKOR sobre
vantagem aceitável; (e) aviso explícito se alternativas podem entrar/sair do conjunto.

## Quando usar (e quando não)

Sempre — este capítulo é o controle de qualidade dos anteriores. O custo é desprezível
(milissegundos) perto do custo de defender um ranking frágil em público. O que a
análise de sensibilidade **não** faz: consertar estruturação ruim (caps. 01–02) ou
substituir a conversa sobre pesos — ela apenas revela onde a conversa importa.

### Leitura executiva

Um ranking sem análise de sensibilidade é uma fotografia sem legenda: você não sabe se
o vencedor ganhou por robustez ou por 0,008 de peso. No caso âncora, os quatro métodos
concordam (ρ = 1), mas A1 reina numa janela de 4 pontos de peso e perde o trono se um
candidato medíocre entrar no conjunto. **O que levar** hoje: adote o protocolo do
passo 4 como formato padrão de entrega — ranking sem margem declarada é opinião com
casas decimais.

## Mão na massa — decisor-zero, etapa 11

Em `decisor-zero/etapas/11-sensibilidade/`, nasce `motor/sensibilidade.py`
(varredura, Spearman, comparação e ensaio de reversal) com rotas e página para os três
instrumentos. O produto ganhou `POST /api/decisoes/{id}/comparar` (rankings dos 4
métodos + matriz de Spearman + concordância média). Exercício de completar: implemente
a varredura **bidimensional** (dois pesos simultâneos, mapa de regiões de vitória) e
mostre em teste o ponto (w_Preço, w_Área) mais próximo do atual em que A3 vence.

## Segundo domínio — a fotografia da robustez

Aplicando o protocolo inteiro ao fornecedor, o contraste com o apartamento vira
número:

| Instrumento | Apartamento | Fornecedor |
|---|---|---|
| Faixa de estabilidade do vencedor (peso do 1º critério) | A1: [0,316; 0,358) — 4,2 p.p. | F2: [0; 0,561) — **56 p.p.** |
| Concordância entre os 4 métodos | ρ = 1 | ρ = 1 |
| Quem nunca vence na varredura | — | F1 (nenhum peso de Custo o elege) |

F2 vence com qualquer peso de Custo até 0,561 — treze vezes a janela de A1 — e a
Hiperescala não existe peso que salve. Mesmo protocolo, fotografias opostas: uma
decisão pede cautela e conversa sobre pesos; a outra pode ser assinada hoje. *Teste
`test_segundo_dominio_faixa_larga_e_f1_nunca_vence` da etapa 11.*

## Verificação

1. Por que renormalizar os demais pesos na varredura, em vez de só aumentar um?
   (Dica: objetivo 1 — Σw = 1.)
2. ρ = 1 entre métodos e faixa de estabilidade estreita: o que cada um diz, e qual
   preocupa mais neste caso? (Dica: objetivo 2.)
3. Explique em uma frase por que A5, em último lugar, mexeu no pódio do TOPSIS.
   (Dica: objetivo 3 — o que A5 fez com o anti-ideal.)

---

## Apêndice A — sensibilidade nas ferramentas

- **pymcdm** traz correlações de ranking prontas (`pymcdm.correlations`: Spearman,
  pesos de ranking, WS) e helpers de comparação
  (<https://github.com/kotbaton/pymcdm>).
- O framework de seleção de métodos de Wątróbski et al. (2018) tem ferramenta web
  associada — útil como segunda opinião sobre "qual método cabe no meu problema"
  (<https://arxiv.org/abs/1810.11078>).
- **pyDecision** publica notebooks comparando métodos no mesmo dataset
  (<https://github.com/Valdecy/pyDecision>).

## Apêndice B — gabarito comentado da Verificação

1. Porque Σw = 1 é parte da definição (cap. 01): aumentar um peso sem renormalizar
   criaria um vetor inválido, e a comparação entre pontos da varredura deixaria de ser
   justa — cada ponto precisa ser um modelo legítimo completo.
2. ρ = 1 diz que a *régua* não importa (as quatro filosofias concordam); a faixa
   estreita diz que o *insumo* importa demais (0,008 de peso vira outro vencedor).
   Preocupa mais a faixa: métodos são escolha nossa, pesos são elicitação imperfeita
   de gente — e é aí que a decisão está por um fio.
3. O bairro 1 de A5 esticou a coluna Bairro e moveu o **anti-ideal** — a referência de
   "pior" de todo mundo. Distâncias mudam, C_i muda, e a ordem relativa de A3/A4, que
   já era apertada, vira. Uma frase: *no TOPSIS, cada alternativa é medida contra
   extremos que pertencem ao conjunto — mude o conjunto, mude a régua.*
