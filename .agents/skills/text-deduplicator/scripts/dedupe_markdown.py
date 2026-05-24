#!/usr/bin/env python3
"""Find exact and near-duplicate paragraphs in Markdown/plain text."""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paragraph:
    index: int
    start_line: int
    end_line: int
    text: str
    normalized: str


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[^a-z0-9áéíóúüñ]+", " ", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def is_structural_block(block: str) -> bool:
    stripped = block.strip()
    if not stripped:
        return True
    if stripped == "---":
        return True
    if stripped.startswith(("---\n", "```", "|", "#")):
        return True
    return False


def extract_paragraphs(text: str, min_chars: int) -> list[Paragraph]:
    lines = text.splitlines()
    paragraphs: list[Paragraph] = []
    buffer: list[str] = []
    start_line = 1
    in_code_fence = False

    def flush(end_line: int) -> None:
        nonlocal buffer, start_line
        block = "\n".join(buffer).strip()
        buffer = []
        if is_structural_block(block):
            return
        normalized = normalize(block)
        if len(normalized) < min_chars:
            return
        paragraphs.append(
            Paragraph(
                index=len(paragraphs) + 1,
                start_line=start_line,
                end_line=end_line,
                text=block,
                normalized=normalized,
            )
        )

    for line_number, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            if buffer:
                flush(line_number - 1)
            in_code_fence = not in_code_fence
            continue

        if in_code_fence:
            continue

        if not line.strip():
            if buffer:
                flush(line_number - 1)
            start_line = line_number + 1
            continue

        if not buffer:
            start_line = line_number
        buffer.append(line)

    if buffer:
        flush(len(lines))

    return paragraphs


def find_duplicates(paragraphs: list[Paragraph], threshold: float) -> tuple[list[tuple[Paragraph, Paragraph]], list[tuple[float, Paragraph, Paragraph]]]:
    exact: list[tuple[Paragraph, Paragraph]] = []
    near: list[tuple[float, Paragraph, Paragraph]] = []
    token_sets = [set(paragraph.normalized.split()) for paragraph in paragraphs]

    for left_index, left in enumerate(paragraphs):
        left_len = len(left.normalized)
        for right in paragraphs[left_index + 1 :]:
            if left.normalized == right.normalized:
                exact.append((left, right))
                continue
            right_len = len(right.normalized)
            max_possible_ratio = (2 * min(left_len, right_len)) / (left_len + right_len)
            if max_possible_ratio < threshold:
                continue
            left_tokens = token_sets[left_index]
            right_tokens = token_sets[right.index - 1]
            token_union = left_tokens | right_tokens
            if token_union:
                token_overlap = len(left_tokens & right_tokens) / len(token_union)
                if token_overlap < threshold * 0.45:
                    continue
            ratio = difflib.SequenceMatcher(None, left.normalized, right.normalized).ratio()
            if ratio >= threshold:
                near.append((ratio, left, right))

    near.sort(key=lambda item: item[0], reverse=True)
    return exact, near


def preview(text: str, length: int = 180) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= length:
        return compact
    return compact[: length - 3] + "..."


def main() -> int:
    parser = argparse.ArgumentParser(description="Find duplicate paragraphs in Markdown/plain text.")
    parser.add_argument("--input", "-i", type=Path, help="Input Markdown/plain text file. Reads stdin when omitted.")
    parser.add_argument("--threshold", "-t", type=float, default=0.9, help="Near-duplicate similarity threshold, 0.0-1.0.")
    parser.add_argument("--max-near", type=int, default=30, help="Maximum near-duplicate pairs to print.")
    parser.add_argument("--min-chars", type=int, default=80, help="Minimum normalized characters per block.")
    args = parser.parse_args()

    if not 0 <= args.threshold <= 1:
        parser.error("--threshold must be between 0 and 1")

    if args.input:
        text = args.input.read_text(encoding="utf-8")
        label = str(args.input)
    else:
        text = sys.stdin.read()
        label = "<stdin>"

    paragraphs = extract_paragraphs(text, args.min_chars)
    exact, near = find_duplicates(paragraphs, args.threshold)

    print(f"# Duplicate report: {label}")
    print(f"Paragraphs checked: {len(paragraphs)}")
    print(f"Exact duplicate pairs: {len(exact)}")
    print(f"Near duplicate pairs: {len(near)}")

    if exact:
        print("\n## Exact duplicates")
        for left, right in exact:
            print(f"- lines {left.start_line}-{left.end_line} ~= {right.start_line}-{right.end_line}")
            print(f"  {preview(left.text)}")

    if near:
        print("\n## Near duplicates")
        for ratio, left, right in near[: args.max_near]:
            print(f"- similarity {ratio:.2f}: lines {left.start_line}-{left.end_line} ~= {right.start_line}-{right.end_line}")
            print(f"  A: {preview(left.text)}")
            print(f"  B: {preview(right.text)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
