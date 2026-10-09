# apple-cta-websites

Landing pages for our seven apps. Each app gets one simple website, and each site has one job: collecting waitlist emails through a single call-to-action (CTA) button while the app is still being built.

## What each site does

- Shows one CTA button, a **"Join the waitlist"** email signup.
- Collects only an email address, to register interest.
- Nothing else. No extra pages, features or flows.

## Repository structure

All seven sites live in this repo, one folder per app. Each folder is deployed and hosted on its own.

```
apple-cta-websites/
├── README.md
├── APPS.md       # Details for each app
├── lotus-g-1/    # Lotus G-1 → https://lotus-g-1.pages.dev
├── lotus-c-1/    # Lotus C-1 → https://lotus-c-1.pages.dev
├── lotus-f-1/    # Lotus F-1 → https://lotus-f-1.pages.dev
├── lotus-f-2/    # Lotus F-2 → https://lotus-f-2.pages.dev
├── lotus-e-1/    # Lotus E-1 → https://lotus-e-1.pages.dev
├── lotus-e-2/    # Lotus E-2 → https://lotus-e-2.pages.dev
└── lotus-e-3/    # Lotus E-3 → https://lotus-e-3.pages.dev
```

See [APPS.md](APPS.md) for what each app does, who it's for, and its key features.

## Waitlist storage: Cloudflare D1

All seven sites write to **one shared Cloudflare D1 database**.

- Each signup stores the email and which app it came from, so one database holds all seven waitlists.
- Every site is a Cloudflare Pages project with its own Pages Function at `/api/join`, bound to the D1 database `waitlist-db`.

## Status

🚧 The apps are still being built. These sites exist only to capture interest before launch.

## Building the sites

The seven sites are generated from one shared design, so they stay consistent. Don't edit the `lotus-*/` folders by hand; edit the source and rebuild.

```
tools/site-builder/
├── build.py          # Renders every app into its folder
├── assets/           # Shared styles.css and site.js
├── functions/api/    # The /api/join Pages Function, copied into every site
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

Each `lotus-*/` folder is a self-contained Cloudflare Pages project:

```
lotus-g-1/
├── wrangler.toml       # Pages config: D1 binding (DB → waitlist-db) + APP_SLUG
├── functions/api/      # POST /api/join → D1
└── public/             # Static pages: home, release notes, contact, privacy, terms, follow updates
```

## Waitlist

`POST /api/join` on each site writes to the shared D1 database `waitlist-db`:

- `contacts`: one row per email (unique on the lowercased email)
- `waitlist_signups`: one row per email per app, with approximate location from Cloudflare (country, region, city, time zone, lat/long), `utm_*` tags from the landing URL, landing page, referrer, and the form it came from (`metadata.source`)
- `apps`: one row per site. The site's `APP_SLUG` picks the row, so a site can only add to its own waitlist.

Forms work without JavaScript too: a plain form post redirects back with `?joined=1`.

## Deploying

Deploy each site from its own folder, so Wrangler picks up that folder's `wrangler.toml` and `functions/`:

```bash
python3 tools/site-builder/build.py
for s in lotus-*/; do (cd "$s" && npx wrangler pages deploy --branch main --force); done
```

`--force` sends the deploy to Cloudflare Pages. Without it, recent Wrangler versions try to deploy to Workers static assets instead.

Export sign-ups (exports are gitignored; they contain personal data):

```bash
npx wrangler d1 execute waitlist-db --remote --json --command \
  "SELECT a.slug, c.email, s.joined_at, s.country, s.utm_source FROM waitlist_signups s JOIN contacts c ON c.id = s.contact_id JOIN apps a ON a.id = s.app_id ORDER BY s.joined_at"
```
