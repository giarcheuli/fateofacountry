# Fate of a Country

A non-commercial, community-maintained, open-source project to make indicators
about Georgia (the country) easier to follow. This is an early prototype, not a
newsroom or a complete picture of life in Georgia.

The dashboard fetches the latest available observations from the World Bank
when it is built, and links each indicator to its source. Years differ because
indicators are published at different times; the latest value is not necessarily
current. The initial selection covers the economy, work, health, education,
connectivity and the environment. It does **not** yet cover politics, democracy,
human rights, freedom, science or many other important aspects of life. Help
finding reliable, openly accessible sources for those gaps is welcome.

## Run and publish

Python 3.9 or newer is the only required software; there are no Python
dependencies. An internet connection to `api.worldbank.org` is required.

```sh
python3 build.py
python3 -m http.server --directory site 8000
```

Open <http://localhost:8000>. The build fails rather than publishing a partial
or fabricated update if a source cannot be reached or returns invalid data.
`site/data.json` contains the observations used in the build. Run
`python3 -m unittest discover -s tests` for the offline tests.

To publish without a proprietary hosting dependency, serve the generated `site/`
directory with an open-source web server such as nginx or Caddy, and schedule
`python3 build.py` with cron or a systemd timer. Build in a staging directory
and replace the served directory only after a successful build. Codeberg Pages
is another static-hosting option. GitHub Pages is also supported by the included
workflow, although GitHub is a proprietary hosted service: enable Pages with
**GitHub Actions** as the source in repository settings. The workflow rebuilds
weekly and can also be started manually. It publishes only after a successful
build. Review GitHub's service terms before choosing a host.

## Research and review

Volunteers can use `research.py` with a locally running
[Ollama](https://github.com/ollama/ollama) server and an open-source-licensed model to
produce a draft and a separate model critique from a built `site/data.json`:

```sh
python3 research.py --model YOUR_LOCAL_MODEL > draft.txt
```

This is optional; the dashboard needs no model, subscription, API key, or
personal data. A model critique is **not fact-checking**. Models can invent
claims, citations and context, and public indicators alone cannot establish
causation. A human must independently check every claim against the original
sources, check the year and definitions, document limitations, and approve
publication. Never publish a model draft automatically or submit private
information to a model. A volunteer may run the command on a regular schedule;
drafts remain local until reviewed.

To publish a reviewed note, add an entry to `research.json` with `title`,
`date` (YYYY-MM-DD), `summary`, and `sources` (a list of HTTPS URLs). The
dashboard displays those entries separately from the indicators. Only commit
notes that have been independently reviewed; include primary source links and
correct or remove notes if evidence changes. No example note is presented as
real research.

## Contributing

Issues and pull requests are welcome. Propose indicators with a stable source,
definition, unit, update frequency and limitations; do not treat a numerical
proxy as proof of rights or democratic conditions. Review source licensing
before adding data or text. Keep the project non-commercial, disclose conflicts
of interest, respect privacy, and verify research independently of AI tools.
Code is available under the MIT license; third-party data remains subject to its
own terms.
