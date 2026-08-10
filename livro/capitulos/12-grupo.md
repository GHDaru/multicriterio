# 12 — Decisão em grupo: agregar pessoas sem esconder o conflito

> **Estado da arte capturado em 2026-07** · última revisão 2026-08-10 · [histórico](../HISTORICO.md)

## Objetivos de aprendizagem

1. **Aplicar** duas agregações de rankings — contagem de Borda e torneio de Copeland —
   e **explicar** o que cada uma privilegia.
2. **Demonstrar** o paradoxo de Condorcet e o que ele implica para qualquer regra de
   agregação.
3. **Agregar** julgamentos AHP de vários decisores pela média geométrica (AIJ) e
   **justificar** por que a média aritmética quebraria a reciprocidade.
4. **Decidir** entre agregar *entradas* (julgamentos/pesos) e agregar *saídas*
   (rankings) — e quando cada caminho é o honesto.

## O problema

Robustez conquistada (cap. 11), resta a realidade final: decisões importantes têm
**vários decisores**. Ana olha o dinheiro, Bia a qualidade de vida, Caio o equilíbrio
— três rankings legítimos e conflitantes. "Tirar a média" parece inocente, mas
agregação de preferências é um campo minado conhecido desde o século XVIII: maiorias
que andam em círculo, vencedores que não são o favorito de ninguém, regras
manipuláveis.

## De onde isto veio

**O aperto.** Este é o capítulo mais velho do livro: dois séculos antes de existir
"MCDA", a **Académie Royale des Sciences** precisava eleger seus próprios membros — e
a literatura conta que **Jean-Charles de Borda** (engenheiro militar, acadêmico)
argumentou, num memorial apresentado à Académie (a versão impressa é de 1781), que a
pluralidade simples podia eleger alguém que a **maioria detestava**, desde que a
oposição se dividisse. O aperto era doméstico e concreto: a própria instituição usava
uma regra de votação defeituosa para decidir quem entrava.

**O que se fazia antes.** Pluralidade: conta-se só o 1º lugar de cada eleitor — e
toda a informação sobre o resto da ordem vai para o lixo (é o "quem tem mais 1ºs" que
o cap. 14 reencontra e recusa).

**A virada.** Duas, rivais desde o berço. Borda: usar a **posição inteira** do ranking
de cada eleitor (pontos por posição — o consenso). **Condorcet** (1785, no *Essai*
sobre a probabilidade das decisões): usar os **duelos majoritários** par a par — e a
descoberta desconcertante de que as maiorias podem andar em círculo (o paradoxo do
capítulo). A rivalidade nunca se resolveu — em 1951, **Arrow** provou por quê: nenhuma
regra satisfaz todos os requisitos razoáveis ao mesmo tempo (e **Copeland**, cuja
regra usamos, circula atribuído a uma nota de seminário *não publicada* de 1951 — caso
raro em que a fonte primária talvez seja inalcançável por natureza).

**A ideia reaproveitável.** **Agregação de preferências tem teoremas de
impossibilidade** — não existe regra neutra, logo a escolha da regra é parte da
decisão e deve ser feita **antes** de ver os rankings (regra escolhida depois é regra
manipulada). E: jogar fora a ordem abaixo do 1º lugar é jogar fora quase toda a
informação — lição que atravessa deste capítulo ao 14 (a Prop. 2 do Apêndice C prova
que o posto esperado da AEO *é* uma Borda média: o século XVIII vivo no método de
2026).

**O nome.** "Contagem de Borda", "paradoxo de Condorcet", "método de Copeland" — o
campo nomeia as regras pelos autores; a *social choice theory* moderna (o nome do
campo) nasce com o livro de Arrow.

| Afirmação | Selo |
|---|---|
| Borda, memorial sobre eleições (impresso 1781; apresentação anterior à Académie) e a crítica à pluralidade | ⏳ atribuição corrente; primária aberta (Gallica) bloqueada deste ambiente — na fila |
| Condorcet (1785), *Essai*, paradoxo dos ciclos | ⏳ metadados notórios; registro na fila |
| Arrow (1951), teorema da impossibilidade | ✓ᵐ (obra notória; registro a conferir na fila) |
| Copeland (1951) como nota de seminário não publicada (Michigan) | ⏳ atribuição corrente — possivelmente ❌ por natureza |
| AIJ pela média geométrica: Aczél & Saaty (1983) | ⏳ metadados na fila |

## Fundamentos

Dois caminhos (Belton & Stewart, 2002; panorama em Greco et al., 2016):

**Agregar saídas (rankings).** A **contagem de Borda** converte posição em pontos (1º
vale $m-1$, último vale 0) e soma — privilegia consenso amplo. O **método de
Copeland** disputa cada par por maioria e pontua vitórias menos derrotas — privilegia
quem vence confrontos diretos. Ambos esbarram no **paradoxo de Condorcet**: com
preferências cíclicas (X≻Y≻Z, Y≻Z≻X, Z≻X≻Y), as maiorias par a par andam em círculo e
não existe vencedor coerente — caso particular do resultado geral de Arrow de que
nenhuma regra de agregação satisfaz simultaneamente todos os critérios razoáveis de
justiça.

**Agregar entradas (julgamentos).** No AHP em grupo, a agregação canônica dos
julgamentos individuais é a **média geométrica** elemento a elemento (AIJ): é a única
média que preserva a reciprocidade ($a_{ij} = 1/a_{ji}$) — a aritmética a destrói
(média de 2 e 1/2 é 1,25, mas a de seus recíprocos não é 1/1,25). Depois, o autovetor
do cap. 05 segue normalmente.

(Bibliografia completa e status de validação: `livro/bibliografia.md`.)

## O método passo a passo

**Os três rankings** — Ana: A4 ≻ A2 ≻ A1 ≻ A3 · Bia: A3 ≻ A1 ≻ A2 ≻ A4 · Caio: A1 ≻
A4 ≻ A2 ≻ A3.

**Borda** (1º = 3 pontos): A1 = 1+2+3 = **6** · A4 = 3+0+2 = 5 · A2 = 2+1+1 = 4 ·
A3 = 0+3+0 = 3. **Copeland**: A1 vence os três duelos (sempre por 2 votos a 1) →
+3; A4 → +1; A2 → −1; A3 → −3.

| # | Alternativa | Borda | Copeland |
|---|---|---|---|
| 1 | **A1 — Centro** | **6** | **+3** |
| 2 | A4 — Estação | 5 | +1 |
| 3 | A2 — Jardim | 4 | −1 |
| 4 | A3 — Parque | 3 | −3 |

O achado didático: **A1 vence nas duas regras sem ter sido o 1º de ninguém** —
agregação de grupo tende a eleger o consenso, não o favorito. E o contraexemplo
obrigatório: no ciclo de Condorcet, Copeland dá 0 a todos e Borda empata todos — a
regra devolve o empate porque o grupo *de fato* não tem vencedor.

**AIJ**: Ana usa a matriz de julgamentos do cap. 05 (peso do Preço 0,4236); Bia julga
quase tudo igual. A média geométrica preserva reciprocidade (testado elemento a
elemento) e o peso do Preço do **grupo** cai para um valor entre os dois — com CR
ainda consistente. *Todos os números são testes da etapa 12.*

## Quando usar (e quando não)

Agregue **entradas** (julgamentos, pesos, funções de valor) quando o grupo compartilha
a mesma matriz de decisão e quer um modelo único auditável — a discussão acontece nos
insumos, onde é mais produtiva. Agregue **saídas** (rankings) quando os decisores
usaram modelos diferentes ou quando os insumos são confidenciais — sabendo que Borda e
Copeland podem discordar entre si e que ciclos são possíveis. Em qualquer caminho:
reporte o conflito (quem discordou de quê), não só o agregado — esconder a divergência
é a forma mais rápida de perder o comitê. E lembre o cap. 10: empate técnico existe em
grupo também.

### Leitura executiva

Agregar pessoas não é como agregar critérios: não há pesos "verdadeiros" entre seres
humanos, e a teoria garante que toda regra tem pontos cegos. Borda elege consenso,
Copeland elege gladiador, AIJ constrói o julgamento médio com matemática honesta —
e Condorcet lembra que às vezes o grupo genuinamente não decidiu. **O que levar**
hoje: escolha a regra **antes** de ver os rankings (regra escolhida depois é regra
manipulada) e apresente sempre o mapa da divergência junto com o resultado.

## Mão na massa — decisor-zero, etapa 12

Em `decisor-zero/etapas/12-grupo/`, nasce `motor/grupo.py` (Borda, Copeland, AIJ
reaproveitando o autovetor da etapa 05) com rotas `POST /api/grupo/rankings` e
`POST /api/grupo/julgamentos`; a página traz o comitê Ana/Bia/Caio e o botão do
paradoxo. Decisão da rodada: agregação de grupo fica na trilha; no produto ela entra
junto com contas de usuário (spec futura — hoje o produto não tem noção de "vários
decisores"). Exercício de completar: implemente a checagem de **vencedor de
Condorcet** (existe alternativa que vence todos os duelos?) e devolva-a quando
existir, com teste para os dois cenários da página.

## Segundo domínio — o comitê de tecnologia

Três personas ranqueiam os fornecedores: Financeiro (F3 ≻ F2 ≻ F1), Confiabilidade
(F1 ≻ F2 ≻ F3) e Latência (F2 ≻ F3 ≻ F1). **Borda: F2 = 4 > F3 = 3 > F1 = 2 ·
Copeland: F2 = +2 > F3 = 0 > F1 = −2.** De novo o padrão do consenso — F2 vence com um
único 1º lugar — mas com um detalhe novo: Financeiro e Confiabilidade são
**perfeitamente opostos** (rankings invertidos, ρ de Spearman = −1), e é o terceiro
voto que desempata tudo. Comitês polarizados dão poder desproporcional ao voto do
meio; vale reportar a polarização junto com o agregado. *Teste
`test_segundo_dominio_comite_polarizado` da etapa 12.*

## Verificação

1. Refaça a contagem de Borda de A4 e explique por que ela fica atrás de A1 mesmo com
   um 1º lugar. (Dica: objetivo 1 — consenso × favoritismo.)
2. No ciclo X/Y/Z, o que exatamente "não existe"? Um ranking? Um vencedor? (Dica:
   objetivo 2 — maiorias par a par.)
3. Mostre com um par de números por que a média aritmética de julgamentos AHP quebra
   $a_{ij} \cdot a_{ji} = 1$. (Dica: objetivo 3 — use 2 e 1/2.)

---

## Apêndice A — decisão em grupo nas ferramentas

- **pyDecision** inclui variantes de grupo (fuzzy AHP em grupo, agregações) com
  notebooks (<https://github.com/Valdecy/pyDecision>).
- **1000minds** e **M-MACBETH** têm módulos comerciais de decisão em grupo — úteis
  como referência de UX para a futura spec de multiusuário do Decisor.
- O capítulo de decisão em grupo de Greco, Ehrgott & Figueira (2016) é o survey de
  referência (<https://link.springer.com/book/10.1007/978-1-4939-3094-4>).

## Apêndice B — gabarito comentado da Verificação

1. A4 soma 3 (1º de Ana) + 0 (último de Bia) + 2 (2º de Caio) = 5. O 1º lugar de Ana
   não compensa o último de Bia — Borda pune rejeição forte tanto quanto premia
   favoritismo. A1, sem nenhum 1º lugar, nunca é rejeitada (2º, 2º, 1º… no mínimo 3º)
   e soma mais.
2. O que não existe é um **vencedor de Condorcet** — uma alternativa que vença todas
   as outras nos duelos por maioria — e, mais forte, qualquer ordenação coerente com
   as maiorias par a par (elas formam um ciclo). Rankings individuais existem;
   coletivo coerente, não.
3. Julgamentos 2 e 1/2: média aritmética = 1,25; média dos recíprocos (1/2 e 2)
   também = 1,25 — mas o recíproco de 1,25 é 0,8 ≠ 1,25. A matriz média deixaria de
   ser recíproca. Média geométrica: √(2 · 1/2) = 1 e √(1/2 · 2) = 1 — reciprocidade
   intacta.
