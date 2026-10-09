// Lotus waitlist API: one Cloudflare Worker + one D1 table for all seven sites.
//
// POST /api/join   { email, app, source? }   (JSON or form-encoded)
//   201 { ok: true }                 new sign-up
//   200 { ok: true, already: true }  email already on that app's waitlist
//   400 { error }                    bad input
//
// Form posts (no JavaScript) are redirected back to the page with ?joined=1.

export const APPS = new Set([
  "lotus-g-1", "lotus-c-1", "lotus-f-1", "lotus-f-2",
  "lotus-e-1", "lotus-e-2", "lotus-e-3",
]);

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function corsHeaders(request, env) {
  const origin = request.headers.get("Origin") || "";
  const allowed = (env.ALLOWED_ORIGINS || "*").split(",").map((s) => s.trim());
  const allow = allowed.includes("*") ? "*" : allowed.includes(origin) ? origin : "";
  return {
    ...(allow && { "Access-Control-Allow-Origin": allow }),
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Vary": "Origin",
  };
}

function json(body, status, headers) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", ...headers },
  });
}

async function readBody(request) {
  const type = request.headers.get("Content-Type") || "";
  if (type.includes("application/json")) return { data: await request.json(), isForm: false };
  const form = await request.formData();
  return { data: Object.fromEntries(form), isForm: true };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const cors = corsHeaders(request, env);

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    if (url.pathname !== "/api/join") return json({ error: "Not found" }, 404, cors);
    if (request.method !== "POST") return json({ error: "Method not allowed" }, 405, cors);

    let data, isForm;
    try {
      ({ data, isForm } = await readBody(request));
    } catch {
      return json({ error: "Invalid request body." }, 400, cors);
    }

    const email = String(data.email || "").trim().toLowerCase();
    const app = String(data.app || "").trim();
    const source = String(data.source || "site").trim().slice(0, 32);

    // Honeypot: real people never fill this hidden field.
    if (data.company) return json({ ok: true }, 200, cors);
    if (!EMAIL_RE.test(email) || email.length > 254) return json({ error: "Please enter a valid email address." }, 400, cors);
    if (!APPS.has(app)) return json({ error: "Unknown app." }, 400, cors);

    const result = await env.DB
      .prepare("INSERT OR IGNORE INTO waitlist (email, app, source) VALUES (?, ?, ?)")
      .bind(email, app, source)
      .run();
    const already = result.meta.changes === 0;

    if (isForm) {
      const back = request.headers.get("Referer");
      if (back) {
        const target = new URL(back);
        target.searchParams.set("joined", "1");
        target.hash = "waitlist";
        return Response.redirect(target.toString(), 303);
      }
    }
    return json(already ? { ok: true, already: true } : { ok: true }, already ? 200 : 201, cors);
  },
};
