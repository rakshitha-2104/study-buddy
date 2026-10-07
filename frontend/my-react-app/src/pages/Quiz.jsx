import { useEffect, useState } from "react";
import { api } from "../api";
import { SUBJECT_EMOJI, SUBJECT_NAMES } from "../i18n";

const LEVEL_EMOJI = { easy: "🌱", medium: "🌿", hard: "🌳" };
const CHEERS = ["🎉", "⭐", "💪", "🚀"];

// One question at a time: easy -> medium -> hard. Answers are checked on the server.
export default function Quiz({ lang, t, subject, unit, onDone, onBack }) {
  const [qs, setQs] = useState(null);
  const [warn, setWarn] = useState(false);     // true when translation was not possible
  const [i, setI] = useState(0);
  const [picked, setPicked] = useState({});    // { questionId: optionIndex }
  const [result, setResult] = useState(null);

  useEffect(() => {
    api(`/quiz?subject=${subject}&unit=${unit}&lang=${lang}`)
      .then((r) => { setQs(r.questions); setWarn(lang !== "en" && !r.translated); })
      .catch(() => setQs([]));
  }, [subject, unit, lang]);

  if (!qs) return <div className="card center">⏳ ...</div>;
  if (!qs.length) return <div className="card center">{t.error}<button onClick={onBack}>{t.back}</button></div>;

  const q = qs[i];
  const last = i === qs.length - 1;

  const finish = async () => setResult(await api("/quiz/submit", { subject, unit, answers: picked }));

  // Result screen: show score and which answers were right.
  if (result) {
    return (
      <div className="card center result">
        <div className="mascot">{result.score === result.total ? "🏆" : "🌟"}</div>
        <h2>{t.score}: {result.score} / {result.total}</h2>
        {qs.map((x) => (
          <p key={x.id} className={picked[x.id] === result.key[x.id] ? "right" : "wrong"}>
            {picked[x.id] === result.key[x.id] ? "✅" : "❌"} {x.options[result.key[x.id]]}
          </p>
        ))}
        <button className="primary" onClick={onDone}>📊 {t.dashboard}</button>
      </div>
    );
  }

  return (
    <div className="card quiz">
      <div className="quiz-head">
        <button className="ghost" onClick={onBack}>← {t.back}</button>
        <span className="badge">{SUBJECT_EMOJI[subject]} {SUBJECT_NAMES[subject][lang]} · {t.unit} {unit}</span>
      </div>

      {warn && <p className="warn">⚠️ {t.noTrans}</p>}

      <div className="progress"><div style={{ width: `${((i + 1) / qs.length) * 100}%` }} /></div>
      <span className={"level " + q.level}>{LEVEL_EMOJI[q.level]} {t[q.level]}</span>
      <h2 className="question">✏️ {q.text}</h2>

      {q.options.map((o, idx) => (
        <button key={idx} className={`option opt${idx} ` + (picked[q.id] === idx ? "on" : "")}
                onClick={() => setPicked({ ...picked, [q.id]: idx })}>
          <span className="letter">{"ABCD"[idx]}</span> {o}
        </button>
      ))}

      <button className="primary big" disabled={picked[q.id] === undefined}
              onClick={() => (last ? finish() : setI(i + 1))}>
        {last ? t.finish : t.next} {CHEERS[i % CHEERS.length]}
      </button>
    </div>
  );
}