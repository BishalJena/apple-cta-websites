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
├── lotus-g-1/    # Lotus G-1
├── lotus-c-1/    # Lotus C-1
├── lotus-f-1/    # Lotus F-1
├── lotus-f-2/    # Lotus F-2
├── lotus-e-1/    # Lotus E-1
├── lotus-e-2/    # Lotus E-2
└── lotus-e-3/    # Lotus E-3
```

See [APPS.md](APPS.md) for what each app does, who it's for, and its key features.

## Waitlist storage: Cloudflare D1

All seven sites write to **one shared Cloudflare D1 database**.

- Each signup stores the email and which app it came from, so a single table can hold all seven waitlists.
- Every site's CTA submits to the same backend, which writes to D1.

## Status

🚧 The apps are still being built. These sites exist only to capture interest before launch.

## Building the sites

The seven sites are generated from one shared design, so they stay consistent. Don't edit the `lotus-*/` folders by hand; edit the source and rebuild.

```
tools/site-builder/
├── build.py          # Renders every app into its folder
├── assets/           # Shared styles.css and site.js
└── apps/             # One content file per app (copy, features, FAQ, policies)
```

```bash
python3 tools/site-builder/build.py              # build all seven
python3 tools/site-builder/build.py lotus-g-1    # build one
WAITLIST_ENDPOINT=https://<worker-url>/api/join python3 tools/site-builder/build.py
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

Each `lotus-*/` folder is self-contained static HTML (pages: home, release notes, contact, privacy, terms, follow updates) and can be deployed on its own. Without `WAITLIST_ENDPOINT`, the forms show "The waitlist isn't connected yet".

## Waitlist API setup

`waitlist-api/` is a Cloudflare Worker that writes every site's signups to the shared D1 table (`email`, `app`, `source`, `created_at`, unique per email and app).

```bash
cd waitlist-api
npx wrangler d1 create lotus-waitlist                       # copy the id into wrangler.toml
npx wrangler d1 execute lotus-waitlist --remote --file=schema.sql
npx wrangler deploy                                         # then rebuild the sites with WAITLIST_ENDPOINT
```

Set `ALLOWED_ORIGINS` in `wrangler.toml` to the sites' domains before going live.
