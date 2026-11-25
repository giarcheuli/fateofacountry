#!/usr/bin/env python3
"""Generate an unpublished research draft and critique with a local model."""

import argparse
import json
from pathlib import Path
from urllib.request import ProxyHandler, Request, build_opener


ROOT = Path(__file__).resolve().parent
OLLAMA = "http://127.0.0.1:11434/api/generate"


def generate(model, prompt):
    request = Request(
        OLLAMA,
        data=json.dumps({"model": model, "prompt": prompt, "stream": False}).encode(),
        headers={"Content-Type": "application/json"},
    )
    with build_opener(ProxyHandler({})).open(request, timeout=300) as response:
        result = json.load(response)
    if not isinstance(result.get("response"), str) or not result["response"].strip():
        raise ValueError("The local model returned an empty response")
    return result["response"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Name of an installed local Ollama model")
    args = parser.parse_args()
    data = (ROOT / "site" / "data.json").read_text(encoding="utf-8")
    context = (
        "The following are World Bank observations for Georgia (the country). "
        "Use only these observations; their years and definitions differ. "
        "Do not invent sources, imply causation, or claim to have checked external facts.\n"
        + data
    )
    draft = generate(args.model, context + "\nDraft a short research note with limitations.")
    critique = generate(
        args.model,
        context + "\nCritique the following draft for unsupported claims, incorrect numbers, "
        "missing limitations and misleading comparisons. This is not independent fact-checking.\n"
        + draft,
    )
    print("UNREVIEWED DRAFT — DO NOT PUBLISH WITHOUT HUMAN FACT-CHECKING\n")
    print(draft)
    print("\nMODEL CRITIQUE — NOT INDEPENDENT VALIDATION\n")
    print(critique)


if __name__ == "__main__":
    main()
