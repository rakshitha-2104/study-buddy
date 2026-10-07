"""StudyBuddy backend: Flask + SQLite. No API key needed.

Run:  pip install -r requirements.txt
      python app.py
"""
import hashlib, json, os, re, sqlite3
from functools import wraps

from deep_translator import GoogleTranslator   # free translation, needs internet, no key
from flask import Flask, g, jsonify, request
from flask_cors import CORS
from itsdangerous import BadSignature, URLSafeTimedSerializer
from werkzeug.security import check_password_hash, generate_password_hash

from database.seed import seed
from knowledge import KB

app = Flask(__name__)
CORS(app)
BASE = os.path.dirname(os.path.abspath(__file__))
tokens = URLSafeTimedSerializer(os.environ.get("SECRET_KEY", "change-me-in-production"))
DB_PATH = os.path.join(BASE, "database", "studybuddy.db")
SCHEMA_PATH = os.path.join(BASE, "database", "schema.sql")
LANGS = {"en": "English", "kn": "Kannada", "te": "Telugu",
         "hi": "Hindi", "ml": "Malayalam", "ta": "Tamil"}

# ---------- Database helpers ----------
def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(_):
    conn = g.pop("db", None)
    if conn:
        conn.close()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        conn.executescript(f.read())
    seed(conn)
    conn.close()

# ---------- Auth ----------
def login_required(fn):
    """Reads 'Authorization: Bearer <token>' and puts the user id in g.uid."""
    @wraps(fn)
    def wrapper(*a, **kw):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        try:
            g.uid = tokens.loads(token, max_age=60 * 60 * 24 * 7)["uid"]
        except (BadSignature, KeyError):
            return jsonify(error="auth"), 401
        return fn(*a, **kw)
    return wrapper

def auth_reply(row):
    return jsonify(token=tokens.dumps({"uid": row["id"]}),
                   user={"name": row["name"], "student_id": row["student_id"],
                         "language": row["language"]})

@app.post("/api/register")
def register():
    d = request.json or {}
    name, sid, pw = d.get("name", "").strip(), d.get("student_id", "").strip(), d.get("password", "")
    lang = d.get("language") if d.get("language") in LANGS else "en"
    if not (name and sid and len(pw) >= 6):
        return jsonify(error="invalid"), 400
    try:
        db().execute("INSERT INTO users (student_id, name, password_hash, language) VALUES (?,?,?,?)",
                     (sid, name, generate_password_hash(pw), lang))
        db().commit()
    except sqlite3.IntegrityError:
        return jsonify(error="exists"), 409
    row = db().execute("SELECT * FROM users WHERE student_id=?", (sid,)).fetchone()
    return auth_reply(row)

@app.post("/api/login")
def login():
    d = request.json or {}
    row = db().execute("SELECT * FROM users WHERE student_id=?", (d.get("student_id", ""),)).fetchone()
    if not row or not check_password_hash(row["password_hash"], d.get("password", "")):
        return jsonify(error="credentials"), 401
    if d.get("language") in LANGS:       # remember the language chosen on the first page
        db().execute("UPDATE users SET language=? WHERE id=?", (d["language"], row["id"]))
        db().commit()
    return auth_reply(row)

# ---------- Translation (free, cached) ----------
def should_translate(s):
    """Keep code-like or one-word options (TCP, __init__, CSMA/CD) as they are."""
    return len(s.split()) >= 2 and not re.search(r"[(){}\[\]_=<>;/]", s)

def translate_many(strings, lang):
    """Translate English strings to `lang`.
    Returns (translated_list, ok). ok is False if anything could not be translated.
    Saved translations are used first; new ones are saved for next time."""
    if lang == "en" or lang not in LANGS:
        return strings, True
    h = lambda s: hashlib.md5(s.encode("utf-8")).hexdigest()
    done, todo = {}, []
    for s in strings:
        row = db().execute("SELECT text FROM text_cache WHERE h=? AND lang=?", (h(s), lang)).fetchone()
        if row:
            done[s] = row["text"]
        elif s not in todo:
            todo.append(s)

    ok = True
    if todo:
        translator = GoogleTranslator(source="en", target=lang)
        for s in todo:                       # one by one, so one failure does not break the rest
            try:
                result = translator.translate(s)
            except Exception as e:
                print("TRANSLATION ERROR:", repr(e))   # shows the real reason in your terminal
                result = None
            if result and result.strip():
                done[s] = result
                db().execute("INSERT OR REPLACE INTO text_cache VALUES (?,?,?)", (h(s), lang, result))
            else:
                done[s] = s                  # fall back to English for this one string
                ok = False
        db().commit()
    return [done[s] for s in strings], ok

def to_english(text):
    """Student may type in Kannada, Telugu, etc. Convert to English for matching."""
    try:
        return GoogleTranslator(source="auto", target="en").translate(text) or text
    except Exception:
        return text

# ---------- Subjects & quiz ----------
@app.get("/api/subjects")
def subjects():
    return jsonify([dict(r) for r in db().execute("SELECT * FROM subjects")])

@app.get("/api/quiz")
@login_required
def quiz():
    subject, unit = request.args["subject"], int(request.args["unit"])
    lang = request.args.get("lang", "en")
    rows = db().execute(
        "SELECT * FROM questions WHERE subject_id=? AND unit=? "
        "ORDER BY CASE level WHEN 'easy' THEN 1 WHEN 'medium' THEN 2 ELSE 3 END", (subject, unit)).fetchall()
    strings = []
    for q in rows:
        strings.append(q["text"])
        strings += [o for o in json.loads(q["options"]) if should_translate(o)]
    translated, ok = translate_many(strings, lang)
    tr = dict(zip(strings, translated))
    return jsonify(translated=ok, questions=[{       # beginning -> middle -> difficult
        "id": q["id"], "level": q["level"], "text": tr[q["text"]],
        "options": [tr.get(o, o) for o in json.loads(q["options"])],
    } for q in rows])

@app.post("/api/quiz/submit")
@login_required
def submit():
    d = request.json
    answers = {int(k): v for k, v in d["answers"].items()}
    if not answers:
        return jsonify(error="empty"), 400
    qs = db().execute(f"SELECT id, answer FROM questions WHERE id IN ({','.join('?' * len(answers))})",
                      list(answers)).fetchall()
    correct = {q["id"]: int(answers[q["id"]] == q["answer"]) for q in qs}
    score = sum(correct.values())
    cur = db().execute("INSERT INTO attempts (user_id, subject_id, unit, score, total) VALUES (?,?,?,?,?)",
                       (g.uid, d["subject"], d["unit"], score, len(qs)))
    db().executemany("INSERT INTO attempt_answers VALUES (?,?,?)",
                     [(cur.lastrowid, qid, c) for qid, c in correct.items()])
    db().commit()
    # The right answers are sent back only AFTER submitting.
    return jsonify(score=score, total=len(qs), key={q["id"]: q["answer"] for q in qs})

# ---------- Learning gaps & dashboard ----------
def rating(pct):
    return "excellent" if pct >= 80 else "good" if pct >= 60 else "practice"

def weak_units(uid):
    """Simple rule: a unit is a 'gap' if the student's accuracy there is below 60%."""
    rows = db().execute(
        "SELECT a.subject_id, a.unit, AVG(aa.correct) AS acc FROM attempts a "
        "JOIN attempt_answers aa ON aa.attempt_id=a.id WHERE a.user_id=? "
        "GROUP BY a.subject_id, a.unit HAVING acc < 0.6 ORDER BY acc", (uid,)).fetchall()
    return [{"subject": r["subject_id"], "unit": r["unit"], "accuracy": round(r["acc"] * 100)} for r in rows]

@app.get("/api/dashboard")
@login_required
def dashboard():
    att = db().execute("SELECT subject_id, unit, score, total FROM attempts "
                       "WHERE user_id=? ORDER BY id", (g.uid,)).fetchall()
    history = [{"n": i + 1, "label": f"{a['subject_id'].upper()} U{a['unit']}",
                "percent": round(100 * a["score"] / a["total"])} for i, a in enumerate(att)]
    by_subject = db().execute(
        "SELECT subject_id, ROUND(100.0*SUM(score)/SUM(total)) AS percent FROM attempts "
        "WHERE user_id=? GROUP BY subject_id", (g.uid,)).fetchall()
    overall = round(sum(h["percent"] for h in history) / len(history)) if history else 0
    return jsonify(history=history, by_subject=[dict(r) for r in by_subject],
                   overall=overall, rating=rating(overall), weak=weak_units(g.uid))

# ---------- Built-in tutor bot (no AI key) ----------
def find_answer(question_en, subject):
    """Pick the KB entry whose keywords appear in the question (longer keyword = better match)."""
    q = question_en.lower()
    best, best_score = None, 0
    for entry in KB:
        if subject and entry[0] != subject:
            continue
        score = sum(len(k) for k in entry[2] if re.search(r"\b" + re.escape(k) + r"\b", q))
        if score > best_score:
            best, best_score = entry, score
    return best

@app.post("/api/chat")
@login_required
def chat():
    d = request.json
    lang, subject = d.get("language", "en"), d.get("subject")
    question = d["message"][:500]
    question_en = question if lang == "en" else to_english(question)

    # Look in the selected subject first, then in all subjects.
    hit = find_answer(question_en, subject) or find_answer(question_en, None)
    if not hit:
        topics = [e[2][0] for e in KB if not subject or e[0] == subject][:6]
        return jsonify(found=False, topics=topics)

    sub, unit, _, explanation, example = hit
    text = translate_many([explanation], lang)[0][0]
    if example:
        text += "\n\n" + example          # code stays in English, exactly as written
    gap = any(w["subject"] == sub and w["unit"] == unit for w in weak_units(g.uid))
    return jsonify(found=True, reply=text, subject=sub, unit=unit, revise=gap)

if __name__ == "__main__":
    init_db()
    app.run(port=5000, debug=True)