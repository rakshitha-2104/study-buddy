import { useEffect, useRef, useState } from "react";
import { api } from "../api";
import { SUBJECT_EMOJI, SUBJECT_NAMES } from "../i18n";

// Page 2: left half = Study Buddy bot, right half = subjects with Unit 1-4 buttons.
export default function Home({ lang, t, onStart }) {
  const [subjects, setSubjects] = useState([]);
  const [open, setOpen] = useState(null);           // subject id whose units are shown
  const [msgs, setMsgs] = useState([{ from: "bot", text: "🤖 " + t.greet }]);
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  const endRef = useRef();

  useEffect(() => { api("/subjects").then(setSubjects).catch(() => {}); }, []);
  useEffect(() => { endRef.current?.scrollIntoView({ behavior: "smooth" }); }, [msgs]);

  const send = async () => {
    if (!text.trim() || busy) return;
    const message = text;
    setText(""); setBusy(true);
    setMsgs((m) => [...m, { from: "me", text: message }]);
    try {
      const r = await api("/chat", { message, language: lang, subject: open });
      const reply = r.found
        // Found: explanation, plus a gentle reminder if this unit was weak in earlier quizzes
        ? r.reply + (r.revise ? `\n\n📌 ${t.unit} ${r.unit}: ${t.revise}` : "")
        // Not found: show topics the bot can explain
        : `${t.notFound}\n${r.topics.map((x) => "• " + x).join("\n")}`;
      setMsgs((m) => [...m, { from: "bot", text: reply }]);
    } catch {
      setMsgs((m) => [...m, { from: "bot", text: t.error }]);
    }
    setBusy(false);
  };

  return (
    <div className="split">
      {/* Left half: Study Buddy bot */}
      <section className="card chat">
        <h2>🤖 {t.askAi}</h2>
        <div className="msgs">
          {msgs.map((m, i) => <div key={i} className={"bubble " + m.from}>{m.text}</div>)}
          {busy && <div className="bubble bot">💭 ...</div>}
          <div ref={endRef} />
        </div>
        <div className="row">
          <input value={text} placeholder={t.typeQ} onChange={(e) => setText(e.target.value)}
                 onKeyDown={(e) => e.key === "Enter" && send()} />
          <button className="primary" onClick={send}>{t.send} ✈️</button>
        </div>
      </section>

      {/* Right half: subjects column */}
      <section className="card subjects">
        <h2>📖 {t.subjects}</h2>
        {subjects.map((s) => (
          <div key={s.id} className={"subject s-" + s.id}>
            <button className={"subject-btn " + (open === s.id ? "on" : "")} onClick={() => setOpen(open === s.id ? null : s.id)}>
              <span>{SUBJECT_EMOJI[s.id]}</span> {SUBJECT_NAMES[s.id][lang]}
            </button>
            {open === s.id && (
              <div className="units">
                {[1, 2, 3, 4].map((u) => (
                  <button key={u} className="chip" onClick={() => onStart(s.id, u)}>
                    ✏️ {t.unit} {u}
                  </button>
                ))}
              </div>
            )}
          </div>
        ))}
      </section>
    </div>
  );
}