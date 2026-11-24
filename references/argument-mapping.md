# Argument and Judgment Correspondence

Read this reference after the material whitelist is confirmed and before proposing an outline. Its purpose is to map the new opposing filing or challenged judgment to the lawyer's existing positions, the courts' reasoning, and the written record without drafting the pleading prematurely.

## Preconditions

Do not begin until:

- the target document and represented parties are known;
- the procedural cutoff and visibility whitelist are fixed;
- the operative opposing filing or challenged judgment is available;
- the lawyer's relevant filed or confirmed prior positions have been identified.

Use only visible materials. A later lawyer final or later judgment may be used only in retrospective evaluation after the target output is frozen.

When the source is readable and the page is unstable, map the proposition as a paraphrase with its document and stable internal locator, and mark page verification pending. Keep exact quotations with unverified pages out of approved text.

## 1. Anchor the map to the target task

Start from the document that creates the current writing task:

| Target document | Mapping anchor |
|---|---|
| Second-instance defense | every material appeal ground and requested change to the first-instance result |
| Retrial defense | every asserted retrial ground and the underlying factual or legal proposition |
| Retrial application | every challenged holding or reasoning step that materially produced the unfavorable effective result |

Break each anchor into atomic propositions. One proposition should contain one actor, factual or legal assertion, and intended consequence. Separate:

- the requested result;
- the legal ground;
- the factual premise;
- the evidentiary premise;
- the inference connecting them.

Do not hide several propositions under a broad label such as “事实认定错误” or “原审判决正确”.

## 2. Build one correspondence record per proposition

Use this minimum record:

```yaml
map_id:
applicable_party:
target_proposition:
target_source_and_page:
proposition_type: result/fact/evidence/law/procedure/inference
prior_lawyer_position:
prior_lawyer_source_and_page:
first_judgment_position_and_page:
second_judgment_position_and_page:
court_relation:
record_support_and_page:
admission_or_inconsistency:
newness:
response_status: already-answered/partly-answered/unanswered/not-needed
suggested_treatment: retain/reframe/merge/reserve/delete/lawyer-decision
uncertainty_or_missing_material:
```

Use `not applicable` rather than inventing a position for a stage or party. Paraphrases must remain distinguishable from exact quotations.

## 3. Label relationships precisely

### Opposing position compared with prior lawyer position

Use one of:

- `repeated`: the same material proposition was already answered;
- `restated`: wording changed but the proposition and requested consequence did not;
- `narrowed`: part of the prior position remains;
- `expanded`: a prior position now includes an additional premise or consequence;
- `contradicted`: the party's present proposition conflicts with its earlier statement;
- `abandoned`: a previously material proposition is no longer pursued;
- `new`: the material proposition could not be derived from the earlier submission.

### Judgment compared with lawyer position

Use one of:

- `explicitly-adopted`: the judgment states the same material reasoning;
- `substantively-adopted`: the reasoning is materially the same although the wording differs;
- `rejected`;
- `not-addressed`;
- `resolved-on-other-ground`;
- `ambiguous`.

The same result does not prove that the court adopted the lawyer's reasoning. Do not write “法院已认可我方观点” unless the reasoning correspondence supports that statement.

### Record compared with proposition

Use `supports`, `undermines`, `mixed`, `missing`, or `not-reached`. State which part of the proposition the source affects.

## 4. Classify what is genuinely new

Classify newness by substance, not wording:

- `repeated` or `restated`;
- `new-interpretation`: an old fact or exhibit is used to support a materially different inference;
- `new-fact`;
- `new-evidence`;
- `new-law-or-legal-basis`;
- `new-procedural-ground`;
- `new-request-or-result`;
- `court-new-reasoning`: a judgment reaches or supports the result through reasoning not previously advanced by the parties.

An exhibit is not new evidence merely because it is described differently. A claimed new exhibit is not available evidence when the referenced attachment is missing. A court's new reasoning must be reported even when the disposition favors the client, because it may change the response required at the next stage.

For each new item, state:

1. what changed;
2. where the earlier and current versions appear;
3. whether the existing lawyer position already answers it;
4. whether a new response, evidence review, or lawyer decision is required.

Do not create the new response at this stage when it would alter strategy. Present the gap and a proposed direction for lawyer confirmation.

## 5. Map judgment reasoning without overclaiming

For every holding material to the result, extract:

- the court's conclusion;
- the decisive factual finding;
- the evidentiary or legal premise;
- the reasoning step connecting the premise to the conclusion;
- the disposition affected;
- the exact source page.

Then compare that reasoning with the lawyer's earlier position. Use concise judgment quotations only when the exact wording matters. If the court did not address an argument, say so; do not convert silence into adoption or rejection. If the court reached the same result on another ground, preserve that distinction.

## 6. Audit admissions, inconsistencies, and evidence acknowledgments

Search the visible pleadings, hearing transcripts, written evidence opinions, and judgments for:

- changed accounts of the same fact;
- statements about parties, authority, payment, performance, timing, purpose, or document authenticity;
- changes to claims, requests, or legal grounds;
- acknowledgment of an exhibit's authenticity or content;
- statements inconsistent with the current appeal or retrial proposition;
- reliance on a supposedly new exhibit that was not supplied.

Record each candidate with the speaker or submitting party, exact quotation, document and page, necessary surrounding context, the current proposition it affects, and any limitation. Distinguish acknowledgment of authenticity from acknowledgment of content, purpose, probative force, or legal effect. Do not label a statement a binding admission merely because it is unfavorable; identify it as an admission candidate for lawyer review.

## 7. Keep represented subjects separate

Create separate records when one proposition affects represented parties differently. Do not transfer one party's statement, evidence acknowledgment, defense, or procedural role to another party without a stated legal and factual basis. When a joint document is planned, identify which sections are shared and which are subject-specific.

## 8. Use only the tools needed for this mapping

- Use full-text search to locate repeated terms, amounts, dates, document names, and party statements across the visible corpus.
- Use document or extracted-text comparison to align process and final versions and to distinguish rewording from substantive change.
- Use the rendered DOCX or PDF page to verify every quotation and page citation that enters the report.

Search results and diffs identify candidates; they do not decide legal equivalence. Make the final relationship classification from the source context.

## 9. Present the lawyer-facing analysis

In the single complete analysis report, present:

1. a concise procedural and adjudication history;
2. a proposition-by-proposition correspondence table;
3. repeated or already answered opposing positions;
4. genuinely new opposing positions and why they are new;
5. court reasoning that adopted, rejected, omitted, or changed the lawyer's earlier approach;
6. admissions, inconsistencies, and evidence acknowledgments with exact pages;
7. differences among represented subjects;
8. missing materials, uncertainty, and issues requiring lawyer strategy;
9. recommended treatment of each proposition, without drafting the pleading or locking the outline.

The report must be complete even though the later pleading will be selective. The lawyer chooses the current-stage dispute focus at the outline gate.

## 10. Quality gate

Before presenting the analysis, verify:

- every material anchor proposition is accounted for;
- every relationship label is supported by source context;
- every direct quotation has a verified document and page. A material factual proposition with an unresolved page has a source locator and a visible verification warning;
- court adoption is not inferred from disposition alone;
- new wording is not mislabeled as a new position;
- new facts, evidence, law, procedure, and court reasoning remain distinct;
- represented subjects are not conflated;
- excluded or future documents did not influence the analysis;
- unknown or ambiguous points are identified rather than completed by inference;
- no pleading prose or unapproved strategy has been drafted.
