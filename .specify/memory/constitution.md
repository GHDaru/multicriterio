# Constituição — Decisor (livro vivo + aplicação de decisão multicritério)

> A lei do projeto. Em conflito entre um pedido pontual e esta constituição, a constituição
> prevalece — ou o conflito é explicitado ao usuário antes de agir.
>
> **Versão 1.1.0** · Ratificada em 2026-07-30 · Emendada em 2026-08-10 (Princípio VIII,
> ADR 0009) · Linhagem: constituição do
> [Engenharia de Harness](https://github.com/ghdaru/harness_engineering) (v1.2.0) +
> princípios do [Maestro](https://github.com/ghdaru/maestro) (v1.0.0).

O projeto tem três corpos inseparáveis:

1. **O livro** (`livro/`) — ensina decisão multicritério (MCDA) do zero: o leitor aprende lendo.
2. **A construção prática** (`decisor-zero/`) — uma etapa executável por capítulo: o leitor aprende construindo.
3. **A aplicação** (`app/`) — o produto (backend FastAPI + banco Neon/Postgres + frontend web): o leitor aprende usando.

## Princípios

### I. Evidência acima de retórica (NÃO-NEGOCIÁVEL)

Toda afirmação metodológica sobre um método MCDA exige fonte primária com status
validado (✓) em `livro/bibliografia.md`. Toda fórmula apresentada no livro exige um
**exemplo numérico resolvido** cujo resultado é reproduzido por um teste automatizado no
`decisor-zero` — o worked example do capítulo é fixture de teste. Toda fonte de indústria
ou software exige URL verificável. Sem evidência, não entra no corpo do livro.

### II. Nenhum método sem implementação; nenhuma implementação sem fonte

A fonte-base do livro é a **literatura seminal de MCDA lida na origem** (Keeney & Raiffa,
Saaty, Roy, Brans, Hwang & Yoon…), e a prova de compreensão é o **código executável**.
Um método só ganha capítulo quando sua implementação no `decisor-zero` passa nos testes
que reproduzem exemplos da literatura; um algoritmo só entra no código citando no
docstring a fonte da formulação. Surveys e material didático de terceiros contextualizam,
mas não substituem a fonte seminal.

### III. Método pedagógico combinado

Todo capítulo e toda etapa seguem **Backward Design** (objetivos → evidências → conteúdo),
**4C/ID** (etapas do `decisor-zero` = learning tasks; capítulos = supportive information;
docstrings = just-in-time; exercícios = part-task practice), **Diátaxis** (tutorial,
how-to, referência e explicação nunca misturados na mesma seção) e **Carga Cognitiva**
(worked example antes de exercício; uma ideia nova por vez). O **esqueleto v3 de
capítulo** (ver `livro/GUIA-EDITORIAL.md`) é obrigatório. Um único **caso âncora**
(a escolha de um apartamento) atravessa o livro inteiro — todo método novo é aplicado
primeiro ao caso âncora, para que o leitor compare métodos sobre o mesmo problema.

### IV. Livro vivo (datação e expiração)

Todo capítulo declara **data de captura** no cabeçalho
(`> **Estado da arte capturado em AAAA-MM** · última revisão AAAA-MM-DD`). Toda edição
atualiza `livro/HISTORICO.md` — changelog, tabela de snapshot por capítulo e **registro
do modelo de IA usado** (saídas de LLM são não-determinísticas; o registro é parte da
rastreabilidade). Reavaliar = nova rodada, nunca sobrescrever silenciosamente.

### V. Segurança e credenciais

Nenhum segredo (connection string do Neon, chave de API, token) entra em arquivo, commit
ou texto publicado. Credenciais vivem só em variáveis de ambiente / `.env` gitignored;
todo diretório executável tem `.env.example` sem valores reais. Chave exposta é chave
comprometida: alertar e orientar revogação. O código didático demonstra a prática correta.

### VI. Neutralidade metodológica e acessibilidade

**Nenhum método MCDA é "o melhor"**: cada capítulo declara premissas, condições de uso e
limitações conhecidas do método (compensação, independência preferencial, rank reversal,
escolha de normalização) com fonte. A trilha prática roda a **custo zero**: tudo executa
localmente sem banco (fallback SQLite/memória) e o produto usa o free tier do Neon.
Prosa em português; termos técnicos consagrados (trade-off, outranking, rank reversal)
sem tradução forçada, expandidos na primeira ocorrência.

### VII. Spec-driven, raias e gates (NÃO-NEGOCIÁVEL — herdado do Maestro)

Toda melhoria passa pelo ciclo `spec → plan (Constitution Check) → tasks → implement →
DoD verificável → revisão em contexto fresco → gate humano → merge`, cada uma na sua
branch/rodada, registrada em `specs/NNN-nome/`. **Raias**: *leve* (typo, link, bug com
teste que o reproduz — o PR é o artefato), *plena* (capítulo, etapa, feature — spec
completa), *infra* (banco, deploy, migração — sempre plena + gates de reversibilidade:
backup, dry-run, rollback documentado). Regras permanentes: na dúvida, é plena; quem
executa não verifica (revisão independente em contexto fresco); **"prove, não declare"**
(todo "pronto" vem com o output do teste/build que o comprova); toda decisão relevante
vira ADR em `adr/` (imutável — superada, nunca editada no mérito). Exceções que vão
direto ao main: emendas a esta constituição e correções triviais.

### VIII. Nenhum método cai do céu (NÃO-NEGOCIÁVEL)

Todo método deste livro foi inventado por **alguém**, que estava **preso** num problema
concreto, numa data, com meios limitados. Um capítulo que apresenta o método sem essa
história entrega um procedimento — e procedimento, o leitor decora. **Este livro não passa
decoreba.**

A razão não é ornamental. Quem sabe *que problema forçou o método a existir* consegue
reconhecer, anos depois e noutro contexto, quando está diante do mesmo tipo de aperto — e é
isso que transfere. Quem só sabe executar o procedimento tem uma habilidade que expira com a
prova.

#### A seção obrigatória: "De onde isto veio"

Todo capítulo de método tem essa seção, posicionada **depois** de "o problema" e **antes** da
intuição. Ela não é caixa de curiosidade: é o que dá ao leitor um motivo para não pular
direto para a fórmula.

Cinco elementos, nesta ordem:

| Elemento | A pergunta que responde |
|---|---|
| **O aperto** | Quem estava preso, em quê, quando. Um problema do mundo, com data e gente |
| **O que se fazia antes** | Contra o quê o método compete. Sem isto, não dá para medir o salto |
| **A virada** | Qual foi a ideia que destravou — em linguagem natural, sem notação |
| **A ideia reaproveitável** | O padrão de raciocínio que serve **fora** deste método |
| **O nome** | Se o nome tem origem, ela é contada |

O elemento que mais importa é o quarto. **Todo artifício técnico declara a ideia
reaproveitável que há por trás dele.** Um artifício sem ideia é truque, e truque não se
transfere.

#### História é afirmação, e exige fonte

Este é o terreno mais fácil do livro para inventar, porque **história inventada soa bem**: uma
data errada e uma atribuição plausível passam por qualquer revisão apressada.

**Inventar história é pior do que omiti-la, porque é convincente.**

Toda afirmação histórica carrega um selo, e cada capítulo fecha a seção com uma tabela que
declara o estado de cada uma:

| Selo | Significa |
|---|---|
| ✓ | **Fonte aberta e lida.** O que está afirmado foi conferido no texto |
| ✓ᵐ | **Só os metadados** foram conferidos (autor, obra, ano, identificador). O conteúdo não foi lido |
| ⏳ | **Atribuição corrente**, repetida na literatura didática, **não confirmada em fonte primária** |
| ❌ | Procurei e **não achei fonte** |
| 📖 | **Leitura editorial** — interpretação deste livro, não afirmação histórica |

A distinção entre ✓ e ✓ᵐ não é preciosismo: ela é o que impede confundir *"existe e é este
artigo"* com *"eu li e diz isso"*. Metadado confere que a obra existe; não confere o que ela
afirma.

O selo ❌ é permitido e às vezes é o mais honesto. Uma lacuna admitida em voz alta vale mais
do que uma suposição com cara de fato.

#### Três proibições

1. **Nada de gênio solitário.** É uma história ruim e geralmente falsa. Métodos nascem de
   instituições, encomendas, prazos e restrições materiais — e é isso que ensina.
2. **Nada de curiosidade decorativa.** Se o parágrafo sai sem o leitor perder compreensão ou
   julgamento, ele é enfeite. A história entra porque ensina, não porque enfeita.
3. **Nada de misturar registro.** "A literatura atribui a X" não é a mesma frase que "X
   publicou em 19NN", e as duas não podem parecer iguais no texto.

#### Processo: pesquise de uma vez, não capítulo a capítulo

Concentre a pesquisa histórica numa **sessão própria**, que produz uma nota de pesquisa
alimentando as rodadas seguintes — em vez de pesquisar dentro de cada capítulo.

A razão é concreta: **as histórias se conectam, e quem descobre a conexão depois já publicou
os dois lados sem ela.** Pesquisando junto, as ligações aparecem; pesquisando separado, não.

A nota de pesquisa deve terminar com uma **fila de verificação**, ordenada por quanta dúvida
cada fonte fecharia por unidade de esforço. Nem toda fonte é alcançável, e saber qual abrir
primeiro poupa horas.

#### Duas armadilhas, aprendidas na prática

**Resumo de busca não é fonte — nem para confirmar, nem para desmentir.** Um resumo pode
abreviar o original de tal forma que um fato **correto** pareça errado. Corrigir a partir do
resumo introduz o erro que você achava estar consertando. Se a afirmação importa, abra o
texto.

**Ler a fonte não serve só para conferir: serve para achar o que você não sabia que estava
lá.** As melhores histórias quase nunca aparecem em resumo — elas estão no parágrafo que
ninguém resumiu.

#### O teste da seção

O leitor deve terminá-la **querendo continuar**. Um livro técnico compete com a tentação de
pular para a fórmula; a história é o que dá ao leitor um motivo para não pular.

## Restrições da construção (decisor-zero e app)

1. **Uma etapa por capítulo, autocontida** — cada `decisor-zero/etapas/NN-tema/` roda
   sozinha (`uvicorn app:app --reload`); o diff entre etapas consecutivas é a lição do
   capítulo. O frontend das etapas é HTML+JS sem build (carga cognitiva mínima).
2. **Motor de cálculo puro** — os algoritmos MCDA são funções puras sem I/O, testáveis
   sem servidor e sem banco; FastAPI e persistência são camadas por fora (hexagonal por
   refatoração, como no harness-zero).
3. **O produto congela a stack**: backend Python + FastAPI; banco Postgres (Neon) com
   fallback SQLite local; frontend conforme ADR 0002. Nada de framework novo sem ADR.
4. **Anti-apodrecimento**: o acesso a banco fica atrás de uma camada de repositório;
   trocar Neon por outro Postgres (ou SQLite) não toca o motor nem as rotas.

## Governança

Emendas a esta constituição: versão semântica (MAJOR remoção/redefinição de princípio,
MINOR princípio novo, PATCH clarificação), registro em `livro/HISTORICO.md` e ADR quando
a decisão for material. Todo agente e humano DEVE ler este arquivo antes de qualquer
trabalho no projeto.
