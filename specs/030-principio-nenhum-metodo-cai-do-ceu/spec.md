# Spec 030 — Princípio VIII: "Nenhum método cai do céu" (emenda + infraestrutura)

- **Status**: Aprovada (pedido do Steward: "vamos incluir na constituicao e revisar o
  livro", com o texto integral do princípio) · **Raia**: Plena · **Data**: 2026-08-10
- **O quê**: (a) emenda constitucional v1.0.0 → **v1.1.0** — Princípio VIII com o
  texto do autor na íntegra (seção "De onde isto veio" com 5 elementos; selos
  ✓/✓ᵐ/⏳/❌/📖; três proibições; processo de pesquisa única com fila de verificação;
  duas armadilhas; teste da seção); (b) esqueleto v3 do guia editorial ganha o item 3
  obrigatório; (c) **nota de pesquisa histórica** (`estudos/nota-pesquisa-historia-mcda.md`)
  cobrindo caps. 02–10, 12, 14, produzida em sessão dedicada com leitura real de fonte
  (Roy 1968 ✓; obituário INFORMS de Saaty ✓) e fila de verificação; (d) ADR 0009;
  (e) CLAUDE.md/AGENTS.md, HISTORICO, CHANGELOG. A revisão dos capítulos (inserção das
  seções) é a **spec 031**, que consome a nota.
- **Por quê**: capítulo sem história entrega procedimento, e procedimento se decora;
  história inventada é pior que omitida porque convence. O princípio protege a
  transferência (a ideia reaproveitável) e a honestidade (selo por afirmação).
- **Constitution Check**: I ✅ (a própria emenda estende o regime de evidência à
  história; leitura real de Roy 1968 já selada) · II ✅ · III ✅ (a seção nova é
  supportive information posicionada antes da intuição) · IV ✅ (edição 0.30) · V ✅ ·
  VI ✅ (a história não elege "melhor método"; registra recusas e contextos) ·
  VII ✅ (branch própria; emenda constitucional documentada com ADR — a exceção "direto
  ao main" não foi usada porque a rodada inclui guia + nota + registro) · VIII ✅
  (processo do próprio princípio seguido: pesquisa em sessão única, nota com fila,
  selos honestos — inclusive ⏳ para o que só veio de resumo de busca).
- **DoD**: [x] constituição v1.1.0 com texto verbatim · [x] guia editorial (esqueleto
  10 itens) · [x] nota de pesquisa com fila (item 5 já fechado na sessão) ·
  [x] ADR 0009 · [x] mkdocs --strict · [ ] gate do autor.
