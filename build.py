#!/usr/bin/env python3
"""Build a static dashboard from World Bank observations."""

import datetime
import html
import json
import math
import os
from pathlib import Path
import tempfile
from urllib.parse import urlparse
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parent
INDICATORS = (
    ("Economy", "GDP per capita", "NY.GDP.PCAP.CD", "current US$"),
    ("Cost of living", "Consumer price inflation", "FP.CPI.TOTL.ZG", "% annual"),
    ("Work", "Unemployment", "SL.UEM.TOTL.ZS", "% of labor force"),
    ("Health", "Life expectancy at birth", "SP.DYN.LE00.IN", "years"),
    ("Education", "Government education expenditure", "SE.XPD.TOTL.GD.ZS", "% of GDP"),
    ("Society", "People using the internet", "IT.NET.USER.ZS", "% of population"),
    ("Environment", "Renewable energy consumption", "EG.FEC.RNEW.ZS", "% of total final energy"),
)


def fetch_indicator(indicator):
    category, label, code, unit = indicator
    url = f"https://api.worldbank.org/v2/country/GEO/indicator/{code}?format=json&per_page=100"
    with urlopen(url, timeout=30) as response:
        payload = json.load(response)
    if not isinstance(payload, list) or len(payload) != 2 or not isinstance(payload[1], list):
        raise ValueError(f"Unexpected World Bank response for {code}")
    observations = []
    for row in payload[1]:
        if not isinstance(row, dict):
            raise ValueError(f"Invalid observation for {code}")
        value, year = row.get("value"), row.get("date")
        if value is None:
            continue
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or not isinstance(year, str)
                or len(year) != 4 or not year.isascii() or not year.isdigit()):
            raise ValueError(f"Invalid observation for {code}")
        observations.append((int(year), value))
    if not observations:
        raise ValueError(f"No observations for {code}")
    year, value = max(observations, key=lambda observation: observation[0])
    return {
        "category": category, "label": label, "code": code, "unit": unit,
        "year": year, "value": value,
        "source": f"https://data.worldbank.org/indicator/{code}?locations=GE",
    }


def load_research(path):
    notes = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(notes, list):
        raise ValueError("Research must be a list")
    for note in notes:
        if not isinstance(note, dict) or any(
            not isinstance(note.get(key), str) or not note[key].strip()
            for key in ("title", "date", "summary")
        ):
            raise ValueError("Each research note needs a title, date and summary")
        try:
            datetime.date.fromisoformat(note["date"])
        except ValueError as exc:
            raise ValueError("Research date must be YYYY-MM-DD") from exc
        if len(note["date"]) != 10:
            raise ValueError("Research date must be YYYY-MM-DD")
        sources = note.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValueError("Each research note needs at least one source")
        for source in sources:
            if not isinstance(source, str):
                raise ValueError("Research sources must be HTTPS URLs")
            parsed = urlparse(source)
            if parsed.scheme != "https" or not parsed.hostname or any(c.isspace() for c in source):
                raise ValueError("Research sources must be HTTPS URLs")
    return notes


def render(observations, notes, updated):
    esc = lambda value: html.escape(str(value), quote=True)
    cards = "".join(
        f'<article><p class="category">{esc(row["category"])}</p>'
        f'<h3>{esc(row["label"])}</h3><p class="value">{row["value"]:,.2f}</p>'
        f'<p>{esc(row["unit"])} · {esc(row["year"])}</p>'
        f'<a href="{esc(row["source"])}">World Bank source and definition</a></article>'
        for row in observations
    )
    research = "".join(
        f'<article><h3>{esc(note["title"])}</h3><p>{esc(note["date"])}</p>'
        f'<p>{esc(note["summary"])}</p><p>Sources: '
        + " · ".join(f'<a href="{esc(url)}">Source {i}</a>'
                     for i, url in enumerate(note["sources"], 1))
        + "</p></article>"
        for note in notes
    ) or "<p>No reviewed research has been published yet.</p>"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fate of a Country · Georgia</title>
<style>
body{{font:16px/1.6 system-ui,sans-serif;background:#f5f4ef;color:#202b29;margin:0}}
main{{max-width:1100px;margin:auto;padding:2rem 1.25rem 4rem}}
h1{{font-size:clamp(2.2rem,6vw,4rem);line-height:1.1;margin:.3rem 0}}
h2{{margin-top:2.5rem}} a{{color:#165b52}} .intro{{max-width:70ch}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1rem}}
article{{background:white;border:1px solid #d5ded9;border-radius:8px;padding:1.2rem}}
article h3{{margin:.25rem 0}} article p{{margin:.4rem 0}} .category{{color:#41655c}}
.value{{font-size:2rem;font-weight:700}} footer{{margin-top:3rem}}
</style></head><body><main>
<header><p>COMMUNITY-LED · OPEN SOURCE · NON-COMMERCIAL</p>
<h1>Fate of a Country</h1><p class="intro">A starting point for following life in Georgia,
the country, through public data and independently reviewed research.</p></header>
<section><h2>Indicators</h2><p>Latest available World Bank observations, retrieved
{esc(updated)}. Years and definitions vary; figures are not necessarily current.
Follow the source links for methodology and limitations.</p><div class="grid">{cards}</div></section>
<section><h2>Reviewed research</h2>{research}</section>
<section><h2>What is missing?</h2><p>This initial dashboard does not yet measure politics,
democracy, human rights, freedom, science, or every aspect of Georgian life.
Numbers alone cannot tell the whole story. Contributions of reliable sources and
independently checked research are welcome.</p></section>
<footer><a href="https://github.com/giarcheuli/fateofacountry">Contribute on GitHub</a></footer>
</main></body></html>"""


def main():
    observations = [fetch_indicator(indicator) for indicator in INDICATORS]
    notes = load_research(ROOT / "research.json")
    updated = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    output = ROOT / "site"
    output.mkdir(exist_ok=True)
    for name, content in (
        ("data.json", json.dumps(observations, ensure_ascii=False, indent=2) + "\n"),
        ("index.html", render(observations, notes, updated)),
    ):
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=output, delete=False) as file:
            try:
                file.write(content)
                file.flush()
                os.replace(file.name, output / name)
            finally:
                if os.path.exists(file.name):
                    os.unlink(file.name)


if __name__ == "__main__":
    main()
