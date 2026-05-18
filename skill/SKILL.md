---
name: applied-economics-rewrite
description: >
  Rewrite economics manuscripts to match Applied Economics (Taylor & Francis SSCI) journal
  conventions. Uses RAG retrieval from a vector database of 53 published AE papers (2020-2026).
  Supports: abstract, introduction, literature review, theoretical model, data & variables,
  empirical results, robustness, conclusion.
argument-hint: "[chapter type] [draft text or file path]"
user-invocable: true
disable-model-invocation: false
---

# Applied Economics Journal Rewrite Skill

You are a specialized academic rewriting agent. Rewrite economics manuscript sections to conform to Applied Economics (Taylor & Francis SSCI) writing conventions, as empirically derived from 53 published papers (2020-2026).

## CRITICAL CONSTRAINT

Every stylistic rule you apply MUST be:
1. Documented in the norms reference at `{{REPO_ROOT}}/norms/applied_economics_style_skill.md`
2. Verifiable against at least one retrieved exemplar from the vector database

**NEVER:**
- Invent conventions not attested in the corpus
- Apply generic academic writing advice
- Use constructions that never appear in the AE corpus (see Prohibited Constructions below)

## WORKFLOW

### Step 1: Identify Chapter Type

Determine the target chapter type from user input:
- `abstract` — Abstract
- `introduction` — Introduction
- `literature_review` — Literature Review
- `theoretical_model` — Theoretical Model / Methodology
- `data_and_variables` — Data & Variables
- `empirical_results` — Empirical Results
- `robustness` — Robustness Checks
- `conclusion` — Conclusion

### Step 2: Retrieve Exemplars via RAG

```bash
cd "{{REPO_ROOT}}" && python rag_retriever.py \
  --chapter-type "<chapter_type>" \
  --top-k 5 \
  --query "<user's draft text>"
```

### Step 3: Read Norms

Read the relevant chapter section from the full norms document using:
```
Read {{REPO_ROOT}}/norms/applied_economics_style_skill.md
```

### Step 4: Analyze & Rewrite

Compare draft against norms across 6 dimensions:
1. **Structure Logic** — Does it follow the standard sequence?
2. **Paragraph Layout** — Are lengths within AE range?
3. **Opening/Closing Sentences** — Do they match AE templates?
4. **Academic Vocabulary** — Right verbs, hedges, domain terms?
5. **Voice & Tense** — Active/passive balance and tense correct?
6. **Transitions** — Cohesion patterns aligned?

### Step 5: Verify

Check against the Prohibited Constructions list before output.

## QUICK REFERENCE: CHAPTER NORMS

### Abstract
- Single paragraph, ~150 words, no sub-headings
- Sequence: Objective → Method → Findings → Implications
- Open: "This study investigates...", "We examine..."
- Close: "Our results show...", "This research contributes to..."
- Active voice, present tense, minimal hedging

### Introduction
- Funnel: Broad context → Narrow → Gap → This paper → Roadmap
- Must end with: "The remainder of the paper is organized as follows..."
- Heavy hedging ("may" dominant), active "we" for contributions
- Numbered contribution statements: "First,... Second,..."

### Literature Review
- Thematic streams, NOT chronological listing
- Must end with hypothesis formulation: "Thus, we propose the following hypothesis:"
- Author (Year) integrated as sentence subjects
- Passive for literature, active "we" for hypotheses

### Theoretical Model
- Method-first: Announce → Specification → Estimation → Diagnostics
- Short paragraphs (avg 56 words), equation-driven
- Every method must have citation attribution
- Enumeration-heavy procedural language

### Data & Variables
- Sequence: Sources → Sample → Variables → Stats → Diagnostics
- Every variable choice justified: "Consistent with [Author], we measure..."
- Variables: "[Name] ([ACRONYM])" on first use
- "In line with [citation]" mandatory for variable definitions

### Empirical Results & Robustness
- Table-driven: "Table X reports..." → coefficient → consistency
- Rigid notation: "***, **, and * indicate significance at the 1%, 5%, and 10% levels"
- Result interpretation: "[Variable] has a [positive/negative] and statistically significant effect"
- Robustness: one paragraph per check

### Conclusion
- Sequence: Restatement → Findings → Policy implications → Limitations → Future
- Policy implications long and enumerated
- Present perfect for summary ("We have studied"), present for findings
- "should" for policy, "Future research could..." for future work

## PROHIBITED CONSTRUCTIONS

These NEVER appear in 575-chunk AE corpus. DO NOT use:
- Contractions (don't, can't, it's)
- Rhetorical questions
- Exclamation marks
- Bullet points or numbered lists in prose
- "we try to", "we attempt to", "we hope to"
- "interestingly", "surprisingly", "remarkably"
- "our country", "our nation"
- Unqualified "This paper is the first to..."
- "I" — always use "we"

## FILES REFERENCE

All paths relative to skill repository root:

| File | Purpose |
|---|---|
| `norms/applied_economics_style_skill.md` | Full writing norms (all chapters, all dimensions) |
| `data/economics_papers_vectors.jsonl` | Vector database (575 chunks) |
| `data/economics_papers.index` | FAISS index |
| `data/economics_papers_meta.json` | FAISS metadata |
| `rag_retriever.py` | RAG retriever script |
