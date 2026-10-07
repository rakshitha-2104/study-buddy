import { useState } from "react";
import { T } from "./i18n";
import { getToken, setToken } from "./api";
import Auth from "./pages/Auth";
import Home from "./pages/Home";
import Quiz from "./pages/Quiz";
import Dashboard from "./pages/Dashboard";
import "./styles.css";

// Simple state-based navigation: auth -> home -> quiz -> dashboard.
export default function App() {
  const [user, setUser] = useState(() => JSON.parse(localStorage.getItem("sb_user") || "null"));
  const [lang, setLang] = useState(() => user?.language || "kn");
  const [page, setPage] = useState(getToken() && user ? "home" : "auth");
  const [quiz, setQuiz] = useState(null); // { subject, unit }
  const t = T[lang];

  const onAuth = (res) => {
    setToken(res.token);
    localStorage.setItem("sb_user", JSON.stringify(res.user));
    setUser(res.user);
    setPage("home");
  };
  const logout = () => {
    setToken(null);
    localStorage.removeItem("sb_user");
    setUser(null);
    setPage("auth");
  };

  if (page === "auth") return <Auth lang={lang} setLang={setLang} t={t} onAuth={onAuth} />;

  return (
    <div className="shell">
      <header className="topbar">
        <b onClick={() => setPage("home")} style={{ cursor: "pointer" }}>📚 StudyBuddy</b>
        <span>
          👋 {user?.name}
          <button className="ghost" onClick={() => setPage("dashboard")}>📊 {t.dashboard}</button>
          <button className="ghost" onClick={logout}>{t.logout}</button>
        </span>
      </header>
      {page === "home" && <Home lang={lang} t={t} onStart={(subject, unit) => { setQuiz({ subject, unit }); setPage("quiz"); }} />}
      {page === "quiz" && <Quiz lang={lang} t={t} {...quiz} onDone={() => setPage("dashboard")} onBack={() => setPage("home")} />}
      {page === "dashboard" && <Dashboard lang={lang} t={t} onBack={() => setPage("home")} />}
    </div>
  );
}