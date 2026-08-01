# Spec 029 — AEO, iteração 2: a matemática do prior (ADR 0008)

- **Status**: Aprovada (direção do Steward: "vamos para iteração 2" + conjectura dos
  valores médios) · **Raia**: Plena · **Data**: 2026-07-31
- **O quê**: formalizar a conjectura do autor sobre os valores médios do sorteio.
  Resultado: **Proposição 5** — a densidade do prior AEO no simplexo é ∝ max(v)^(−m)
  (prova por jacobiano); corolário fechado m=2: E = (ln 2, 1−ln 2) ≈ (0,693; 0,307).
  A conjectura (0,75 × 0,25) é exatamente a média do prior uniforme-no-simplexo
  (= ROC) — um prior legítimo, distinto do implementado. Motor ganha
  `prior="uniforme"|"simplexo"` + `media_valores_ordenados` + `media_simplexo_ordenado`;
  experimento §7.4 mede o impacto no caso âncora (aceitabilidade de A4: 36,4% → 65,1%;
  campeão e Condorcet estáveis; cauda muda). Artigo bump → iteração 2; agenda item 1
  concluído.
- **Constitution Check**: I ✅ (prova + verificação Monte Carlo em teste, ln 2 a 2e-3;
  simplexo ≡ ROC a 2e-3) · II ✅ · III ✅ (cap. 14 ganha o parágrafo "o sorteio é um
  prior") · IV ✅ (edição 0.29; artigo versionado) · V ✅ · VI ✅ (nenhum prior é "o
  correto"; escolha declarável) · VII ✅. Sem violações.
- **DoD**: [x] etapa 14 `14 passed` · [x] mkdocs --strict · [ ] gate do autor.
