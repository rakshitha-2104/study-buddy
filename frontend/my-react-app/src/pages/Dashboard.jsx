import { useEffect, useState } from "react";
import { Bar, BarChart, CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { api } from "../api";
import { SUBJECT_EMOJI, SUBJECT_NAMES } from "../i18n";

const RATING_EMOJI = { excellent: "🏆", good: "😊", practice: "💪" };

// Page 3: graph built from the student's own quiz results + a friendly rating.
export default function Dashboard({ lang, t, onBack }) {
  const [d, setD] = useState(null);
  useEffect(() => { api("/dashboard").then(setD).catch(() => setD({ history: [] })); }, []);

  if (!d) return <div className="card center">⏳ ...</div>;
  if (!d.history.length) return <div className="card center"><p>📝 {t.noData}</p><button onClick={onBack}>← {t.back}</button></div>;

  const bars = d.by_subject.map((s) => ({ ...s, name: SUBJECT_EMOJI[s.subject_id] + " " + SUBJECT_NAMES[s.subject_id][lang] }));

  return (
    <div className="dash">
      <button className="ghost" onClick={onBack}>← {t.back}</button>

      <div className="card center">
        <div className="mascot">{RATING_EMOJI[d.rating]}</div>
        <h2>{d.overall}%</h2>
        <p>{t[d.rating]}</p>
      </div>

      <div className="card">
        <h3>📈 {t.dashboard}</h3>
        <ResponsiveContainer width="100%" height={240}>
          <LineChart data={d.history}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="label" fontSize={11} />
            <YAxis domain={[0, 100]} unit="%" />
            <Tooltip />
            <Line type="monotone" dataKey="percent" stroke="#7c5cff" strokeWidth={3} dot={{ r: 5 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="card">
        <h3>🎯 {t.subjects}</h3>
        <ResponsiveContainer width="100%" height={240}>
          <BarChart data={bars}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" fontSize={11} />
            <YAxis domain={[0, 100]} unit="%" />
            <Tooltip />
            <Bar dataKey="percent" fill="#ff8fab" radius={[8, 8, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {d.weak.length > 0 && (
        <div className="card">
          <h3>🌱 {t.gaps}</h3>
          {d.weak.map((w, i) => (
            <span key={i} className="chip">{SUBJECT_EMOJI[w.subject]} {SUBJECT_NAMES[w.subject][lang]} · {t.unit} {w.unit} ({w.accuracy}%)</span>
          ))}
        </div>
      )}
    </div>
  );
}