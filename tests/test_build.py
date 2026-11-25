import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build
import research


class IndicatorTests(unittest.TestCase):
    def test_selects_latest_nonempty_observation_not_response_order(self):
        response = [{}, [
            {"date": "2021", "value": 2},
            {"date": "2023", "value": None},
            {"date": "2022", "value": 3.5},
        ]]
        with patch("build.urlopen", return_value=io.BytesIO(json.dumps(response).encode())):
            result = build.fetch_indicator(build.INDICATORS[0])
        self.assertEqual((result["year"], result["value"]), (2022, 3.5))
        self.assertIn("locations=GE", result["source"])

    def test_rejects_bad_or_missing_observations(self):
        for observations in (None, [], [{"date": "2022", "value": True}]):
            with self.subTest(observations=observations):
                payload = json.dumps([{}, observations]).encode()
                with patch("build.urlopen", return_value=io.BytesIO(payload)):
                    with self.assertRaises(ValueError):
                        build.fetch_indicator(build.INDICATORS[0])

    def test_render_escapes_research_and_shows_empty_state(self):
        note = {"title": "<script>", "date": "2025-01-01",
                "summary": "<b>claim</b>", "sources": ["https://example.org/?a=1&b=2"]}
        output = build.render([], [note], "today")
        self.assertIn("&lt;script&gt;", output)
        self.assertNotIn("<script>", output)
        self.assertIn("a=1&amp;b=2", output)
        self.assertIn("No reviewed research", build.render([], [], "today"))

    def test_failed_refresh_leaves_existing_site_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "site").mkdir()
            (root / "site" / "index.html").write_text("previous")
            (root / "site" / "data.json").write_text("previous data")
            with patch.object(build, "ROOT", root), \
                    patch("build.fetch_indicator", side_effect=OSError("source unavailable")):
                with self.assertRaises(OSError):
                    build.main()
            self.assertEqual((root / "site" / "index.html").read_text(), "previous")
            self.assertEqual((root / "site" / "data.json").read_text(), "previous data")

    def test_research_requires_valid_source_and_date(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "research.json"
            note = {"title": "Title", "date": "2025-01-01", "summary": "Summary",
                    "sources": ["https://example.org"]}
            path.write_text(json.dumps([note]))
            self.assertEqual(build.load_research(path), [note])
            for key, value in (("sources", ["javascript:alert(1)"]), ("date", "2025-02-30")):
                invalid = dict(note, **{key: value})
                path.write_text(json.dumps([invalid]))
                with self.assertRaises(ValueError):
                    build.load_research(path)

    def test_research_draft_is_critiqued_but_not_published(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "site").mkdir()
            (root / "site" / "data.json").write_text("[]")
            with patch.object(research, "ROOT", root), \
                    patch("research.generate", side_effect=["draft", "critique"]) as generate, \
                    patch("sys.argv", ["research.py", "--model", "local"]), \
                    patch("sys.stdout", new_callable=io.StringIO) as stdout:
                research.main()
            self.assertEqual(generate.call_count, 2)
            self.assertIn("draft", generate.call_args_list[1].args[1])
            self.assertIn("NOT INDEPENDENT VALIDATION", stdout.getvalue())
            self.assertFalse((root / "research.json").exists())


if __name__ == "__main__":
    unittest.main()
