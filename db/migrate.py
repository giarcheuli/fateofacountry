"""Apply numbered SQLite migrations. Run: python db/migrate.py country.sqlite"""
import sqlite3
import sys
from pathlib import Path

MIGRATIONS = Path(__file__).with_name("migrations")


def migrate(database):
    connection = sqlite3.connect(database, timeout=30)
    try:
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("BEGIN IMMEDIATE")
        version = connection.execute("PRAGMA user_version").fetchone()[0]
        files = sorted(MIGRATIONS.glob("*.sql"))
        if version > len(files):
            raise ValueError("Database schema is newer than this worker")
        for number, path in enumerate(files, 1):
            if int(path.stem.split("_")[0]) != number:
                raise ValueError(f"Unexpected migration sequence at {path}")
            if number <= version:
                continue
            statement = ""
            for line in path.read_text().splitlines(keepends=True):
                statement += line
                if sqlite3.complete_statement(statement):
                    connection.execute(statement)
                    statement = ""
            if statement.strip():
                raise ValueError(f"Incomplete SQL in {path}")
            connection.execute(f"PRAGMA user_version={number}")
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    migrate(sys.argv[1])
