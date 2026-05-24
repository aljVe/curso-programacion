---
name: text-deduplicator
description: Detect and remove unnecessary duplicated text in Markdown or plain text while preserving meaning, structure, warnings, and citations.
---

Use this skill when the user asks to deduplicate, compress, clean up, or remove repeated text from Markdown, course material, documentation, drafts, transcripts, notes, or plain text.

## Goal

Reduce redundant text without losing information. Prefer conservative edits: remove repeated wording, merge overlapping paragraphs, and keep the clearest version.

## Safety rules

- Do not remove legal, privacy, security, clinical, safety, consent, or validation warnings just because they appear more than once. Instead, consolidate them only when the repeated warning is in the same section or clearly unnecessary.
- Do not remove citations, links, tables, code blocks, front matter, slide separators, headings, or list structure unless the user explicitly asks for structural rewriting.
- Do not deduplicate examples that intentionally compare similar cases.
- Preserve Spanish tone, terminology, and audience level when editing Spanish course content.
- If the text contains patient, clinical, or regulated data, do not send it to external services unless the user explicitly confirms that it is synthetic, anonymized, or authorized.

## Workflow

1. Identify the target file or text range.
2. Inspect nearby context before editing. For Markdown, note headings, slide separators, code fences, lists, and tables.
3. Run the helper script when files are local:

   ```powershell
   python .agents\skills\text-deduplicator\scripts\dedupe_markdown.py --input <file.md> --threshold 0.88
   ```

   For slide decks or short notes, lower the block size:

   ```powershell
   python .agents\skills\text-deduplicator\scripts\dedupe_markdown.py --input <file.md> --threshold 0.88 --min-chars 40
   ```

4. Classify repeated content:
   - `exact`: same normalized paragraph appears more than once.
   - `near`: paragraphs overlap heavily and can likely be merged.
   - `intentional`: repetition that teaches, warns, contrasts, or preserves local context.
5. Edit only the repeated text that is genuinely unnecessary.
6. After editing, rerun the helper script and summarize:
   - paragraphs removed or merged;
   - important content preserved;
   - remaining repetitions that were intentionally kept.

## Editing policy

When removing duplicate material:

- Keep the version closest to the most relevant heading.
- Keep the version with the most precise wording, citations, examples, or caveats.
- If two paragraphs partially overlap, merge them instead of deleting one wholesale.
- If repeated text appears in both slides and theory documents, do not remove it automatically; slides and long-form notes often need parallel summaries.
- For Slidev files, preserve `---` slide separators and keep slide text brief.

## Output format

For a review-only task, return:

```markdown
## Duplicados detectados
- Archivo/seccion:
- Tipo: exact | near | intentional
- Recomendacion:

## Propuesta de limpieza
- Mantener:
- Eliminar o fusionar:
- Riesgo:
```

For an edit task, make the changes and then report the exact files modified plus verification results.
