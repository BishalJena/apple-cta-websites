// Lotus waitlists: Pages Function for POST /<app>/api/join (e.g. /lotus-g-1/api/join).
//
// Static pages in public/<app>/ are served by Pages directly; only this route runs code.
//
// POST /<app>/api/join   { email, source?, page?, referrer? }   (JSON or form-encoded)
//   201 { ok: true }                 new sign-up
//   200 { ok: true, already: true }  email already on this app's waitlist
//   400 { error }                    bad input
//   404 { error }                    <app> isn't an active row in the apps table
//
// Each site's forms post to "api/join" relative to their own folder, so the app
// is the first path segment ([app] in this file's path). Writes go to the D1
// database bound as DB in wrangler.toml: contacts (one row per email) +
// waitlist_signups (one row per email per app). Form posts (no JavaScript)
// redirect back with ?joined=1.

const SLUG_RE = /^[a-z0-9-]+$/;
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const UTM_KEYS = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term"];

function json(body, status) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
  });
}

function clip(value, max) {
  const s = value == null ? "" : String(value).trim();
  return s ? s.slice(0, max) : null;
}

function parseUrl(value) {
  try {
    return value ? new URL(value) : null;
  } catch {
    return null;
  }
}

async function readBody(request) {
  const type = request.headers.get("Content-Type") || "";
  if (type.includes("application/json")) return { data: await request.json(), isForm: false };
  const form = await request.formData();
  return { data: Object.fromEntries(form), isForm: true };
}

export async function onRequestPost({ request, env, params }) {
  const slug = String(params.app || "");
  if (!SLUG_RE.test(slug)) return json({ error: "Not found" }, 404);
  return join(request, env, slug);
}

export function onRequest() {
  return json({ error: "Method not allowed" }, 405);
}

async function join(request, env, slug) {
  let data, isForm;
  try {
    ({ data, isForm } = await readBody(request));
  } catch {
    return json({ error: "Invalid request body." }, 400);
  }

  // Honeypot: real people never fill this hidden field.
  if (data.company) return json({ ok: true }, 200);

  const email = String(data.email || "").trim();
  const normalized = email.toLowerCase();
  if (!EMAIL_RE.test(normalized) || normalized.length > 254) {
    return json({ error: "Please enter a valid email address." }, 400);
  }

  const app = await env.DB
    .prepare("SELECT id FROM apps WHERE slug = ? AND is_active = 1")
    .bind(slug)
    .first();
  if (!app) return json({ error: "This waitlist isn't open right now." }, 404);

  // Same-origin form posts send the page as Referer; fetch() sends it as `page`.
  const landing = parseUrl(data.page) || parseUrl(request.headers.get("Referer"));
  const landingOk = landing && landing.host === new URL(request.url).host;
  const utm = UTM_KEYS.map((k) => (landingOk ? clip(landing.searchParams.get(k), 200) : null));
  const cf = request.cf || {};
  const metadata = JSON.stringify({ source: clip(data.source, 32) || "site" });

  const [, signup] = await env.DB.batch([
    env.DB
      .prepare("INSERT OR IGNORE INTO contacts (email, normalized_email) VALUES (?, ?)")
      .bind(email.slice(0, 254), normalized),
    env.DB
      .prepare(
        `INSERT OR IGNORE INTO waitlist_signups (
           contact_id, app_id, country, region, city, timezone, latitude, longitude,
           utm_source, utm_medium, utm_campaign, utm_content, utm_term,
           landing_page, referrer, metadata
         )
         SELECT id, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
         FROM contacts WHERE normalized_email = ?`,
      )
      .bind(
        app.id,
        clip(cf.country, 8), clip(cf.region, 100), clip(cf.city, 100), clip(cf.timezone, 64),
        cf.latitude != null ? Number(cf.latitude) : null,
        cf.longitude != null ? Number(cf.longitude) : null,
        ...utm,
        landingOk ? clip(landing.pathname + landing.search, 500) : null,
        clip(data.referrer, 500),
        metadata,
        normalized,
      ),
  ]);
  const already = signup.meta.changes === 0;

  if (isForm && landingOk) {
    landing.searchParams.set("joined", "1");
    landing.hash = "waitlist";
    return Response.redirect(landing.toString(), 303);
  }
  return json(already ? { ok: true, already: true } : { ok: true }, already ? 200 : 201);
}
