# text-deduplicator

Local Agent Skill for detecting and cleaning unnecessary repeated text in Markdown or plain text.

It follows the OpenAI Skills pattern: a folder with a `SKILL.md` manifest plus optional helper files. The OpenAI guide describes a skill as a versioned bundle with `SKILL.md`, and local shell usage attaches the skill by name, description, and local path.

## Local use

Run the detector:

```powershell
python .agents\skills\text-deduplicator\scripts\dedupe_markdown.py --input slides.md --threshold 0.88
```

For shorter repeated bullets:

```powershell
python .agents\skills\text-deduplicator\scripts\dedupe_markdown.py --input slides.md --threshold 0.88 --min-chars 40
```

Use the skill from the Responses API local shell mode with the JSON shape in:

```text
.agents/skills/text-deduplicator/examples/local-shell-response.json
```

## What it does

- Finds exact duplicate paragraphs.
- Finds near-duplicate paragraphs above a configurable similarity threshold.
- Leaves the final removal/merge decision to the agent, because some repetition is intentional in course material, slides, warnings, and summaries.
