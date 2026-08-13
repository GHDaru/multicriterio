# Histórico — este é um livro vivo

> Princípio IV da constituição (`.specify/memory/constitution.md`): o que este livro
> descreve tem data; toda edição fica registrada aqui, com o modelo de IA usado.

## Como ler as datas do livro

- **Data do evento** — quando algo aconteceu no mundo (ex.: publicação de um paper);
  vive no corpo do texto e não muda.
- **Data de captura** — o "estado da arte capturado em AAAA-MM" no cabeçalho de cada
  capítulo: quando as fontes, bibliotecas e links foram verificados pela última vez.
- **Rodada** — o ciclo spec-kit (`specs/NNN-*`) que produziu ou revisou o conteúdo.

## Tabela de snapshot por capítulo

| Capítulo | Estado da arte capturado em | Etapa testada | Última revisão |
|---|---|---|---|
| 00 Introdução | 2026-07 | ✓ (etapa 00) | 2026-08-13 |
| 01 O problema multicritério | 2026-07 | ✓ (etapa 01) | 2026-08-13 |
| 02 Estruturação e dominância | 2026-07 | ✓ (etapa 02) | 2026-08-13 |
| 03 Normalização e pesos | 2026-07 | ✓ (etapa 03) | 2026-08-13 |
| 04 SAW — o método aditivo | 2026-07 | ✓ (etapa 04) | 2026-08-13 |
| 05 AHP | 2026-07 | ✓ (etapa 05) | 2026-08-13 |
| 06 TOPSIS | 2026-07 | ✓ (etapa 06) | 2026-08-13 |
| 07 MAVT e Even Swaps | 2026-07 | ✓ (etapa 07) | 2026-08-13 |
| 08 PROMETHEE | 2026-07 | ✓ (etapa 08) | 2026-08-13 |
| 09 ELECTRE | 2026-07 | ✓ (etapa 09) | 2026-08-13 |
| 10 VIKOR e BWM | 2026-07 | ✓ (etapa 10) | 2026-08-13 |
| 11 Sensibilidade e rank reversal | 2026-07 | ✓ (etapa 11) | 2026-08-13 |
| 12 Decisão em grupo | 2026-07 | ✓ (etapa 12) | 2026-08-13 |
| 13 Do protótipo ao produto | 2026-07 | ✓ (etapa 13) | 2026-08-13 |
| 14 AEO (contribuição original) | 2026-07 | ✓ (etapa 14) · artigo iteração 2 | 2026-08-13 |

## Edições

### Edição 0.39 — 2026-08-13 · o produto vai ao ar: Railway + Neon (spec 039, ADR 0010)

- Nascem os artefatos de deploy do **produto** (o livro já estava publicado desde a
  rodada 003): `Dockerfile`, `.dockerignore`, `railway.json` (builder Dockerfile,
  healthcheck em `/health`, restart on-failure) e o runbook `app/DEPLOY.md`, com
  verificação obrigatória pós-deploy, rollback por redeploy e dry-run de esquema por
  branch do Neon.
- **Decisão (ADR 0010)**: backend e frontend no mesmo serviço do Railway — o front é
  um HTML sem build servido pela própria API, e separá-lo hoje custaria CORS, duas
  URLs e dois pipelines para ganhar CDN em um arquivo. O Vercel fica registrado com
  gatilho de revisão explícito.
- Cap. 13 registra o degrau cumprido e a medida do acoplamento com o provedor: um
  processo que escuta em `$PORT` e recebe `DATABASE_URL`.
- Limites declarados no runbook: sem migrações (o start faz `create_all`), sem
  autenticação no v0, dependências sem pin.
- **IA**: agente **Claude Code (Anthropic)**; execução do deploy e segredos: Steward.

### Edição 0.38 — 2026-08-13 · fila encerrada: caps. 05 e 10 fecham suas origens (spec 038)

- **Forman & Gass (2001) lido** — a gênese do AHP sai do "a literatura atribui" e vira
  narrativa documentada no cap. 05: no fim dos anos 1960, dirigindo pesquisa da ACDA,
  Saaty recrutou teóricos de primeira linha (**Debreu, Harsanyi e Selten**, futuros
  Nobel) e o resultado decepcionou — pelo relato dele próprio, modelos abstratos
  demais para avaliar trocas entre sistemas de armas, e advogados redigindo a posição
  americana sem saber avaliá-las melhor. O incômodo, anos depois na Wharton, gerou o
  método. A cena de "1971, DoD" some do corpo do texto: **não aparece em nenhuma das
  quatro fontes lidas**, inclusive nas duas retrospectivas do próprio Saaty.
- **Opricovic & Tzeng (2007) lido** — e o cap. 10 ganha uma correção de origem: a
  medida $L_p$ que gera S e R vem de **Duckstein & Opricovic (1980), sobre bacias
  hidrográficas**; o planejamento pós-terremoto é **aplicação** documentada de 2002,
  não a gênese que a literatura didática repete. Belgrado confirmado.
- **A fila de verificação está encerrada**: 11 de 11 itens resolvidos, 9 por leitura
  de fonte. Saldo da rodada inteira: quatro correções ao que já estava publicado.
- **IA**: agente **Claude Code (Anthropic)**; fontes fornecidas pelo Steward.

### Edição 0.37 — 2026-08-13 · obituário da IJAHP (raia leve, spec 037)

- O obituário de Saaty na IJAHP (Assad, 2017) é **acesso aberto e alcançável** desta
  máquina: acrescenta ao cap. 05 as passagens pelo **Office of Naval Research**, pela
  embaixada dos EUA em Londres e pelo Navy Management Office, o doutorado em Yale e a
  ida de Wharton para a Katz School (Pittsburgh) em 1979. Também **não** menciona a
  cena de 1971 — que segue ⏳ com o livro de 1980 como candidata.
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana no gate.

### Edição 0.36 — 2026-08-13 · três fontes lidas: caps. 04, 06 e 08 na origem (spec 036)

- **Churchman & Ackoff (1954) lido** — e o cap. 04 muda de tese. A soma ponderada não
  é "método sem cena de invenção": ela entra na literatura por uma **réplica** a um
  trabalho que media valor por "estados-armadilha" (ganhar ou perder uma guerra), com
  o contraexemplo do enxadrista que quer perder para alguém de quem gosta. Correção
  registrada: as hipóteses de aditividade e **seus casos de falha** já estão no artigo
  de 1954 — não é verdade que a teoria só chegou com Fishburn em 1967.
- **Hwang & Yoon (1981) lido** (prefácio e sumário) — o cap. 06 troca o ❌ por
  contexto documentado: sequência do levantamento anterior dos autores, **dezessete**
  métodos classificados, financiamento do **Office of Naval Research** e do DoE,
  dívida com MacCrimmon, e o rascunho **testado numa turma de 1980**. Persiste (agora
  bem menor) a lacuna: o prefácio não narra o momento da ideia das duas distâncias.
- **Brans & Vincke (1985) lido** — a conferência de 1982 se confirma pela referência
  dos próprios autores, **com correção**: "L'ingénierie de la décision" é o título da
  comunicação de Brans em Laval (agosto de 1982), não o nome do colóquio. Também
  confirmado: o objetivo declarado de no máximo dois parâmetros com significado
  econômico (era leitura editorial, vira ✓) e a submissão em junho de 1982 para
  publicação só em 1985.
- Nota de pesquisa: a conexão nº 1 (financiamento militar) passa de suposição a
  documento em três fontes independentes. Placar da fila: **10 de 11 itens fechados**;
  restam Opricovic (VIKOR) e a cena de 1971 do AHP (item 2b).
- **IA**: agente **Claude Code (Anthropic)**; fontes fornecidas pelo Steward.

### Edição 0.35 — 2026-08-13 · Saaty (1977) lido: o cap. 05 na fonte (spec 035)

- O artigo seminal do AHP foi lido na íntegra (exemplar fornecido pelo Steward) e o
  cap. 05 passa a falar da fonte, não de segunda mão. Fechado o ⏳ **"Wharton"** (está
  na folha de rosto); entram com selo ✓ a premissa de projeto (a inconsistência humana
  é acomodada, não proibida), a âncora em **Miller (1956)** para a hierarquia e o teto
  da escala 1–9, as **validações contra respostas conhecidas** (distâncias a
  Filadélfia, lei do inverso do quadrado, riqueza de nações) e as aplicações
  declaradas (Sudão, Marinha dos EUA, corporação mexicana, NSF).
- **Dois achados que a literatura didática não conta**: (1) a **semente do rank
  reversal está no próprio artigo de 1977**, seis anos antes de Belton & Gear — Saaty
  registra que retirar uma atividade não redistribui seu peso proporcionalmente
  (removida a URSS do exemplo de riqueza, a razão EUA/Japão vai de 3,47 a 2,74); os
  caps. 05 e 11 passam a registrar isso. (2) **Achado negativo**: a cena fundadora
  "outono de 1971, planejamento de contingência para o DoD" **não aparece** no artigo
  — nem 1971, nem DoD, nem ACDA; os agradecimentos citam dois colegas e o parecerista.
  A atribuição continua ⏳, com a introdução do livro de 1980 como última candidata.
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana no gate.

### Edição 0.34 — 2026-08-13 · varredura Unpaywall/Semantic Scholar (raia leve, spec 034)

- Pedido de usar Sci-Hub **recusado** (violaria direitos autorais); em seu lugar, os
  DOIs em aberto passaram pelo Unpaywall e pelo Semantic Scholar (rotas legais de
  acesso aberto). Sem cópia OA para Saaty 1977, Churchman & Ackoff 1954 e Brans &
  Vincke 1985 — mas a varredura rendeu dois metadados: o DOI direto do artigo de 1954
  (10.1287/opre.2.2.172, cap. 04) e o título catalogado completo do paper do
  PROMETHEE — "**Note**—…" — que entrou na *Management Science* como nota, rimando
  com a carta ao editor de Fishburn (cap. 08 registra o paralelo).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana no gate.

### Edição 0.33 — 2026-08-13 · fila varrida até o fim pela rota Internet Archive (spec 033)

- **Mais dois itens fechados por leitura**: **Condorcet (1785)** — folha de rosto e o
  paradoxo na formulação original ("de duas quaisquer das três proposições resulta
  uma conclusão contrária à terceira", *Discours préliminaire*) — selo ✓ no cap. 12;
  **Churchman, Ackoff & Arnoff (1957)** — capítulo "Weighting Objectives" lido na
  íntegra: método das comparações sucessivas (contraprova por redundância, vinte anos
  antes do CR), a crítica aos "intangíveis" e o caso executivo — cap. 04 reescrito
  com selo ✓; o artigo de 1954 corroborado pelos "Comments" do mesmo fascículo (✓ᵐ).
- **Quatro itens esgotados pela rota e documentados**: Saaty (1977) e Hwang & Yoon
  (1981) existem no IA só como empréstimo (403/401); Brans (1982) e Opricovic não têm
  exemplar. Ficam abertos com o registro da tentativa — fechá-los agora exige paywall
  ou biblioteca física.
- Placar da fila: **7 de 11 itens fechados** (4 por leitura integral de fonte
  primária: Roy, Franklin, Borda, Condorcet + o manual de 1957).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana no gate.

### Edição 0.32 — 2026-08-13 · revisão editorial + fontes fechadas na fila (spec 032)

- **Revisão de humanização** (livro inteiro): cortados os tiques verbais em cluster
  ("exatamente" ×30 → ×18, mantidos só os literais; "brilha" repetido variado),
  corrigido o typo "plusalidade" (2×) no Apêndice C e atualizado o "iteração 1"
  residual (cap. 14 e §8 do artigo) para iteração 2. Voz do livro (travessão, negrito
  estrutural, "O que levar") preservada — é a voz do autor, não cacoete de IA.
- **Fila de verificação: 5 itens fechados** pela rota Internet Archive (Gallica e
  founders.archives.gov seguem bloqueados; as mesmas obras existem lá em edição
  aberta): **Franklin → Priestley lida** (Smyth vol. V — colunas Pró/Contra, 3–4 dias,
  "Moral or Prudential Algebra", e o "não o quê, mas como" que antecipa Roy em dois
  séculos) e **Borda lido** (volume da Académie de 1781 — 21 eleitores, metáfora dos
  atletas, e a nota de rodapé datando a apresentação em **16/06/1770**); Aczél &
  Saaty (1983), Shannon (1948) e Arrow (1951) conferidos por registro (✓ᵐ). Selos
  promovidos nos caps. 03, 07 e 12; nota de pesquisa atualizada (restam 5 itens,
  incluindo o novo: Condorcet no Internet Archive).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana no gate.

### Edição 0.31 — 2026-08-10 · "De onde isto veio" nos 11 capítulos de método (spec 031)

- Primeira aplicação integral do Princípio VIII: os caps. 02–10, 12 e 14 ganham a
  seção **"De onde isto veio"** (aperto → antes → virada → ideia reaproveitável →
  nome + tabela de selos), consumindo a nota de pesquisa histórica. Destaques: a
  história do ELECTRE com selo ✓ (lida na fonte — SEMA 1966, três autores, manual de
  programa, CDC); a do AHP ancorada no obituário INFORMS (ACDA 1961–69); a lacuna do
  TOPSIS admitida (❌ sem cena fundadora); o fio ordinal Borda 1781 → ROC → AEO
  costurando os caps. 03, 12 e 14. Caps. 00, 01, 11 e 13 (conceituais/operacionais)
  omitem a seção, conforme o guia.
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana no gate.

### Edição 0.30 — 2026-08-10 · Princípio VIII: "Nenhum método cai do céu" (spec 030, ADR 0009)

- **Emenda constitucional v1.1.0** (texto integral do autor): todo capítulo de método
  ganha a seção obrigatória **"De onde isto veio"** (aperto → o que se fazia antes →
  virada → ideia reaproveitável → nome), com selo por afirmação histórica
  (✓ · ✓ᵐ · ⏳ · ❌ · 📖) e três proibições (gênio solitário, curiosidade decorativa,
  mistura de registro). Esqueleto v3 atualizado no guia editorial.
- Nasce a **nota de pesquisa histórica** (`estudos/nota-pesquisa-historia-mcda.md`),
  produzida em sessão única com leitura real de fonte: Roy (1968) lido na íntegra —
  ELECTRE nasce como nota interna da SEMA (1966, Benayoun/Roy/Sussmann, manual de
  programa, CDC ≤100 objetos) e o acrônimo famoso **não está** no artigo (achado
  negativo); obituário INFORMS de Saaty lido (ACDA 1961–69 → Penn 1969). Fila de
  verificação com 9 itens abertos. A inserção das seções nos capítulos é a spec 031.
- **IA**: agente **Claude Code (Anthropic)**; princípio e texto do autor (Steward).

### Edição 0.29 — 2026-07-31 · AEO iteração 2: a matemática do prior (spec 029)

- A conjectura do autor sobre os valores médios do sorteio vira a **Proposição 5** do
  artigo: densidade do prior AEO ∝ max(v)^(−m); para m=2, E = (ln 2, 1−ln 2) ≈
  (0,693; 0,307) — e o palpite 0,75 × 0,25 é exatamente a média do prior do simplexo
  (ROC). Motor ganha os dois priors; experimento §7.4 mede o impacto (aceitabilidade
  de A4 quase dobra; campeão estável). Etapa 14: `14 passed`.
- **IA**: agente **Claude Code (Anthropic)**; método e conjectura do autor (Steward).

### Edição 0.28 — 2026-07-31 · contribuição original: AEO (spec 028, ADR 0008)

- Nasce o cap. 14 — **Agregação Estocástica Ordinal** (método do autor: só ordens,
  simulação de funções de importância, matriz de aceitabilidade, protocolo de decisão,
  pesos centrais/"crenças") — e o **Apêndice C**, artigo vivo completo (iteração 1)
  com formalização, 4 proposições provadas, algoritmo, experimentos e agenda.
- Posicionamento bibliográfico verificado: família SMAA (6 fontes ✓).
- Etapa `14-simulacao-ordinal`: motor `simular_aeo` reprodutível por semente +
  `POST /api/aeo` + página; `8 passed` (dominância com prob. 1, simetria, números do
  capítulo, divergência entre regras, crenças, reprodutibilidade).
- **IA**: agente **Claude Code (Anthropic)**; método e direção do autor (Steward);
  curadoria humana a posteriori.

### Edições 0.14+ — 2026-07-31 · rodada de aprofundamento (specs 014–027, ADR 0007)

Uma edição por capítulo; fórmula uniforme: segundo domínio (fornecedor de nuvem)
worked com números em teste + Apêndice B (gabarito comentado) + promoções de fonte.

- **0.27 (spec 027, cap. 13)**: o acervo com os dois domínios; gabarito; etapa 13
  `4 passed`. **Corrida de aprofundamento completa: caps. 00–13.**
- **0.26 (spec 026, cap. 12)**: comitê polarizado no B2B; gabarito; etapa 12
  `7 passed`.
- **0.25 (spec 025, cap. 11)**: a fotografia da robustez (56 × 4,2 p.p.); gabarito;
  etapa 11 `7 passed`.
- **0.24 (spec 024, cap. 10)**: VIKOR B2B — DQ embute o tamanho do conjunto;
  gabarito; etapa 10 `7 passed`.
- **0.23 (spec 023, cap. 09)**: ELECTRE B2B (kernel {F2, F3}); gabarito; etapa 09
  `6 passed`.
- **0.22 (spec 022, cap. 08)**: fluxos B2B (F1 perde os duelos); gabarito; etapa 08
  `6 passed`.
- **0.21 (spec 021, cap. 07)**: curvas B2B (limiar de SLA, orçamento); gabarito;
  etapa 07 `6 passed`.
- **0.20 (spec 020, cap. 06)**: TOPSIS B2B com validação pymcdm; gabarito; etapa 06
  `6 passed`.
- **0.19 (spec 019, cap. 05)**: AHP do CTO no B2B (CR=0,0038); gabarito; etapa 05
  `9 passed`.
- **0.18 (spec 018, cap. 04)**: SAW B2B — vitória robusta (margem 17× maior);
  gabarito; etapa 04 `8 passed`.
- **0.17 (spec 017, cap. 03)**: entropia quase uniforme no B2B como diagnóstico;
  gabarito; etapa 03 `21 passed`.
- **0.16 (spec 016, cap. 02)**: F4 — Revenda dominada por dois candidatos
  (diagnóstico de redundância); gabarito; etapa 02 `9 passed`.
- **0.15 (spec 015, cap. 01)**: modelagem e soma crua do segundo domínio ("elege o
  mais caro de novo"); gabarito; etapa 01 `12 passed, 1 skipped`.
- **0.14 (spec 014, cap. 00)**: segundo domínio apresentado; etapa 00 ganha
  `/api/caso-fornecedor` e testes (`2 passed`).

### Edição 0.13 — 2026-07-31 · Do protótipo ao produto (spec 013) — TRILHA COMPLETA

- Capítulo 13 (porta de persistência, Neon + fallback SQLite, credenciais, /health,
  degraus de infra futuros); etapa `13-persistencia` com a prova de sobrevivência ao
  reinício; `GET /health` no produto. **Os 14 capítulos do SUMARIO estão publicados,
  cada um com etapa executável testada.**
- Varredura final da long run: todas as etapas + produto + build estrito verdes
  (qa-report 013).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.12 — 2026-07-31 · Decisão em grupo (spec 012, long run ADR 0006)

- Capítulo 12 (Borda × Copeland — "A1 vence sem ser o 1º de ninguém"; paradoxo de
  Condorcet; AIJ por média geométrica); etapa `12-grupo`.
- **Verificação**: etapa `6 passed` (qa-report 012).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.11 — 2026-07-31 · Sensibilidade e rank reversal (spec 011, long run ADR 0006)

- Capítulo 11 (varredura de peso — A1 reina só em [0,316; 0,358); ρ=1 entre os 4
  métodos; rank reversal real: A5 de último lugar troca A3/A4 no TOPSIS e o VENCEDOR
  no SAW; protocolo de robustez do livro); etapa `11-sensibilidade`;
  `POST /api/decisoes/{id}/comparar` no produto.
- **Verificação**: etapa `5 passed`; app `21 passed` (qa-report 011).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.10 — 2026-07-31 · VIKOR e BWM (spec 010, long run ADR 0006)

- Capítulo 10 (S/R/Q, condições C1/C2 e o conjunto de compromisso {A1, A4} do caso
  âncora; BWM com 2n−3 comparações e ξ); etapa `10-vikor-bwm` (VIKOR validado contra
  pymcdm; BWM via linprog, forma exata no caso consistente); `vikor` no produto.
- **Verificação**: etapa `6 passed`; app `20 passed` (qa-report 010).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.9 — 2026-07-31 · ELECTRE (spec 009, long run ADR 0006)

- Capítulo 09 (concordância/discordância/veto/kernel; "não ranquear" como resposta
  honesta); etapa `09-electre` com três cenários em teste (relação vazia → shortlist
  {A1, A3} → veto devolvendo A2). Fora do catálogo de ranking do produto por design.
- **Verificação**: etapa `5 passed` (qa-report 009).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.8 — 2026-07-31 · PROMETHEE (spec 008, long run ADR 0006)

- Capítulo 08 (fluxos φ, degrau × V-shape com o salto de A3); etapa `08-promethee`
  validada contra a pymcdm; `promethee2` no catálogo do produto. Incidente didático
  registrado no spec: a primeira versão do teste de propriedade do V-shape estava
  errada — virou lição do capítulo.
- **Verificação**: etapa `5 passed`; app `19 passed` (qa-report 008).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.7 — 2026-07-31 · MAVT e Even Swaps (spec 007, long run ADR 0006)

- Capítulo 07 (funções de valor por partes, independência preferencial, Even Swaps);
  etapa `07-funcoes-de-valor` com as provas "linear ≡ SAW" e "curvas mudam o pódio
  sem tocar nos pesos" (A2: 4º → 2º). MAVT fora do produto até UI de curvas.
- **Verificação**: etapa `5 passed` (qa-report 007).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.6 — 2026-07-31 · TOPSIS (spec 006, long run ADR 0006)

- Capítulo 06 (ideal/anti-ideal, C_i, rank reversal específico apontado); etapa
  `06-topsis` com validação pymcdm a 1e-6; `topsis` no catálogo do produto.
- **Verificação**: etapa `5 passed`; app `18 passed` (qa-report 006).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.5 — 2026-07-31 · AHP (spec 005, long run ADR 0006)

- Capítulo 05 (autovetor, CI/CR, debate Belton & Gear/Dyer; AHP como técnica de pesos
  por decisão do ADR 0006); etapa `05-ahp` com página interativa de julgamentos;
  `/api/pesos` do produto ganha `ahp` (recusa CR > 0,10). Fontes: 6 promovidas a ✓.
- **Verificação**: etapa `8 passed`; app `17 passed` (qa-report 005).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana a posteriori (ADR 0006).

### Edição 0.4 — 2026-07-31 · SAW: o primeiro ranking (spec 004)

- Capítulo 04 (agregação aditiva: fórmula, premissas — independência preferencial,
  escala de intervalo, compensação total — e o processo SMART) no esqueleto v3; o
  worked example central é a virada de ranking: rating direto elege A1, ROC elege A4,
  mesma matriz e mesma ordem de importância.
- Etapa `04-saw`: motor aditivo puro + rota + página com os dois vetores de pesos;
  **validação cruzada com pymcdm** (WSM + min-max) em teste — os escores batem a 1e-6.
- Produto: `POST /api/decisoes/{id}/ranking` aceita sobrescrita de pesos (revalidada);
  teste prova a troca de vencedor sobre a decisão salva.
- Bibliografia: Fishburn (1967) promovida a ✓ (registro DOI; nota: é carta ao editor).
- **Verificação**: etapa 04 `7 passed`; app `16 passed`; `mkdocs build --strict` verde
  (ver `specs/004-saw/qa-report.md`).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana pendente de gate de merge.

### Edição 0.3 — 2026-07-30 · normalização e pesos (spec 003)

- Capítulo 03 (min-max × vetorial; rating direto, ROC, swing e entropia) no esqueleto
  v3, com todas as tabelas geradas pelo motor da etapa; a origem dos pesos
  0,35/0,25/0,25/0,15 usados desde o cap. 01 fica declarada (rating direto).
- Etapa `03-normalizacao-pesos`: `normalizacao.py` + `pesos.py` puros, rotas
  `/api/normalizar` e `/api/pesos`, página comparando as duas normalizações.
- Produto: rota stateless `POST /api/pesos` (rating, ROC, swing, entropia).
- Bibliografia: Edwards & Barron (1994) promovida a ✓ (registro DOI verificado).
- **Verificação**: etapa 03 `20 passed`; app `14 passed`; `mkdocs build --strict` verde
  (ver `specs/003-normalizacao-pesos/qa-report.md`).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana pendente de gate de merge.

### Edição 0.2 — 2026-07-30 · repositório próprio + estruturação e dominância (spec 002)

- O projeto migrou para o repositório próprio **GHDaru/multicriterio** por determinação
  do Steward — extração registrada no ADR 0005 (supera a pendência do ADR 0001); CI e
  workflow do Pages ativos na raiz.
- Capítulo 02 (estruturação: value-focused thinking, checklist da família de critérios,
  dominância/fronteira de Pareto) no esqueleto v3; Keeney (1992) promovido a ✓ na
  bibliografia por verificação direta.
- `decisor-zero` etapa `02-dominancia`: motor de dominância puro + API + página, com o
  worked example (A5 dominado por A1) em teste; `matriz.py` incorporou o gabarito do
  exercício do cap. 01 (peso negativo agora é erro).
- Produto: rota `POST /api/decisoes/{id}/dominancia` com o mesmo motor e teste
  ponta a ponta.
- **Verificação**: etapa 02 `8 passed`; app `10 passed`; `mkdocs build --strict` verde
  (ver `specs/002-estruturacao-dominancia/qa-report.md`).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana pendente de gate de merge.

### Edição 0.1 — 2026-07-30 · fundação do projeto (spec 001)

- Nasce o projeto **Decisor**: constituição própria (v1.0.0, linhagem Engenharia de
  Harness + Maestro), `CLAUDE.md`/`AGENTS.md` para agentes, guia editorial com esqueleto
  v3 e caso âncora, sumário com a sequência didática completa (14 capítulos, Parte I–IV).
- Capítulos 00 e 01 escritos no esqueleto v3; bibliografia inicial com 30+ fontes e
  status de verificação (✓/?) — curadoria registrada em `bibliografia.md`.
- `decisor-zero/` etapas 00 (esqueleto FastAPI) e 01 (matriz de decisão como código),
  com os worked examples dos capítulos reproduzidos em testes.
- `app/` (o produto Decisor): backend FastAPI + motor SAW puro + repositório com
  Postgres (Neon) e fallback SQLite; frontend estático v0. Decisões em ADR 0001–0004.
- **Verificação**: `pytest` verde nas etapas e no app; build do livro verde
  (ver `specs/001-fundacao/qa-report.md`).
- **IA**: agente **Claude Code (Anthropic)**; curadoria humana pendente de gate de merge.

## Registro de expiração (o placar das previsões)

| Componente | Existe porque… | Previmos que expira quando… | Estado | Evidência datada |
|---|---|---|---|---|
| Seed no harness_engineering (ADR 0001) | não havia repositório próprio no nascimento | o Steward criar o repositório e o seed ser extraído | 🟢 cumprida | 2026-07-30 — GHDaru/multicriterio criado; ADR 0005 |
| Fallback SQLite no `app/` | a trilha deve rodar a custo zero e offline (Princípio VI) | o cap. 13 tornar o provisionamento Neon parte da trilha | 🟡 em movimento | 2026-07-31 — cap. 13 documenta o provisionamento; fallback permanece pelo custo zero |
| Capítulos 05–13 (long run, ADR 0006) | cobertura completa priorizada sobre profundidade | uma rodada de auditoria/aprofundamento revisar cada um | 🟢 cumprida | 2026-07-31 — specs 014–027 (ADR 0007): segundo domínio worked + gabarito em todos os capítulos |
| Frontend estático v0 | zero build = carga cognitiva mínima nas etapas | a UI do produto exigir estado complexo (comparação multi-método, cap. 11+) → migração conforme ADR 0002 | 🔵 aberta | — |
| Status "?" na bibliografia | editores bloqueiam verificação por robô | cada fonte "?" for promovida a ✓ antes de ser citada em capítulo novo | 🔵 aberta | — |

Legenda: 🔵 aberta · 🟡 em movimento · 🟢 cumprida · 🔴 refutada/não-expira.
Regra de manutenção: revisar este placar a cada edição.
