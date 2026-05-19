# Applied Economics Journal — Writing Norms Skill

## SKILL METADATA

```yaml
name: applied-economics-rewrite
description: >
  Rewrite economics research manuscripts to match Applied Economics (Taylor & Francis SSCI)
  journal writing conventions. Uses RAG retrieval against a vector database of published
  AE papers to ground every stylistic decision in real published exemplars.
  Covers all 7 standard chapter types: Abstract, Introduction, Literature Review,
  Theoretical Model, Data & Variables, Empirical Results & Robustness, Conclusion.
version: 1.0
vector_db: <REPO_ROOT>/data/economics_papers_vectors.jsonl
faiss_index: <REPO_ROOT>/data/economics_papers.index
```

---

## DATA SOURCE & CORPUS OVERVIEW

All norms below are extracted exclusively from published Applied Economics articles. Every norm is derived from high-frequency patterns observed across multiple papers in this corpus. Do NOT apply generic academic writing advice that contradicts the specific evidence below.

---

## OVERRIDING RULE: DATA INTEGRITY & ACADEMIC HONESTY

This skill performs **language-level rewriting** — improving expression, structure, and journal-convention compliance. It does NOT generate new research content. The following rules apply to ALL chapter types and override any stylistic convention below when they conflict.

### Z1. Zero Fabrication

Under no circumstances may the rewrite:

| Prohibited | Rationale |
|---|---|
| Invent numbers, coefficients, p-values, sample sizes, R² | Only the original manuscript contains real data |
| Invent paper titles, authors, years, DOIs, journal names | False citations are academic fraud |
| Invent historical events, policy changes, institutional names | These are factual claims, not stylistic choices |
| Change sign, magnitude, or significance of any result | Even if "stronger," this misrepresents the research |
| Add claims about causality, mechanisms, implications the authors did not make | Overstepping the author's voice |

### Z2. Metadata as Ground Truth

- The original manuscript's abstract, tables, equations, and author statements are the sole source of truth for all factual and quantitative content.
- Number-preservation rule: If the original states "the coefficient is 0.034," the surrounding prose may change but "0.034" must appear verbatim.
- Gap-filling prohibition: If the original text omits a statistic (e.g., no F-statistic is reported), do NOT invent one — even if convention would include it.

### Z3. Verifiable Citations Only

Every literature reference introduced during rewriting must trace to one of three acceptable sources:

1. **Cross-reference** — already cited elsewhere in the same manuscript
2. **RAG retrieval** — retrieved via the vector database; output includes real paper metadata (author, year, journal)
3. **User-provided** — explicitly given by the user

Unacceptable: papers "recalled" from training data; papers whose existence cannot be confirmed; generic "(Author, Year)" without specific identity.

**When in doubt, do NOT add the citation.** Prefer under-citation to false citation.

### Z4. Provenance Annotation

Every external fact, statistic, or citation added beyond the original manuscript must include a provenance tag:

```
[Source: RAG retrieval — Churchill & Marisetty (2020), Applied Economics]
[Source: User-provided manuscript, Section 3.2, Table 2]  
[Source: Cross-reference from manuscript Introduction ¶3]
```

If provenance cannot be established, the claim must not be written.

---

## BATCH 1: ABSTRACT WRITING NORMS

### 1.1 Structure Logic

**Fixed sequence (high-frequency):**

1. **Research objective/motivation** — Sentence 1: What this paper does. Opens with "We examine", "This study investigates", or "This paper analyses".
2. **Method/approach** — Sentence 2-3: Data source, sample period, methodology name. Opens with "Using...", "We use...", or methodology is named inline.
3. **Key findings** — Sentence 3-5: Core empirical results. Opens with "We find that", "The results show that", "Our findings demonstrate that".
4. **Implications/contribution** — Final 1-2 sentences: Policy relevance or literature contribution. Opens with "These results", "Our findings", "This research contributes to".

**Critical structural rule:** Applied Economics abstracts are single-paragraph (all sampled abstracts). No sub-headings, no multi-paragraph abstracts. Average length: ~150 words. Range: compact.

**Anti-patterns (absent from corpus):**
- No structured abstracts with labeled sub-sections (Background/Aim/Methods/Results)
- No bullet points
- No standalone research questions
- No JEL codes or keywords integrated into abstract text

### 1.2 Paragraph Layout

- **Single paragraph, block prose** (all sampled). No line breaks within abstract.
- Average sentence count: 5-7 sentences.
- Sentence length: medium-long, often multi-clause (see trigram data: "and economic growth", "over the period", "based on the").
- Dense information packaging: method and finding often co-occur in one sentence (e.g., "Using [method], we find that [result]").

### 1.3 Opening & Closing Sentence Templates

**Opening sentence templates (frequency ≥2 in corpus):**
| Template | Frequency | Example Source |
|---|---|---|
| "This study investigates the [topic]..." | 5 | Afsar 2026, multiple |
| "We examine the [topic/relationship]..." | 4 | Afonso 2025, Drobetz 2021 |
| "This paper analyses the [topic]..." | 2 | Dahmani 2023, Fernandes 2021 |
| "This paper investigates the [topic]..." | 2 | Corbet 2022, Li 2021 |
| "This study examines the [topic]..." | 2 | Afsar 2026, Ahunov 2020 |
| "[Context statement]. We examine..." | 3 | Chernoff 2023, multiple |

**Domain-specific opening variant:** When studying a specific policy shock or event, open with context then pivot to the paper's investigation. Example: "On 25 December 2016, China introduced the Environmental Protection Tax Law... By leveraging [this event], we examine..."

**Closing sentence templates (frequency ≥2):**
| Template | Frequency |
|---|---|
| "Our results [show/confirm/underscore]..." | 6 |
| "The findings of this study have [policy implications]..." | 4 |
| "This research contributes to the existing literature [on...]" | 3 |
| "These findings [are consistent with/reject/underpin]..." | 3 |
| "The results [show/indicate/suggest] that..." | 2 |
| Policy recommendation closure: "[Entity] should/must [action]..." | 2 |

### 1.4 Academic Vocabulary & Diction

**High-frequency content vocabulary (top trigrams, normalized):**

*Study/paper self-reference:*
- "this study" "we examine" "this paper" (5), "we find that" (7)
- Dominant pattern: "This study/paper + investigates/examines/analyses" (NOT "In this paper we try to...")

*Result reporting:*
- "results show that" "results indicate that" (5), "we find that" "the empirical results" (8)
- NEVER "we try to", "we attempt to", "we hope to"

*Relationship description:*
- "the impact of" "the effects of" (10), "the relationship between" (9)
- "a significant and positive" (3), "is associated with" (4)

*Contribution language:*
- "contributes to" (4), "novel" (4), "first time" (3), "contribution" (3)
- Modest framing: contributions are stated as "This research contributes to the existing literature on X" rather than "This is the first paper to ever..."

**Hedging profile:** Abstract hedging is MINIMAL compared to other chapters (minimal hedging). When hedging is used:
- "suggest(s) that" (6), "indicate(s) that" (6) — the dominant weak-claim markers
- "likely" "may" (5) — the dominant probability qualifiers
- "should" (7) — used exclusively for policy recommendations, NOT for hedging claims

**Anti-patterns (absent or near-absent):**
- No "might" (absent)
- No "perhaps", "maybe", "could possibly"
- No "to the best of our knowledge" (this belongs in Introduction, not Abstract)

### 1.5 Voice & Tense Conventions

**Voice:** Active voice dominant. "We" is the standard agent (active "we" and passive constructions are roughly balanced).

- "We examine" "We find" "We use" (5), "We conclude" (2)
- Passive reserved for: "It was found that" (rare, 1-2 occurrences), methodological descriptions: "was employed", "were used"

**Tense:** Present tense dominant throughout present tense dominant.
- Research action: present ("This study examines", "We investigate")
- Findings: present ("The results show", "We find that")
- NEVER "This study examined" or "We investigated" in abstract

### 1.6 Transition & Cohesion Patterns

Abstract transitions are sparse by design (compact prose). When used:
- "However" (7) — contrasting findings or qualifying results
- "Moreover" (6) — adding supporting evidence
- "Finally" (3) — signaling last finding
- "Specifically" (4) — elaborating a result
- "Overall" (4), "Collectively" (1) — summary signal before implications
- "Meanwhile" (3) — parallel or contrasting sub-findings (distinctive AE usage)

**Cohesion strategy:** Logical progression is achieved through implicit topic chains rather than explicit transition words. The 4-part structure (objective→method→findings→implications) carries the reader without heavy signposting.

---

## BATCH 2: INTRODUCTION WRITING NORMS

### 2.1 Structure Logic

**Typical introduction structure (synthesized from corpus):**

1. **Broad context/motivation** (1-2 paragraphs) — Economic phenomenon, policy context, or real-world trend motivating the study. Opens with descriptive statements about the research domain.
2. **Narrowing/focusing** (1-2 paragraphs) — Refining to the specific angle the paper addresses. Introduces theoretical mechanism or empirical puzzle.
3. **Literature positioning** (1-2 paragraphs) — Selective reference to key prior work establishing the gap. NOT a full literature review. Citations are instrumental — used to set up what is NOT yet known.
4. **This paper's approach** (1 paragraph) — What this paper does, often with methodology preview. "In this paper, we...", "The purpose of this paper is to..."
5. **Contribution statement** (0.5-1 paragraph) — Explicit contribution claims, often numbered. "Our study makes two contributions... First,... Second,..."
6. **Roadmap** (final paragraph) — "The remainder of the paper is organized as follows. Section 2... Section 3..."

**Observed structural pattern:** Introductions in this corpus frequently end with an explicit road-map paragraph. ~60% of introduction chunks with sub-index 0 contain "The remainder/rest of the paper is organized as follows" or similar.

### 2.2 Paragraph Layout

- Average paragraph: 88 words (P50 = 67 words). High variance (P25 = 30, P75 = 122).
- Opening paragraphs tend to be longer (establishing context).
- Middle paragraphs are shorter and more focused.
- Roadmap paragraph is typically the shortest, formulaic.
- Paragraph breaks occur at logical topic shifts, NOT at arbitrary word counts.

**Citation-integrated prose pattern:** In the introduction, citations are woven into sentences as grammatical subjects or parenthetical evidence, not as standalone sentence subjects dominating the prose. Example: "The literature advances the existence of two fiscal regimes: Ricardian and non-Ricardian. In a Ricardian regime, future tax revenues are expected to..." (Afonso 2025)

### 2.3 Opening & Closing Sentence Templates

**Section-opening patterns (highest frequency):**

*Context-setting openers:*
- "The growth of [phenomenon] seen in [context] is currently a matter of concern..." (2+)
- "Crude oil is a critical global [resource/indicator] due to its widespread use (Author Year)." (3+)
- "In recent decades, [trend/phenomenon] has [intensified/strengthened/become]..." (4+)
- "[Phenomenon] represents a key challenge in [region/context]..." (2+)

*Gap/puzzle openers (for later paragraphs within intro):*
- "However, [unresolved issue]..."
- "The connection between X and Y is further complicated by..."
- "Although [existing knowledge], [gap statement]..."

**Roadmap closers (end-of-introduction paragraph endings):**
| Template | Frequency |
|---|---|
| "The remainder of the paper is organized as follows. Section [N] [verb]..." | ~30% of intros |
| "The rest of the paper is organized as follows..." | ~10% |
| "Section [N] [presents/describes/reports]... Section [N+1] [concludes/discusses]..." | standard |

**Contribution statement templates:**
- "This is the novelty of this work, given that, to the best of our knowledge, this is the first research [applied to X that does Y]."
- "Our study makes [two/three] contributions. First, we... Second, we..."

### 2.4 Academic Vocabulary & Diction

**High-frequency domain vocabulary :**

*Context-setting phrases:*
- "due to the" (41), "based on the" (41), "the effect of" (40), "such as the" (26)
- "according to the" (28), "the role of" (31), "the importance of" (16)
- "one of the" (20), "in the context of" (19)

*Study self-reference:*
- "in this study" (21), "this paper is" (17), "of this paper" (17), "of this study" (17)
- "we" constructions: "we examine" (5+), "we use" (5+), "we estimate" (3+)

*Gap/contrast markers:*
- "However" (104 occurrences) — overwhelmingly the dominant contrast signal
- "On the other hand" (17), "In contrast" (15)
- "While/although" structures are frequent for embedding contrast within sentences

*Contribution language:*
- "contributes/contribution/contribute" (60 total)
- "novel" (19), "extension/extend/extends" (29 total)
- "fill(s) this gap" (5), "shed(s) light on" (6)

**Hedging profile :**
- "may" — the most common hedge
- "likely" (70), "would" (63), "should" (49), "could" (45)
- "suggest(s) that" (40+) — dominant weak-claim construction
- "tend(s) to" (31) — distinctive AE usage pattern
- "generally" (20), "typically" (7)
- "potentially" (9), "possibly" (5)

### 2.5 Voice & Tense Conventions

**Voice:** Mixed, with a passive preference for establishing context and an active preference for stating the paper's contributions.

- Passive: passive preference for context. Context-setting and mechanism descriptions are predominantly passive ("has been the subject of", "is expected to", "are expected to be used").
- Active "we" for own contributions. Shifts to active when the paper's own actions are described ("we examine", "we use", "we estimate", "we find").

**Rule:** Context/background → passive or third-person. This paper's actions → active "we".

**Tense:** Present tense dominant present tense dominant.
- Established findings from literature: present tense ("The literature advances...", "Previous studies find...")
- Historical context: past tense ("The 2008 financial crisis triggered...")
- This paper's action: present ("This paper examines...", "We estimate...")

### 2.6 Transition & Cohesion Patterns

**Transition profile (top transitions):**

- "However" — the primary contrast/concession signal
- "Therefore" — the primary consequence signal
- "Thus/thus" — consequence/inference
- Enumeration: "First" (44), "Second" (43), "Third" (27), "Finally" (32) — heavily used for multi-point arguments and contribution lists
- "Moreover", "Furthermore" — additive emphasis
- "In addition" (26), "Additionally" (11) — neutral additive
- "For example" (30), "In particular" (15) — exemplification
- "Similarly" (17) — comparison
- "In contrast" (15), "On the other hand" (11) — contrast
- "Consequently" (10), "Hence" (9) — strong consequence
- "To this end" (5) — purpose-directed transition
- "In line with" (13), "consistent with" (10) — alignment with prior work

**Paragraph-level cohesion:** The introduction follows a funnel structure (broad→narrow→gap→this paper→roadmap). Topic chains carry across paragraph boundaries. The final sentence of one paragraph often previews the topic of the next.

---

## BATCH 3: LITERATURE REVIEW WRITING NORMS

### 3.1 Structure Logic

**Literature review in Applied Economics follows a thematic-stream organization, NOT chronological or author-by-author listing.**

**Standard structure :**

1. **Thematic sub-sectioning by research stream** — Literature is organized into thematic "strands" or "streams" (observed: "This study is based on two strands of the literature: one related to... and one that deals with..."). Each stream gets 1-3 paragraphs.
2. **Within-stream organization:** Classic study → elaboration → recent work → gaps in this stream.
3. **Hypothesis development** — Reviews frequently conclude with "Therefore, we propose the following hypothesis:" or "Thus, we propose:" followed by numbered hypotheses (H1, H2, H3). This is a distinctive AE pattern: the lit review directly feeds hypothesis formulation.
4. **Gap summarization** — Before transitioning to methodology, a summary of what the literature collectively has NOT addressed.

### 3.2 Paragraph Layout

- Average paragraph: 73 words. High variance — citation-dense review paragraphs average 98 words, hypothesis paragraphs average 41 words.
- P50: 41 words, P75: 98 words → bimodal distribution: short hypothesis paragraphs and long review paragraphs.
- Review paragraphs are often complex, multi-citation constructions (2-4 citations per paragraph typical).
- Hypothesis paragraphs are short and formulaic.

### 3.3 Opening & Closing Sentence Templates

**Literature stream openers:**

| Template | Frequency |
|---|---|
| "There is a consensus in the literature regarding..." | 2+ |
| "The work of [Author] (Year) triggered nearly [N] decades of work on..." | 2+ |
| "A strand of studies has [utilized/examined/investigated]..." | 3+ |
| "This study is based on [N] strands of the literature: one related to... and one that deals with..." | 3+ |
| "Previous studies have consistently suggested that..." | 2+ |
| "Over recent decades, a considerable amount of literature has been published on..." | 2+ |
| "A growing number of existing studies in the broader literature have examined..." | 2+ |

**Hypothesis formulation closers (distinctive AE pattern):**
- "Thus, we propose the following hypothesis:" (9 — THE single most frequent closing pattern in this chapter)
- "Therefore, we propose the following hypothesis:" (7)
- "Therefore, the following hypotheses are proposed:"
- "To summarize our hypotheses: H1a: [statement] H1b: [statement]"

**Gap-summarization closers:**
- "It is worth noting, also, that most of this work uses methods of analysis that do not consider [limitation]. The present paper contributes by [addressing gap]."
- "However, [gap description]. This paper [fills/addresses] this gap by..."

### 3.4 Academic Vocabulary & Diction

**Citation-verb repertoire (extracted from 296 Author-Year citations):**

*Neutral reporting verbs:*
- "find(s) that" (13), "show(s) that" (8), "report(s) that" (5), "observe(s) that" (3)
- "argue(s) that" (5), "suggest(s) that" (8), "conclude(s) that" (4)
- "note(s) that" (3), "document(s)" (3), "demonstrate(s)" (3)

*Evaluative reporting verbs (distinctive of lit reviews):*
- "confirm(s)" (2), "support(s)" (2), "challenge(s)" (1)
- "extend(s)" (2), "contradict(s)" (1)

**Relationship-description vocabulary:**
- "the relationship between" (26), "the impact of" (41)
- "found that the" (13), "negatively associated with" (7)
- "and economic growth" (23), "carbon emissions and" (19)
- "the following hypothesis" (17), "we propose the" (16)

**Hedging profile (moderate hedging, less than introduction):**
- "may" (75), "likely" (16), "would" (15)
- "tend(s) to" (15), "suggest(s) that" (15)
- "generally" (9), "could" (9)
- "typically" (2)

### 3.5 Voice & Tense Conventions

**Voice:** Strong passive preference for describing literature findings (passive preferred for literature).

- Literature description: passive/third-person dominant ("It has been documented that...", "This effect was found to be...")
- Hypothesis formulation: active "we" ("Thus, we propose...", "We hypothesize that...")
- Gap identification: mixed, often active ("we extend", "we contribute")

**Tense:** Present tense dominant present tense dominant.
- Describing existing findings: present tense ("X and Y (2020) find that...")
- Describing specific study actions: past tense ("X and Y (2020) used a sample of...")
- Rule: present for findings/conclusions; past for what specific researchers did procedurally.

### 3.6 Transition & Cohesion Patterns

**Transition profile :**

- "Therefore" (34) — leading into hypotheses from literature synthesis
- "However" (33) — contrasting findings across studies
- "Thus" (18), "Consequently" (14) — consequence/logical flow
- "For example" (10), "For instance" (8) — exemplification
- "Furthermore" (9), "Moreover" (8) — additive
- "Similarly" (9), "In contrast" (9) — comparison/contrast pair
- "Nevertheless" (7) — concession (distinctive: used more in lit reviews than elsewhere)
- "Specifically" (6) — elaboration

**Literature-stream signaling (distinctive AE pattern):**
- "The first/second/third stream of work focuses on..." — stream enumeration
- "Another strand of the literature examines..." — adding streams
- "In the same vein,..." (2) — grouping similar studies
- "Unlike [Author(s)],..." — distinguishing contribution

---

## BATCH 4: THEORETICAL MODEL WRITING NORMS

### 4.1 Structure Logic

**The theoretical model section in AE follows a method-first, stepwise exposition structure:**

1. **Method/approach announcement** (1-2 sentences): "To examine [research question], we [employ/use/implement] [method name], as proposed by [Author (Year)]."
2. **Model specification** (equation + variable definitions): Mathematical notation followed by prose explanation of each term.
3. **Estimation procedure** (1-2 paragraphs): Step-by-step explanation of how the model is estimated. "We begin with...", "Then we...", "The first step of our study is to determine..."
4. **Diagnostic/validation tests** (0.5-1 paragraph): Tests that validate the model choice (unit root, cointegration, cross-sectional dependence).
5. **Justification** (interspersed): Why this method is appropriate, often with citation support.

**Critical structural observation:** AE theoretical model sections are methodologically pluralistic — they frequently combine multiple econometric approaches. The structure is additive/sequential rather than comparative.

### 4.2 Paragraph Layout

- Average paragraph: 56 words (shortest of all chapters).
- P50: 32 words, P75: 66 words.
- Paragraph breaks occur at each new equation, each new step, each new test.
- Formula/equation display significantly reduces paragraph length (text surrounding equations is minimalist).
- Typical pattern: 2-3 sentence paragraph → equation → 2-3 sentence paragraph → equation.

### 4.3 Opening & Closing Sentence Templates

**Section openers:**
- "In order to study [topic] in [context], we use several empirical methodologies in a panel set up."
- "To examine the impact of [X] on [Y] we estimate the following model, inspired by [Author (Year)]."
- "[Method name] methodology — We implement the [method], as proposed by [Author (Year)]. A detailed explanation is provided in [Appendix/ below]."
- "In our analysis, we use a [model type] to examine the effects of [X] on [Y]."
- "The first step of our study is to determine whether the variables are stationary..."

**Equation introduction templates:**
- "..., we estimate the following [model/equation]:"
- "...which can be expressed as:"
- "The baseline model takes the following form:"
- "The [model] is specified as follows:"

**Section closers:**
- "Further details are in Appendix [X]." (common)
- "[Citation] also conclude that there is heterogeneity in..."
- "The panel-data approach allows for unobserved individual heterogeneity by introducing fixed effects, resulting in improved estimation consistency (Author, Year)."
- Transition to next sub-section: "We then move on to [next method/test]."

### 4.4 Academic Vocabulary & Diction

**Methodology vocabulary (top trigrams):**
- "the null hypothesis" (19), "null hypothesis is/of" (14) — overwhelmingly the most frequent phrase
- "based on the" (13), "according to the" (7)
- "the dependent variable" (9), "the existence of" (10)
- "the presence of" (5), "the cross sectional" (6)
- "differences of the" (6), "the effect of" (6)
- "in the panel" (6), "the convergence club" (7)
- "short and long" (6), "and long term" (6)

**Method-referencing convention:** Named methods are always accompanied by their origin citation: "[Method Name], as proposed by [Author (Year)]" or "[Method] developed by [Author (Year)]". This is a rigid pattern — methods are never mentioned without citation attribution in this section.

**Equation-adjacent prose:** Variables are defined in prose immediately following equations using consistent patterns:
- "where [symbol] is the [variable definition]"
- "[symbol] denotes [definition]"
- "[symbol] represents [definition]"

**Hedging profile (lowest of all chapters):**
- Limited hedging (model sections are declarative about method)
- "may" (14), "could" (12), "should" (8), "suggests that/indicates that" (7)
- Relevant hedge: "This approach can be [used/applied/interpreted as]..."

### 4.5 Voice & Tense Conventions

**Voice:** Mixed with active preference for procedural steps (active for procedure, passive for math).

- Procedural description: "we use", "we estimate", "we employ", "we test" (active)
- Mathematical description: passive dominant ("is denoted by", "can be expressed as", "is assumed to be")
- Equation explanation: "where X is...", "the term Y captures..."

**Tense:** Present tense dominant present tense dominant.
- Method description: present ("We use a VAR model", "We estimate the following equation")
- Prior work that developed the method: present ("Phillips and Sul (2007) show that...")
- Diagnostic test results: present ("The test indicates...", "Results show that...")

### 4.6 Transition & Cohesion Patterns

**Transition profile :**

- Enumeration heavy: "first" (21), "second" (19), "First" (10), "Second" (10), "Finally" "Third" (2)
- Sequential procedural: "Then we...", "We then...", "Next we..." — step-by-step method exposition
- "Thus" (12), "Therefore" (4), "Consequently" (4) — logical inference
- "However" (9) — method limitation or assumption qualification
- "In addition" "Moreover" (5), "Furthermore" (5) — adding methodological details
- "Specifically" (4) — elaborating on a method detail
- "Similarly" (5), "In contrast" (2) — comparing methods
- "In line with" (2), "consistent with" (3) — alignment with prior methodological choices

**Distinctive pattern:** Model sections use sequential/procedural logic ("first we do X, then we do Y") rather than argumentative logic. Each paragraph represents one step in the estimation pipeline.

---

## BATCH 5: DATA & VARIABLES WRITING NORMS

### 5.1 Structure Logic

**Standard Data & Variables section structure:**

1. **Data sources** (1 paragraph): Source institution, database name, coverage. "We obtained the data from [source], which is..."
2. **Sample description** (1 paragraph): Countries/firms/individuals, time period, inclusion/exclusion criteria. "We use [panel/cross-sectional/time-series] data covering [period] for [N] [units]."
3. **Variable definitions** (1-2 paragraphs): Dependent variable(s), key independent variable(s), control variables. Each variable defined with source database and measurement.
4. **Descriptive statistics** (0.5-1 paragraph + table): Summary statistics table, key patterns in the data.
5. **Preliminary diagnostics** (0.5-1 paragraph): Stationarity tests, correlation analysis, cross-sectional dependence tests.

### 5.2 Paragraph Layout

- Average paragraph: 72 words (P50 = 52 words, P75 = 95 words).
- Data-source paragraphs are typically longer (listing multiple sources/variables).
- Variable-definition paragraphs are medium-length, formulaic, with consistent structure per variable.
- Statistical test paragraphs are shorter, often formulaic ("Table X shows that since probability values are less than 0.01, the null hypothesis of [test] is rejected...").

### 5.3 Opening & Closing Sentence Templates

**Section openers:**

| Template | Frequency |
|---|---|
| "In this section, we present the [data sources/sample selection/variable definitions]..." | 5+ |
| "We use [data type] covering the [period] for [N] [units]..." | 8+ |
| "The data for the empirical analyses were extracted from [source]..." | 3+ |
| "We obtained the data from the [database name] database, which is..." | 4+ |

**Variable-definition templates:**
- "[Variable name] is measured as [definition], sourced from [database]."
- "[Variable name]: [definition]. Source: [database]."
- "The dependent variable is [name], which captures [definition]."
- "Following [Author (Year)], we measure [variable] as [definition]."

**Sub-section closers:**
- "Table [N] presents the [data/statistics/results]. [Insert Table N about here]"
- "The [test] results indicate that [finding], suggesting that [implication]."
- "[Variable] is [I(0)/I(1)/stationary] at the [X]% significance level."

### 5.4 Academic Vocabulary & Diction

**High-frequency vocabulary :**

*Measurement/source language:*
- "based on the" (43), "the number of" (46), "the ratio of" (15)
- "we use the" (15), "according to the" (14), "used in the" (15)
- "the dependent variable" (13), "the percentage of" (13)
- "consistent with the" (12), "in line with" (11)

*Temporal framing:*
- "the long term" (45), "the short term" (16), "short and long" (13)
- "in the short" (20), "in the long" (22), "the sample period" (13)
- "over the period" (10), "pre and post" "the post covid" (12)

*Statistical vocabulary:*
- "the null hypothesis" (16), "the degree of" (19)
- "there is no" (13), "at the level" (12)
- "the results of" (12), "the value of" (11)

**Prose conventions:**
- Variables are introduced as "[Name] ([ACRONYM])": "Gross Domestic Product (GDP)", "Foreign Direct Investment (FDI)"
- After definition, acronyms are used consistently, never reverting to full name
- Measurement always includes unit: "in constant 2010 US$", "as a percentage of GDP", "in logs"

**Hedging profile (moderate):**
- "may" (59), "likely" (32), "suggests that" (16)
- "generally" (15), "should" (15), "tend(s) to" (17)
- "could" (16), "might" (9), "would" (9)
- "typically" (4)

### 5.5 Voice & Tense Conventions

**Voice:** Mixed (active for data sources, passive for definitions).

- Data source descriptions: "we use", "we obtain", "we collect" (active)
- Variable definitions: passive tendency ("is measured as", "is defined as", "is calculated as")
- Sample descriptions: mixed, with passive preferred for inclusion criteria
- Test descriptions: "we test for", "we conduct", "we apply"

**Tense:** Present tense dominant present tense dominant.
- Data description: present ("The data cover...", "The sample includes...")
- Test results: present ("The test indicates...", "Results confirm...")
- Historical data context: past ("Data were collected from...")

### 5.6 Transition & Cohesion Patterns

**Transition profile :**

- Enumeration: "first" (63), "second" (35), "First" (19), "Second" (12), "Third" "Finally" (17) — heavily used in variable listing
- "However" (42) — acknowledging data limitations, qualifying variable choices
- "Therefore" (33), "Thus" (16) — justifying variable selection
- "In addition" (19), "Furthermore" (18), "Moreover" (14), "Additionally" (8) — additive for listing variables
- "consistent with" (12), "In line with" (5), "Consistent with" (4) — aligning variable choices with prior literature
- "For example" (12), "In contrast" (12) — exemplification and contrast
- "Specifically" (8), "Hence" "Similarly" (7)

**Distinctive pattern:** AE Data sections heavily use "In line with [Author (Year)]" and "Consistent with [Author (Year)]" to justify variable choices — every variable definition is anchored to precedent.

---

## BATCH 6: EMPIRICAL RESULTS & ROBUSTNESS WRITING NORMS

### 6.1 Structure Logic (Results)

**Standard results presentation sequence:**

1. **Preliminary/Diagnostic results** (0.5-1 paragraph): Unit root, cointegration, specification tests. "We start the empirical part by..."
2. **Baseline/Main results** (2-3 paragraphs): Core regression table(s). Each regression column/model discussed sequentially.
3. **Extended/Additional analysis** (1-2 paragraphs): Heterogeneity, mechanisms, sub-samples. "Further analysis shows that..."
4. **Discussion** (0.5-1 paragraph): Connecting results to hypotheses. "These results are consistent with..."

### 6.2 Structure Logic (Robustness)

**Standard robustness section structure:**

1. **Overview sentence**: "We conduct several robustness checks and present the findings below."
2. **Check 1** (alternative method): "To test the robustness of the results, we [re-estimate/employ/conduct]..."
3. **Check 2** (alternative sample/measure): "As an additional robustness check, we..."
4. **Check 3** (endogeneity): "To address potential endogeneity concerns, we..."
5. **Check 4+**: Alternative specifications, placebo tests, sub-sample analysis.
6. **Summary confirmation**: "The results remain [robust/consistent/qualitatively unchanged]..."

### 6.3 Paragraph Layout

**Results:**
- Average paragraph: 68 words (P50 = 44 words, P75 = 91 words).
- Results sections are table-driven — paragraphs serve as prose commentary on tabulated numbers.
- Typical pattern: "Table X reports... The coefficient on [variable] is [sign] and [significant/insignificant], indicating that [interpretation]. This finding is [consistent with/in contrast to] [prior work]."

**Robustness:**
- Average paragraph: 61 words (P50 = 49 words, P75 = 85 words).
- Similar table-driven structure; paragraphs are shorter and more formulaic.
- Each robustness check is typically a single paragraph (method → result → confirmation).

### 6.4 Opening & Closing Sentence Templates

**Results openers:**
- "Table [N] reports the [baseline/main] results." (5+)
- "The results of the [test/model] are presented in Table [N]." (3+)
- "Columns (1) to (N) of Table [N] present..." (2+)
- "The empirical results show that..." (3+)
- "We start the empirical part by [diagnostic test]." (2+)

**Results closers:**
- "These results are consistent with [Author (Year)] and [Author (Year)]."
- "Overall, the evidence suggests that [summary]."
- "This finding is [robust/consistent] across [specifications/samples]."
- "In sum, [key takeaway]."

**Robustness openers:**
- "We conduct several robustness checks and present the findings below." (3+)
- "To test the robustness of the results, we [action]." (5+)
- "To ensure the robustness of our findings, we conducted additional tests using [alternative]." (3+)
- "As an additional robustness check, we..." (2+)
- "We test the robustness of [finding] by..." (2+)

**Robustness closers:**
- "The results are [consistent with/robust to/remain unchanged after]..."
- "These findings [align with/are in line with] the [baseline] results."
- "In sum, [confirmation statement]."

**Significance notation (rigid pattern, observed across 30+ chunks):**
> "***, **, and * indicate significance at the 1%, 5%, and 10% levels, respectively."
> OR "***, ** and * denote significance at the 1%, 5% and 10% levels, respectively."
>
> "t-statistics are reported in parentheses."
> OR "Standard errors are reported in parentheses."

This is one of the most rigidly formulaic patterns in the entire corpus — every results table is accompanied by this exact notation string.

### 6.5 Academic Vocabulary & Diction

**Results vocabulary (top trigrams):**
- "positive and statistically" (27), "and statistically significant" (22)
- "a positive and" (19), "the results of" (23), "results of the" (24)
- "the null hypothesis" (27), "null hypothesis of" (21)
- "the full sample" (21), "the presence of" (19)
- "results show that" (15), "is associated with" (15)
- "significant at the" (15), "consistent with the" (15)
- "the coefficients of" (15), "a standard deviation" (12)
- "in line with" (13), "is consistent with" (13)

**Result-interpretation vocabulary:**
- "a one standard deviation increase in [X] is associated with a [β] [increase/decrease] in [Y]"
- "[Variable] has a [positive/negative] and statistically significant effect on [outcome]"
- "The coefficient on [variable] is [sign] and [significant/insignificant] at the [X]% level"
- "The magnitude of the effect is [economically meaningful/modest/large]"

**Robustness vocabulary:**
- "the results of" (15), "the robustness of" (13)
- "the results are" (13), "at the [X]% level" (11)
- "robust standard errors" (8), "the coefficients of" (12)
- "positive and significant" (9), "significant at the" (9)
- "results indicate that" (8), "the coefficient of" (13)

**Hedging profile (Results — high):**
- "may" (47), "likely" (44), "suggest(s) that" (46)
- "should" (26), "indicate(s) that" (34)
- "would" (15), "could" (14), "tend(s) to" (16)
- "seem(s) to" (9), "appear(s) to" (5)

**Hedging profile (Robustness — moderate):**
- "may" (28), "should" (23), "likely" (16)
- "indicate that" (15), "suggest that" (12)
- "could" "tend to" (8), "would" (8)

### 6.6 Voice & Tense Conventions

**Results voice:** Mixed (active for interpretation, passive for table narration).
- Table narration: mixed ("Table X reports" / "We report in Table X")
- Coefficient interpretation: active preference ("We find that...", "The results show that...")
- Consistency checks: passive tendency ("This finding is consistent with...")

**Robustness voice:** Mixed (active for test description, passive for confirmation).
- Test description: active ("We conduct", "We test", "We re-estimate")
- Result confirmation: passive tendency ("The results are found to be...")

**Tense:** Present tense dominant in both sections (results: 59 present vs 8 past; robustness: 25 present vs 5 past).
- Results reporting: present ("Table X shows", "The coefficient is", "We find")
- Specific procedural actions: past ("We re-estimated", "We conducted")

### 6.7 Transition & Cohesion Patterns

**Results transitions :**
- "However" (44) — qualifying findings, acknowledging unexpected results
- "consistent with" (30), "in line with" (9) — aligning with prior work/hypotheses
- "Thus" (22), "therefore" (21), "Therefore" (27) — drawing conclusions from results
- "Moreover" (21), "In addition" "Furthermore" (7) — additive
- "In contrast" (16), "On the other hand" (6) — comparing sub-sample results
- "Finally" (16), "Overall" (15), "In sum" (3) — concluding sub-section
- "Specifically" "For example" (6) — elaboration

**Robustness transitions :**
- "However" (21), "Therefore" (18) — strongest signals
- Enumeration: "First" (13), "Second" "First, we" (4), "Second, we" (4), "Finally, we" (2)
- "consistent with" (13), "In contrast" (8) — alignment/contrast
- "Specifically" "In addition" "Furthermore" (6)
- "Taken together" (2), "In sum" (1) — summary (less common in robustness)

---

## BATCH 7: CONCLUSION WRITING NORMS

### 7.1 Structure Logic

**Standard conclusion structure :**

1. **Restatement of research objective** (1-2 sentences): "In this paper, we [studied/examined/investigated] [topic]." Past or present perfect to summarize what the paper did.
2. **Summary of key findings** (2-4 paragraphs): The main empirical results, organized by theme. Present tense for findings.
3. **Policy implications** (1-3 paragraphs): "The findings of this paper have several important policy implications. First,... Second,... Third,..." This is a rigid, enumerated structure in AE conclusions. Policy recommendations use "should" heavily.
4. **Limitations & future research** (1 paragraph): "Future research could...", "An interesting direction for future research would be...", "Our study suffers from a number of limitations..."

**Distinctive AE pattern:** The policy implications section is substantially developed — often longer than the findings summary. This reflects AE's applied economics orientation: conclusions must bridge to real-world policy.

### 7.2 Paragraph Layout

- Average paragraph: 94 words (largest of all chapters after abstract, reflecting the discursive nature of implications).
- P50: 68 words, P75: 111 words.
- Policy implication paragraphs are the longest, often containing multi-sentence recommendations.
- Limitation paragraphs are shorter and formulaic.
- Finding-summary paragraphs are medium-length.

### 7.3 Opening & Closing Sentence Templates

**Section openers (study restatement):**

| Template | Frequency |
|---|---|
| "In this paper, we [studied/examined/investigated] [topic]..." | 8+ |
| "This paper [reports/conducts/proposes] [action]..." | 4+ |
| "We have studied [topic] for [context] through [methods]." | 2+ |
| "[Context sentence]. This paper, adopting [method], provides useful insights into..." | 3+ |

**Finding-summary templates:**
- "The findings reveal that..." (2+)
- "Our findings [demonstrate/show/suggest/confirm] that..."
- "The results [indicate/suggest] that..."
- "We find that..."
- "Our analysis further demonstrates that..."

**Policy-implication openers:**
- "The findings of this paper have several important policy implications. First,... Second,... Third,..." (4+)
- "Our findings have significant implications for policymakers and [financial regulators/other actors]..."
- "Policy implications — First, [policy recommendation]."
- "In terms of policy, this means that..."

**Limitation & future research templates:**
- "Future research could [incorporate/examine/extend/explore]..." (10+)
- "Our study suffers from a number of limitations. [limitation 1]. [limitation 2]."
- "An interesting direction for future research would [surround/be to/involve]..."
- "Methods like [X] or [Y] could be applied to detect such [non-linearities/effects] and better model these relationships."
- "Moreover, future studies could expand the [dataset/sample] to include [more diverse/additional] [countries/firms/periods]."

**Section closers (distinctive patterns):**
- Implication-driven: "Consequently, [policy recommendation summary]."
- Forward-looking: "In future, we will further [extend/expand/explore]..."
- Contribution-focused: "This study contributes to the literature by [contribution]."

### 7.4 Academic Vocabulary & Diction

**High-frequency vocabulary :**

*Research-summary vocabulary:*
- "the impact of" (21), "the effects of" "the relationship between" (9)
- "the results of" "based on the" (8)
- "we use the" (6), "in this paper" (5)

*Policy vocabulary:*
- "the development of" (15), "the importance of" (10)
- "should" (dominant — THE most frequent hedge word in conclusions, almost exclusively for policy recommendations)
- "the market should" (5), "the government should" (2+)
- "Policymakers should [consider/implement/adopt]..."
- "It is important for [entity] to [action]..."

*Limitation vocabulary:*
- "However" (22), "potential measurement error" (1+)
- "future research could/should" (12+), "future studies could" (5+)
- "one limitation", "a number of limitations"

*Contribution-summary vocabulary:*
- "contribute/contributes/contribution" (16)
- "extend/extends/extension" (7)

**Hedging profile (policy-heavy):**
- "should" (83) — overwhelmingly dominant, used for policy recommendations
- "may" (39), "could" (32), "would" (24) — for future research suggestions
- "suggest(s) that" (17), "indicate(s) that" (8) — for finding interpretation
- "likely" "might" "tend(s) to" (6)

### 7.5 Voice & Tense Conventions

**Voice:** Mixed with active preference for findings (active for findings summary).

- Study summary: active "we" ("We have studied", "We examined", "We find that")
- Findings: mixed ("The findings reveal" / "We find")
- Policy recommendations: passive tendency ("Policymakers should consider...", "Strategies should be implemented...") but also active imperatives

**Tense:** Present dominant for findings present tense dominant, with a specific pattern:
- **Present perfect** for paper summary: "We have studied", "This paper has examined"
- **Present tense** for findings: "The results show", "The findings reveal"
- **Past tense** for specific procedural actions: "We used two econometric approaches"
- **Conditional/future** for future research: "Future research could", "would be"

### 7.6 Transition & Cohesion Patterns

**Transition profile :**

- Enumeration (policy): "First" (21), "Second" (18), "Third" (10), "Finally" (12) — heavily used for listing policy implications
- "However" (22) — qualifying findings, acknowledging limitations
- "Therefore" (14), "Thus" (10), "Hence" "Consequently" (3) — consequence, often leading to policy
- "In addition" (13), "Furthermore" (10), "Moreover" (9), "Additionally" (8) — additive
- "Overall" (8) — summary signal
- "consistent with" (12), "In contrast" (5), "Similarly" (2) — comparison
- "For instance" (5), "For example" (3), "In particular" (4)
- "Meanwhile" (3), "At the same time" (4) — parallel observations

**Distinctive conclusion cohesion pattern:** The conclusion follows a macro-level structure signaled by explicit section labels or paragraph-openers:
  → "This paper..." (restatement)
  → "The findings/results..." (summary)
  → "First,... Second,... Third,..." (policy implications)
  → "Future research...", "Our study suffers from..." (limitations + future)

---

## CROSS-CUTTING WRITING NORMS (JOURNAL-LEVEL)

These patterns transcend individual chapter types and apply to the entire manuscript.

### C.1 Citation Convention

**Dominant citation style:** Author (Year) format, integrated as grammatical sentence elements. Frequency: numerous occurrences across all chapters.

- "Author (Year) find(s)/show(s)/argue(s) that..." — integrated as sentence subject
- "..., as documented by Author (Year)" — integrated as evidential support
- "(Author Year, Author Year)" — parenthetical for multiple citations
- "Author, Author, and Author (Year)" — three-author first mention
- "Author et al. (Year)" — four+ authors

**Strict rule from data:** The "Author, Year" format (dominant citation style, ... = frequently) appears but is significantly less frequent than "Author (Year)". The parenthetical-only "..., (Author, Year)" style is rare in the narrative flow.

### C.2 "We" as Default Agent

Every chapter type shows active "we" as the standard first-person agent. "I" is never used. "The author(s)" is occasionally used in third-person self-reference but is a minority pattern.

Active "we" frequency by chapter (relative density):
- Abstract: highest density
- Introduction: very high
- Variables: high
- Results: moderate
- Robustness: moderate
- Model: moderate
- Conclusion: moderate
- Review: lowest density — lit reviews use more third-person)

### C.3 Hedging Hierarchy

Hedging intensity decreases as papers move from introduction to conclusion:

**Heavy hedging chapters:** Introduction (most hedged) > Literature Review > Results
**Moderate hedging:** Variables > Robustness > Conclusion
**Light hedging:** Abstract, Model

**Dominant hedge words across all chapters (by total frequency):**
1. "may" — most common
2. "likely"
3. "should" (dual use: hedge + policy recommendation) — dual use: hedge + policy recommendation)
4. "suggest(s) that"
5. "could"
6. "would"
7. "indicate(s) that"

### C.4 Table/Figure Referencing Convention

**Rigid patterns (observed across all empirical chapters):**

- "Table [N] [presents/reports/shows] the [results/statistics]." — Standard reference
- "[Insert Table N about here]" — Placement marker (appears in variables/results)
- "As shown in Table [N]..." (6+), "As shown in Figure [N]..." (5+)
- "***, **, and * indicate significance at the 1%, 5%, and 10% levels, respectively." (observed in the corpus)
- "t-statistics are reported in parentheses." (4+) / "Standard errors are in parentheses." (4+)

### C.5 Prohibited Constructions

Based on their complete absence from the sampled corpus:

- No contractions (don't, can't, won't, it's)
- No rhetorical questions
- No exclamation marks
- No bullet points or numbered lists in prose (only in hypothesis statements)
- No "we try to", "we attempt to", "we hope to"
- No "interestingly", "surprisingly", "remarkably" as stand-alone adverbs (these subjective qualifiers are absent)
- No first-person possessive: no "our country", "our nation" (even when studying the author's own country)
- No "This paper is the first to..." without the qualification "to the best of our knowledge"

### C.6 Fabrication Prohibitions (extends Section Z)

These are NOT stylistic choices — they constitute academic misconduct:

- No invented data points, coefficients, standard errors, p-values, or sample statistics
- No invented literature citations (authors, titles, years, journals, DOIs)
- No altered findings (changing sign, magnitude, or significance of reported results)
- No invented institutional names, policy names, or historical event details
- No fabricated mechanism claims or causal assertions not made by the original authors
- All added citations must include verifiable provenance (see Section Z3-Z4)

---

## RAG RETRIEVAL INTEGRATION

### Retrieval Strategy

When rewriting a manuscript section to match AE style, retrieve relevant exemplar chunks from the vector database:

```
Vector DB Path: <REPO_ROOT>/data/economics_papers_vectors.jsonl
FAISS Index: <REPO_ROOT>/data/economics_papers.index
Metadata: <REPO_ROOT>/data/economics_papers_meta.json
```

**Retrieval procedure (Python):**
```python
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import os

# Set repo root to the directory containing this skill
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))  # or set manually

# Load model and index
model = SentenceTransformer('all-mpnet-base-v2')
index = faiss.read_index(os.path.join(REPO_ROOT, 'data', 'economics_papers.index'))

# Load metadata
with open(os.path.join(REPO_ROOT, 'data', 'economics_papers_meta.json'), 'r') as f:
    metadata = json.load(f)

# Load JSONL records for full text retrieval
records = []
with open(os.path.join(REPO_ROOT, 'data', 'economics_papers_vectors.jsonl'), 'r', encoding='utf-8') as f:
    for line in f:
        records.append(json.loads(line))

def retrieve_exemplars(query_text, chapter_type=None, top_k=5):
    """
    Retrieve the most stylistically relevant AE exemplars for a given query.
    
    Args:
        query_text: The draft text to find exemplars for
        chapter_type: Optional filter (abstract/introduction/review/model/
                      variables/results/robustness/conclusion)
        top_k: Number of exemplars to return
    
    Returns:
        List of {"text": ..., "source": ..., "chapter_type": ...}
    """
    query_vec = model.encode([query_text])
    
    # Search FAISS
    distances, indices = index.search(query_vec.astype(np.float32), top_k * 2)
    
    results = []
    for idx in indices[0]:
        if idx < len(metadata):
            rec = records[metadata[idx]['jsonl_index']]
            ct = rec['id'].rsplit('_', 2)[-2]
            if chapter_type and ct != chapter_type:
                continue
            results.append({
                "text": rec['text_chunk'],
                "source": rec['id'],
                "chapter_type": ct,
                "distance": float(distances[0][len(results)])
            })
            if len(results) >= top_k:
                break
    
    return results
```

**Retrieval usage in rewriting:**
1. For each section being rewritten, retrieve the top-5 most similar AE exemplars of the same chapter type.
2. Compare the draft against the exemplars across all 6 dimensions (structure, paragraphing, openings/closings, vocabulary, voice/tense, transitions).
3. Apply the specific norms from this skill document, cross-referencing with the retrieved exemplars as concrete models.
4. When a norm conflicts with a specific exemplar, the norm (representing majority pattern) takes precedence.

### Chapter-Type Filtering for Retrieval

When rewriting a specific section, filter retrieved exemplars to the matching chapter type:
- Abstract → `chapter_type == "abstract"`
- Introduction → `chapter_type == "introduction"`
- Literature Review → `chapter_type == "review"`
- Theoretical Model → `chapter_type == "model"`
- Data & Variables → `chapter_type == "variables"`
- Empirical Results → `chapter_type == "results"`
- Robustness → `chapter_type == "robustness"`
- Conclusion → `chapter_type == "conclusion"`

### Retrieval-Enhanced Rewriting Protocol

1. **INPUT:** User provides manuscript section text + target chapter type
2. **RETRIEVE:** Query vector DB for top-5 most similar AE published exemplars of same chapter type
3. **ANALYZE GAPS:** Compare draft against the 6 dimensions in this skill document for that chapter type. Identify specific deviations.
4. **REWRITE:** Apply norm corrections. Use retrieved exemplars as concrete style references for sentence construction, transition placement, and vocabulary choice.
5. **VERIFY:** Check rewritten text against the "Prohibited Constructions" list (C.5). Re-retrieve and re-compare if uncertain.

---

## USAGE INSTRUCTIONS

This skill is designed to be invoked when an economics scholar provides a manuscript draft and requests rewriting to Applied Economics journal standards.

**Input required:**
- Manuscript section text
- Chapter type (abstract/introduction/literature review/theoretical model/data & variables/empirical results/robustness/conclusion)

**Output:**
- Rewritten text conforming to AE norms
- Specific changes annotated with reference to the norm applied

**Quality control:**
- Every stylistic claim must be verifiable against both this skill document and at least one retrieved exemplar
- When uncertain about a pattern, default to the most conservative form documented above
- Never invent conventions not attested in the corpus
