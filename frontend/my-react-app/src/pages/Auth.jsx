import { useState } from "react";
import { api } from "../api";
import { LANGUAGES } from "../i18n";

// Page 1: choose language first, then log in or register in that language.
export default function Auth({ lang, setLang, t, onAuth }) {
  const [form, setForm] = useState({ name: "", student_id: "", password: "" });
  const [error, setError] = useState("");
  const set = (k) => (e) => setForm({ ...form, [k]: e.target.value });

  const submit = async (mode) => {
    setError("");
    try {
      onAuth(await api("/" + mode, { ...form, language: lang }));
    } catch {
      setError(t.error);
    }
  };

  return (
    <div className="auth">
      <div className="card auth-card">
        <div className="mascot">🎓</div>
        <h1>{t.welcome}</h1>

        <div className="lang-row">
          {LANGUAGES.map((l) => (
            <button key={l.code} className={"chip " + (lang === l.code ? "on" : "")} onClick={() => setLang(l.code)}>
              {l.label}
            </button>
          ))}
        </div>

        <input placeholder={"🙂 " + t.name} value={form.name} onChange={set("name")} />
        <input placeholder={"🆔 " + t.id} value={form.student_id} onChange={set("student_id")} />
        <input type="password" placeholder={"🔑 " + t.password} value={form.password} onChange={set("password")} />
        {error && <p className="err">⚠️ {error}</p>}

        <div className="row">
          <button className="primary" onClick={() => submit("login")}>{t.login}</button>
          <button className="secondary" onClick={() => submit("register")}>{t.register}</button>
        </div>
      </div>
    </div>
  );
}