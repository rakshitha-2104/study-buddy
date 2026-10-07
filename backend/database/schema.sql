-- StudyBuddy database (SQLite). Run automatically by app.py on first start.

-- One row per student. Passwords are stored as hashes, never as plain text.
CREATE TABLE IF NOT EXISTS users (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id    TEXT UNIQUE NOT NULL,
  name          TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  language      TEXT NOT NULL DEFAULT 'en',      -- en, kn, te, hi, ml, ta
  created_at    TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS subjects (
  id   TEXT PRIMARY KEY,                          -- e.g. 'python'
  name TEXT NOT NULL
);

-- Question bank: 4 units per subject, 3 levels per unit.
CREATE TABLE IF NOT EXISTS questions (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  subject_id TEXT NOT NULL REFERENCES subjects(id),
  unit       INTEGER NOT NULL CHECK (unit BETWEEN 1 AND 4),
  level      TEXT NOT NULL CHECK (level IN ('easy','medium','hard')),
  text       TEXT NOT NULL,
  options    TEXT NOT NULL,                       -- JSON array of 4 strings
  answer     INTEGER NOT NULL                     -- index of the correct option
);

-- One row per quiz taken (feeds the dashboard graph).
CREATE TABLE IF NOT EXISTS attempts (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id    INTEGER NOT NULL REFERENCES users(id),
  subject_id TEXT NOT NULL REFERENCES subjects(id),
  unit       INTEGER NOT NULL,
  score      INTEGER NOT NULL,
  total      INTEGER NOT NULL,
  taken_at   TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Per-question result, used to find learning gaps by unit.
CREATE TABLE IF NOT EXISTS attempt_answers (
  attempt_id  INTEGER NOT NULL REFERENCES attempts(id),
  question_id INTEGER NOT NULL REFERENCES questions(id),
  correct     INTEGER NOT NULL                    -- 1 or 0
);

-- Saved translations (questions, options, bot answers) so each text is
-- translated only once per language. h = md5 of the English text.
CREATE TABLE IF NOT EXISTS text_cache (
  h    TEXT NOT NULL,
  lang TEXT NOT NULL,
  text TEXT NOT NULL,
  PRIMARY KEY (h, lang)
);