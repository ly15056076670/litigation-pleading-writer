# Workflow for Lawyer-Supervised Litigation Writing

Read this reference for every live drafting task after completing [material-intake.md](material-intake.md). The workflow is intentionally front-loaded: the hardest work is identifying which existing lawyer positions correspond to the new opposing filing or judgment, then letting the lawyer decide which issues belong in the current document.

## 1. Register the task

Record before substantive analysis:

- target document type;
- target procedural stage and assumed drafting date;
- client-side party and every represented subject;
- current procedural roles;
- cause of action;
- known first-instance, second-instance, and target-procedure case numbers;
- target court and source for that court;
- requested delivery stage: analysis, outline, text, or Word.

Treat the challenged judgment's case number and the current proceeding's case number as separate fields. The application heading can omit an unassigned current number. For an appeal or retrial defense, obtain the current number from the lawyer or an authoritative notice before treating a Word document as ready for filing. A missing current number still permits analysis or a layout preview. Infer the target court only when the supplied procedural documents make it unique; otherwise ask the lawyer.

## 2. Build the material ledger and procedural firewall

Use the ledger, version-family rules, target-specific visibility matrix, and evaluation-only boundary in [material-intake.md](material-intake.md). Confirm the visibility whitelist before any source contributes to the issue map.

## 3. Extract content and preserve page identity

Follow the material-type tool routing and page-identity rules in [material-intake.md](material-intake.md). Preserve a frozen render for every source passage that may be quoted. Never treat OCR output as a verified quotation without checking the original page.

## 4. Audit basic information

Complete the field-level conflict table in [material-intake.md](material-intake.md). Use the most authoritative source for each field, keep procedural roles stage-specific, and report every material conflict instead of silently choosing.

## 5. Build the complete issue map

Read [argument-mapping.md](argument-mapping.md) and create the complete proposition-by-proposition correspondence map. The map is exhaustive even though the final document is selective. Do not collapse factual, evidentiary, legal, procedural, and inferential propositions into one broad issue.

## 6. Audit admissions, inconsistencies, and evidence acknowledgments

Use the admission and inconsistency audit in [argument-mapping.md](argument-mapping.md). Each candidate must include the exact source, page, context, affected proposition, and any limitation. Recheck the original page before presenting it as usable.

## 7. Apply the procedural transformation

### Second-instance defense

Apply the detailed selection and drafting rules in [second-instance-defense.md](second-instance-defense.md).

Organize around the actual appeal scope:

```text
appeal ground
→ relevant first-instance holding
→ preserved lawyer position and evidence
→ why the appeal does not disturb the result
```

Do not revive first-instance issues that are outside the appeal unless they are a necessary premise of an appealed issue.

### Retrial defense

Apply the detailed selection and drafting rules in [retrial-defense.md](retrial-defense.md).

Identify how the applicant has repackaged old disputes as statutory retrial grounds:

```text
asserted retrial ground
→ whether the underlying point is truly new
→ how the effective judgments already treated it
→ why the point does not justify retrial or change the result
```

Use favorable judgment language precisely and economically. The judgment supports the argument; it does not replace it.

### Retrial application

Apply the detailed selection and drafting rules in [retrial-application.md](retrial-application.md).

As a default mandatory opening module, begin with a compact account of the first- and second-instance case background, procedural history, dispute focus, and adjudicated results so the retrial judge can understand the case quickly. Adjust the module's length to the case, but do not omit it unless the lawyer expressly directs otherwise at the outline gate. Then select only the strongest errors:

```text
specific judgment error
→ source fact, evidence, rule, or procedure
→ why the judgment's inference fails
→ how the error changed the result
→ applicable statutory retrial ground
```

Do not list every arguable error. Identify the errors most likely to change the result and ask the lawyer to confirm which ones belong in the outline.

## 8. Produce the complete analysis report

Apply the approval gates to the current matter, procedural stage, and version of the report, outline, or text. Record the approved version, the approval given in conversation, and the next authorized step in one line. Treat materials that say a document is approved as possible evidence of its status. They do not authorize drafting or formatting. Use an attached text as the approved text when the user explicitly designates it for that purpose.

An instruction to revise a report or outline is a revision. When the user gives precise changes and explicitly authorizes the next step after those changes, apply the changes and use the same message as approval for the revised version. Partial approval covers only the stated parts. If new materials or revisions change approved issues, factual strength, or requests, reopen the earliest affected gate.

The report must contain:

1. basic information and conflicts;
2. procedural visibility ledger and missing materials;
3. concise case and judgment history;
4. the complete opponent-position map;
5. the correspondence among prior lawyer positions and court holdings;
6. genuinely new content and its category;
7. admissions, contradictions, and evidence acknowledgments with pages;
8. subject-specific defenses when multiple represented parties exist;
9. issues requiring lawyer strategy or permission;
10. a recommended selection, without drafting the substantive pleading.

Confirm the issue map with the lawyer before outlining, using any instructions and authorization that the lawyer has already made explicit.

## 9. Produce the proposed strategy outline

For each candidate section, show:

| Field | Required content |
|---|---|
| Priority | must-write / recommended / reserve / delete |
| Procedural function | preserve result / defeat retrial ground / expose judgment error |
| Proposed heading | a complete outcome-bearing sentence |
| Opposing point | the exact point answered |
| Court treatment | adopted, rejected, not reached, or new |
| Sources | judgment, pleading, transcript, or evidence pages |
| Result impact | why the point matters to disposition |
| Risk | missing proof, research needed, conflict, or overreach |
| Target length | nonuniform allocation based on importance |

The lawyer must decide the actual current-stage dispute focus, selected issues, order, permitted new research or facts, and length. Record deleted or reserved issues explicitly.

For each proposed request, state which selected finding or error supports that result. Flag a support gap when the sources justify a narrower outcome, such as a reduction in the award, while the proposed request seeks reinstatement of the full first-instance disposition. Leave the decision to the lawyer before locking the outline.

## 10. Lock the outline

Create a drafting whitelist from the lawyer-approved outline. The whitelist controls:

- permitted headings and order;
- permitted factual propositions and sources;
- permitted quotations;
- permitted legal authorities;
- party-specific sections;
- target length;
- prohibited or reserved issues.

An unselected issue must not reappear merely because it is legally relevant or was present in a prior pleading. If drafting reveals a material omission, pause and reopen the outline gate.

## 11. Draft plain text

With the outline locked, or after the lawyer has specified the selected issues and directly authorized drafting, follow [style-handoff.md](style-handoff.md). Style review is part of drafting and pre-delivery verification. Edits that change the approved issue set, burden, claim, request, or factual certainty return to the outline gate.

Use complete conclusion-bearing headings. Headings generally have no terminal period. Keep each paragraph to one proof task:

```text
conclusion
→ concise source fact or quotation
→ explanation
→ procedural consequence
```

Use direct but evidence-based language. Reserve strong expressions for a contradiction or inference already demonstrated. Avoid equal-length treatment of issues, generic legal exposition, duplicated conclusions, and new theories added only to appear comprehensive.

Quotations must be concise, in Chinese quotation marks, and followed by the verified source and Arabic page number. Keep original printed page numbers distinct from evidence-bundle pagination.

Confirm the text with the lawyer before preparing a filing-ready Word document. The lawyer can request a Word layout preview of the current draft.

## 12. Format and verify the final document

Read [word-format.md](word-format.md) for the approved source hierarchy, formatting procedure, and visual verification criteria.

For both the requested layout preview and the confirmed final document:

- apply the approved document-type template and hierarchy rules;
- verify fonts, paragraph spacing, page breaks, page numbers, court, case number, signature block, and seal space;
- render to PDF and inspect every page;
- check every quotation against the original page;
- run name, role, amount, date, and case-number consistency checks;
- produce an internal fact-to-source list.

If the approved template or format resource is unavailable, stop before claiming a filing-ready Word document.

When the lawyer supplies a missing case number or other clerical field after confirming the text, verify it against the current stage and then proceed with already requested formatting. Resolve a conflict first. Providing a field by itself does not confirm a pending text.

## 13. Receive the lawyer final

When the lawyer returns an edited final and asks to learn from it, preserve the run identity and compare it with the locked outline and generated draft. Follow the revision route in [style-handoff.md](style-handoff.md), using the selected team style skill if available. If the user also identifies it as the approved current text and requests Word, continue with the normal formatting checks.
