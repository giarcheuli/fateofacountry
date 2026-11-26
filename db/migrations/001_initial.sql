CREATE TABLE categories (
    id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL UNIQUE
);
CREATE TABLE sources (
    id TEXT PRIMARY KEY NOT NULL,
    url TEXT NOT NULL,
    title TEXT NOT NULL,
    publisher TEXT,
    author TEXT,
    published_at TEXT,
    retrieved_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    content_sha256 TEXT NOT NULL CHECK(length(content_sha256)=64 AND content_sha256 NOT GLOB '*[^0-9a-f]*'),
    UNIQUE(url, content_sha256)
);
CREATE TABLE claims (
    id TEXT PRIMARY KEY NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE claim_versions (
    claim_id TEXT NOT NULL REFERENCES claims,
    version INTEGER NOT NULL CHECK(typeof(version)='integer' AND version>=1),
    action TEXT NOT NULL CHECK(action IN ('publish','retract')),
    statement TEXT NOT NULL CHECK(length(trim(statement))>0),
    uncertainty TEXT NOT NULL,
    entities TEXT NOT NULL DEFAULT '[]' CHECK(json_type(entities)='array'),
    events TEXT NOT NULL DEFAULT '[]' CHECK(json_type(events)='array'),
    review TEXT NOT NULL DEFAULT 'pending' CHECK(review IN ('pending','approved','rejected')),
    reviewer TEXT,
    reviewed_at TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(claim_id, version),
    CHECK((review='pending' AND reviewer IS NULL AND reviewed_at IS NULL)
       OR (review<>'pending' AND length(trim(coalesce(reviewer,'')))>0 AND reviewed_at IS NOT NULL))
);
CREATE TABLE evidence (
    claim_id TEXT NOT NULL,
    version INTEGER NOT NULL,
    source_id TEXT NOT NULL REFERENCES sources,
    stance TEXT NOT NULL CHECK(stance IN ('supporting','contradicting')),
    locator TEXT NOT NULL,
    PRIMARY KEY(claim_id, version, source_id, stance, locator),
    FOREIGN KEY(claim_id,version) REFERENCES claim_versions
);
CREATE TABLE claim_categories (
    claim_id TEXT NOT NULL,
    version INTEGER NOT NULL,
    category_id TEXT NOT NULL REFERENCES categories,
    PRIMARY KEY(claim_id,version,category_id),
    FOREIGN KEY(claim_id,version) REFERENCES claim_versions
);
CREATE TABLE publication_outbox (
    claim_id TEXT NOT NULL,
    version INTEGER NOT NULL,
    attempts INTEGER NOT NULL DEFAULT 0 CHECK(attempts>=0),
    next_attempt_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    delivered_at TEXT,
    PRIMARY KEY(claim_id,version),
    FOREIGN KEY(claim_id,version) REFERENCES claim_versions
);
CREATE INDEX outbox_due ON publication_outbox(next_attempt_at) WHERE delivered_at IS NULL;
CREATE INDEX evidence_source ON evidence(source_id);
CREATE INDEX categories_lookup ON claim_categories(category_id);
CREATE TABLE research_runs (
    id TEXT PRIMARY KEY NOT NULL,
    started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TEXT,
    status TEXT NOT NULL CHECK(status IN ('running','succeeded','failed')),
    details TEXT,
    CHECK((status='running')=(finished_at IS NULL))
);
CREATE UNIQUE INDEX single_running_worker ON research_runs(status) WHERE status='running';
CREATE TRIGGER new_version BEFORE INSERT ON claim_versions
WHEN NEW.review<>'pending' OR NEW.version<>coalesce(
    (SELECT max(version)+1 FROM claim_versions WHERE claim_id=NEW.claim_id),1)
BEGIN SELECT raise(ABORT,'insert the next pending version'); END;
CREATE TRIGGER preserve_version BEFORE UPDATE ON claim_versions
WHEN OLD.review<>'pending' OR NEW.claim_id<>OLD.claim_id OR NEW.version<>OLD.version
BEGIN SELECT raise(ABORT,'create a new version'); END;
CREATE TRIGGER require_evidence BEFORE UPDATE OF review ON claim_versions
WHEN NEW.review='approved' AND (
    NOT EXISTS(SELECT 1 FROM evidence WHERE claim_id=NEW.claim_id AND version=NEW.version)
    OR NOT EXISTS(SELECT 1 FROM claim_categories WHERE claim_id=NEW.claim_id AND version=NEW.version)
    OR EXISTS(SELECT 1 FROM publication_outbox WHERE claim_id=NEW.claim_id AND version>=NEW.version)
    OR (NEW.action='retract' AND NOT EXISTS(SELECT 1 FROM publication_outbox WHERE claim_id=NEW.claim_id)))
BEGIN SELECT raise(ABORT,'approval requires evidence, category and valid publication order'); END;
CREATE TRIGGER enqueue_approval AFTER UPDATE OF review ON claim_versions WHEN NEW.review='approved'
BEGIN INSERT INTO publication_outbox(claim_id,version) VALUES(NEW.claim_id,NEW.version); END;
CREATE TRIGGER approved_only BEFORE INSERT ON publication_outbox
WHEN (SELECT review FROM claim_versions WHERE claim_id=NEW.claim_id AND version=NEW.version)<>'approved'
BEGIN SELECT raise(ABORT,'approval required'); END;
CREATE TRIGGER immutable_source BEFORE UPDATE ON sources
BEGIN SELECT raise(ABORT,'insert a new source snapshot'); END;
CREATE TRIGGER guard_evidence_insert BEFORE INSERT ON evidence
WHEN (SELECT review FROM claim_versions WHERE claim_id=NEW.claim_id AND version=NEW.version)<>'pending'
BEGIN SELECT raise(ABORT,'reviewed links are immutable'); END;
CREATE TRIGGER guard_evidence_update BEFORE UPDATE ON evidence
WHEN (SELECT review FROM claim_versions WHERE claim_id=NEW.claim_id AND version=NEW.version)<>'pending' OR (SELECT review FROM claim_versions WHERE claim_id=OLD.claim_id AND version=OLD.version)<>'pending'
BEGIN SELECT raise(ABORT,'reviewed links are immutable'); END;
CREATE TRIGGER guard_evidence_delete BEFORE DELETE ON evidence
WHEN (SELECT review FROM claim_versions WHERE claim_id=OLD.claim_id AND version=OLD.version)<>'pending'
BEGIN SELECT raise(ABORT,'reviewed links are immutable'); END;
CREATE TRIGGER guard_claim_categories_insert BEFORE INSERT ON claim_categories
WHEN (SELECT review FROM claim_versions WHERE claim_id=NEW.claim_id AND version=NEW.version)<>'pending'
BEGIN SELECT raise(ABORT,'reviewed links are immutable'); END;
CREATE TRIGGER guard_claim_categories_update BEFORE UPDATE ON claim_categories
WHEN (SELECT review FROM claim_versions WHERE claim_id=NEW.claim_id AND version=NEW.version)<>'pending' OR (SELECT review FROM claim_versions WHERE claim_id=OLD.claim_id AND version=OLD.version)<>'pending'
BEGIN SELECT raise(ABORT,'reviewed links are immutable'); END;
CREATE TRIGGER guard_claim_categories_delete BEFORE DELETE ON claim_categories
WHEN (SELECT review FROM claim_versions WHERE claim_id=OLD.claim_id AND version=OLD.version)<>'pending'
BEGIN SELECT raise(ABORT,'reviewed links are immutable'); END;
INSERT INTO categories VALUES('e651c861-e481-56e2-aa4e-abc413c1eb66','Internal politics');
INSERT INTO categories VALUES('1aeb98c2-b733-5067-8fc0-c6d2b1d62f37','Foreign politics');
INSERT INTO categories VALUES('c64545e6-8d4e-5b58-9df7-e4c08e20176a','Economics');
INSERT INTO categories VALUES('decac0db-3d78-5a2d-9c7e-951416c6e8ad','Social and public life');
INSERT INTO categories VALUES('9f1565a0-7264-5251-9c94-820609022a26','Human rights');
INSERT INTO categories VALUES('0ae15eb3-5330-5f68-bbf2-301b799b6554','Science and arts');
INSERT INTO categories VALUES('91221d4a-e2dd-53ff-b799-40829ee2a75c','Infrastructure');
