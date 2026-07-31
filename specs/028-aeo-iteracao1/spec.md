# Spec 028 — AEO, iteração 1: contribuição original do autor (ADR 0008)

- **Status**: Aprovada (direção do Steward) · **Raia**: Plena · **Data**: 2026-07-31
- **O quê**: fundamentar (busca bibliográfica verificada — família SMAA, 6 fontes ✓),
  formalizar (definições + 4 proposições com prova), implementar (motor `simular_aeo`
  com semente, rota `/api/aeo`, página), simular (âncora com/sem ordem; fornecedor) e
  publicar o cap. 14 + o artigo completo como Apêndice C (vivo, iteração 1).
- **Resposta à pergunta aberta do autor** (como decidir com as contagens): protocolo
  do ADR 0008 — matriz completa + posto esperado (≡ Borda, provado) + selo Condorcet
  estocástico + faixa de empate técnico. Justificado pelos próprios dados: no caso
  âncora sem ordem, as regras divergem (A3 × A1).
- **Crenças**: vetor de pesos central por alternativa (= central weight vector da
  SMAA-2), com leitura prescritiva e inversa; modo sem ordem = força intrínseca.
- **Constitution Check**: I ✅ (6 fontes verificadas; todos os números em teste com
  semente) · II ✅ (motor testado antes da prosa) · III ✅ (cap. didático + artigo
  técnico separados) · IV ✅ (artigo vivo versionado; edição 0.28) · V ✅ · VI ✅
  (posicionamento honesto vs SMAA; prior declarado como escolha) · VII ✅ (branch
  própria; iterações futuras = specs 029+). Sem violações.
- **DoD**: [x] etapa 14 `8 passed` · [x] mkdocs --strict · [ ] gate humano (revisão
  do autor — especialmente nome, posicionamento e protocolo).
