# apple-cta-websites

Landing pages for our seven apps. Each app gets one simple website, and each site has one job: collecting waitlist emails through a single call-to-action (CTA) button while the app is still being built.

## What each site does

- Shows one CTA button, a **"Join the waitlist"** email signup.
- Collects only an email address, to register interest.
- Nothing else. No extra pages, features or flows.

## Repository structure

All seven sites are served by one Cloudflare Worker (`lotus-waitlists`) on the route `bishal.app/lotus-*`, one path per app. The rest of `bishal.app` is the main site, a separate repo and Pages project.

```
apple-cta-websites/
├── README.md
├── APPS.md                     # Details for each app
├── wrangler.toml               # Worker config: route, static assets, D1 binding
├── src/index.js                # Waitlist API: POST /<app>/api/join → D1
└── public/                     # Generated static sites (don't edit by hand)
    ├── lotus-g-1/              # https://bishal.app/lotus-g-1/
    ├── lotus-c-1/              # https://bishal.app/lotus-c-1/
    ├── lotus-f-1/              # https://bishal.app/lotus-f-1/
    ├── lotus-f-2/              # https://bishal.app/lotus-f-2/
    ├── lotus-e-1/              # https://bishal.app/lotus-e-1/
    ├── lotus-e-2/              # https://bishal.app/lotus-e-2/
    └── lotus-e-3/              # https://bishal.app/lotus-e-3/
```

See [APPS.md](APPS.md) for what each app does, who it's for, and its key features.

## Waitlist storage: Cloudflare D1

All seven sites write to **one shared Cloudflare D1 database**.

- Each signup stores the email and which app it came from, so one database holds all seven waitlists.
- Every site's forms post to `api/join` relative to its own folder (`/lotus-g-1/api/join`), handled by the Worker, which is bound to the D1 database `waitlist-db`.

## Status

🚧 The apps are still being built. These sites exist only to capture interest before launch.

## Building the sites

The seven sites are generated from one shared design, so they stay consistent. Don't edit `public/` by hand; edit the source and rebuild.

```
tools/site-builder/
├── build.py          # Renders every app into public/<slug>/
├── assets/           # Shared styles.css and site.js
└── apps/             # One content file per app (copy, features, FAQ, policies)
```

```bash
python3 tools/site-builder/build.py              # build all seven
python3 tools/site-builder/build.py lotus-g-1    # build one
```

### Adding app screenshots

Every home page follows the same layout as the Dayline reference site: a hero phone plus a 7-card feature grid with phones peeking up from each card. Until real screenshots exist, each phone shows a placeholder naming the file it expects.

Drop portrait iPhone screenshots (1179×2556 works well) into `tools/site-builder/screens/<app-folder>/` and rebuild:

| File | Where it appears |
| --- | --- |
| `hero.png` | Hero phone |
| `card-1.png`, `card-3.png`, `card-4.png`, `card-6.png` | Single-phone cards |
| `card-2-1.png`, `card-2-2.png`, `card-5-1.png`, `card-5-2.png` | Two-phone cards |
| `card-7-1.png` … `card-7-3.png` | Full-width card |

`.jpg` and `.webp` work too. Missing files simply keep their placeholder.

## Waitlist

`POST /<app>/api/join` writes to the shared D1 database `waitlist-db`:

- `contacts`: one row per email (unique on the lowercased email)
- `waitlist_signups`: one row per email per app, with approximate location from Cloudflare (country, region, city, time zone, lat/long), `utm_*` tags from the landing URL, landing page, referrer, and the form it came from (`metadata.source`)
- `apps`: one row per site, matched on `slug` (the URL folder). Unknown or inactive slugs get a 404, so a new app needs a row here before its waitlist works.

Forms work without JavaScript too: a plain form post redirects back with `?joined=1`.

## Deploying

Everything deploys as one Worker from the repo root:

```bash
python3 tools/site-builder/build.py
npx wrangler deploy
```

Static files in `public/` are served directly. Only requests that match no file (the waitlist API) run `src/index.js`. Before `bishal.app` is live, the sites are also at `https://lotus-waitlists.bishalj-apps.workers.dev/<app>/`.

## Analytics

One Cloudflare Web Analytics site for `bishal.app` covers the main site and every `/lotus-*` page. It's cookieless. To see one app, filter the dashboard by path, e.g. `/lotus-g-1/`.

Export sign-ups (exports are gitignored; they contain personal data):

```bash
npx wrangler d1 execute waitlist-db --remote --json --command \
  "SELECT a.slug, c.email, s.joined_at, s.country, s.utm_source FROM waitlist_signups s JOIN contacts c ON c.id = s.contact_id JOIN apps a ON a.id = s.app_id ORDER BY s.joined_at"
```
