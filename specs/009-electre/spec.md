# Spec 009 — ELECTRE I (cap. 09 + etapa 09)

- **Status**: Aprovada (defaults, ADR 0006) · **Raia**: Plena · **Data**: 2026-07-31
- **O quê**: capítulo 09 (concordância/discordância/veto/kernel), etapa `09-electre`
  (motor + rota + página com limiares ajustáveis).
- **FRs**: FR1 capítulo v3 (fontes ✓: Roy 1968, Belton & Stewart, Greco et al.) ·
  FR2 três cenários (relação vazia; S={A1→A4, A4→A2} com kernel {A1, A3}; veto) em
  teste · FR3 registro vivo.
- **Decisões da rodada**: saída = relação + kernel (não ranking) ⇒ fora do catálogo de
  ranking do produto; exposição como análise fica para a spec 011. Discordância
  normalizada pela amplitude da coluna (documentada no docstring). Sem validação
  cruzada (pymcdm não tem ELECTRE I) — validação por cenários e propriedades
  (ADR 0006 §3).
- **DoD**: [x] etapa 5 passed · [x] mkdocs --strict · [ ] gate a posteriori.
