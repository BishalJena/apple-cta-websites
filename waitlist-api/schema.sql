-- One table holds all seven waitlists. (email, app) is unique so a person
-- can join several apps' waitlists, but only once per app.
CREATE TABLE IF NOT EXISTS waitlist (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  email      TEXT    NOT NULL,
  app        TEXT    NOT NULL,
  source     TEXT,
  created_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
  UNIQUE (email, app)
);

CREATE INDEX IF NOT EXISTS waitlist_app_created ON waitlist (app, created_at);
