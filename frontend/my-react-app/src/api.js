// Thin fetch wrapper. The login token is kept in localStorage so a refresh keeps you signed in.
export const getToken = () => localStorage.getItem("sb_token");
export const setToken = (t) => (t ? localStorage.setItem("sb_token", t) : localStorage.removeItem("sb_token"));

export async function api(path, body) {
  const res = await fetch("/api" + path, {
    method: body ? "POST" : "GET",
    headers: { "Content-Type": "application/json", Authorization: "Bearer " + (getToken() || "") },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || "error");
  return data;
}