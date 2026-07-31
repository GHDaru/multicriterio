# Spec 008 — PROMETHEE I/II (cap. 08 + etapa 08)

- **Status**: Aprovada (defaults, ADR 0006) · **Raia**: Plena · **Data**: 2026-07-31
- **O quê**: capítulo 08 (funções de preferência, fluxos), etapa `08-promethee`
  (usual + V-shape, validação pymcdm) e `promethee2` no catálogo do produto.
- **FRs**: FR1 capítulo v3 (fonte ✓ Brans & Vincke 1985) · FR2 fluxos do caso âncora
  em teste + Σφ=0 + pymcdm 1e-6 · FR3 V-shape com o salto de A3 em teste · FR4 produto
  (motor usual + catálogo + teste) · FR5 registro vivo.
- **Fora de escopo**: PROMETHEE I (exercício do leitor); funções restantes do paper;
  plano GAIA.
- **DoD**: [x] etapa 5 passed · [x] app 19 passed · [x] mkdocs --strict.
- **Incidente registrado**: teste de propriedade inicial ("vshape encolhe |φ|") estava
  matematicamente errado — o correto é φ+ e φ− encolherem; o líquido pode crescer
  (A3: −0,0333 → +0,0406). Corrigido e transformado em fato didático do capítulo.
  Também corrigida asserção frágil do catálogo (igualdade → inclusão) no teste da
  rodada 006.
