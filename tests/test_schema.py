import sqlite3
import tempfile
import unittest
from pathlib import Path
from uuid import uuid4

from db.migrate import migrate


class SchemaTest(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.path = Path(directory.name) / "test.sqlite"
        migrate(self.path)
        self.db = sqlite3.connect(self.path)
        self.addCleanup(self.db.close)
        self.db.execute("PRAGMA foreign_keys=ON")
        self.claim, self.source = str(uuid4()), str(uuid4())
        self.db.execute("INSERT INTO claims(id) VALUES(?)", (self.claim,))
        self.db.execute("INSERT INTO sources(id,url,title,content_sha256) VALUES(?,?,?,?)",
                        (self.source, "https://example.org/report", "Test report", "a"*64))

    def draft(self, version, action="publish"):
        self.db.execute("INSERT INTO claim_versions(claim_id,version,action,statement,uncertainty) "
                        "VALUES(?,?,?,'Test finding','Unconfirmed')", (self.claim, version, action))

    def link(self, version):
        self.db.execute("INSERT INTO evidence VALUES(?,?,?,'supporting','paragraph 1')",
                        (self.claim, version, self.source))
        self.db.execute("INSERT INTO claim_categories SELECT ?,?,id FROM categories LIMIT 1",
                        (self.claim, version))

    def approve(self, version):
        self.db.execute("UPDATE claim_versions SET review='approved', reviewer='tester', "
                        "reviewed_at=CURRENT_TIMESTAMP WHERE claim_id=? AND version=?", (self.claim, version))

    def test_upgrade_twice_preserves_records(self):
        self.db.commit()
        migrate(self.path)
        self.assertEqual(7, self.db.execute("SELECT count(*) FROM categories").fetchone()[0])
        self.assertEqual(1, self.db.execute("SELECT count(*) FROM claims").fetchone()[0])
        self.assertEqual([], self.db.execute("PRAGMA foreign_key_check").fetchall())

    def test_publication_lifecycle(self):
        for version, action in enumerate(("publish", "publish", "retract"), 1):
            self.draft(version, action)
            self.link(version)
            self.approve(version)
        self.assertEqual([(1,), (2,), (3,)], self.db.execute(
            "SELECT version FROM publication_outbox ORDER BY version").fetchall())
        for sql in ("DELETE FROM evidence", "DELETE FROM claim_categories",
                    "UPDATE claim_versions SET statement='overwrite'"):
            with self.assertRaises(sqlite3.IntegrityError):
                self.db.execute(sql)

    def test_approval_gates(self):
        self.draft(1, "retract")
        with self.assertRaises(sqlite3.IntegrityError):
            self.approve(1)
        self.link(1)
        with self.assertRaises(sqlite3.IntegrityError):
            self.approve(1)
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO publication_outbox(claim_id,version) VALUES(?,1)", (self.claim,))

    def test_deduplication_and_run_lock(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO sources(id,url,title,content_sha256) "
                            "SELECT ?,url,title,content_sha256 FROM sources", (str(uuid4()),))
        self.db.execute("INSERT INTO research_runs(id,status) VALUES(?,'running')", (str(uuid4()),))
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO research_runs(id,status) VALUES(?,'running')", (str(uuid4()),))
