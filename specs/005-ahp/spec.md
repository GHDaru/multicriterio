# Spec 005 — AHP: comparações par a par (cap. 05 + etapa 05)

- **Status**: Aprovada (defaults, ADR 0006) · **Raia**: Plena · **Data**: 2026-07-31
- **Origem**: long run autorizada pelo Steward (ADR 0006), sequência do SUMARIO.

## O quê e por quê

Capítulo 05 (matriz de julgamentos, autovetor, CI/CR, debate do rank reversal) com a
etapa `05-ahp` e o método `ahp` em `/api/pesos` no produto. Resolve a dor do cap. 04:
de onde vem um w defensável — com detector de incoerência.

## Requisitos funcionais

- FR1 — Capítulo 05 esqueleto v3; corpo só com fontes ✓ (Saaty 1977/1980, Belton &
  Gear 1983, Dyer 1990 — promovidas nesta corrida por verificação de registro).
- FR2 — Etapa 05: `motor/ahp.py` puro (validação recíproca, potências, CI/CR, RI de
  Saaty) + rota + página interativa; worked example (pesos, λmax, CR) em teste.
- FR3 — Contraexemplo cíclico (CR=0,4488, reprovado) e caso perfeitamente consistente
  (CR=0) em teste.
- FR4 — Produto: `/api/pesos` método `ahp`, recusando CR > 0,10; teste.
- FR5 — Registro vivo (bibliografia ✓×4, SUMARIO, nav, mapa, HISTORICO 0.5, CHANGELOG).

## Fora de escopo (YAGNI)

AHP completo (alternativas par a par) — decisão do ADR 0006; fuzzy-AHP; ANP.

## Critérios de aceite (DoD)

- [x] pytest etapa 05 (8) e app (17) verdes; mkdocs --strict verde
- [ ] Gate humano a posteriori (ADR 0006)

## Clarify (defaults, ADR 0006)

Autovetor por método das potências em Python puro; RI tabelado até n=10; AHP = técnica
de pesos no produto.
