# Deploying theyashgupta.com to Fly.io (free)

This stack runs on Fly.io's always-free tier:
- 3 shared-CPU 256 MB VMs (we use 1)
- 3 GB persistent volume (we use ~50 MB for SQLite)
- Free custom domain + auto-renewing SSL

Total monthly cost: **$0** at this site's traffic level.

---

## One-time setup (~15 minutes)

### 1. Sign up at https://fly.io
Add a payment card (required to prevent bot abuse, **not** charged inside free limits).

### 2. Install the Fly CLI

```bash
# macOS
brew install flyctl

# or
curl -L https://fly.io/install.sh | sh
```

### 3. Log in

```bash
fly auth login
```

### 4. Set up Resend for transactional email
1. Sign up at https://resend.com (free, 3,000 emails / month).
2. Click **Domains → Add Domain** → enter `theyashgupta.com`.
3. Copy the SPF, DKIM, and Return-Path DNS records Resend shows you.
4. Add them at your domain registrar (Cloudflare, Namecheap, GoDaddy — whichever you use).
5. Wait ~5–60 minutes for Resend to verify the domain (it'll turn green).
6. Click **API Keys → Create** → copy the key starting with `re_…`. Save it for step 6.

### 5. Launch the Fly app
From the repo root:

```bash
cd /Users/yash/theyashgupta
fly launch --copy-config --no-deploy
```

When prompted:
- **App name**: pick a unique name (e.g. `theyashgupta-app`). Update the `app = ...` line in `fly.toml` if needed.
- **Region**: keep the default (`bom` for Mumbai) or pick the one closest to your audience.
- **Setup Postgres / Redis / Sentry**: choose **No** for all of them.
- **Deploy now?**: **No** — we have secrets to set first.

### 6. Set production secrets
Generate a long random Django secret:

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(60))"
```

Then set every required env var:

```bash
fly secrets set \
  DJANGO_SECRET_KEY="<paste the long secret from above>" \
  DJANGO_ALLOWED_HOSTS="theyashgupta.com,www.theyashgupta.com,theyashgupta-app.fly.dev" \
  DJANGO_CSRF_TRUSTED_ORIGINS="https://theyashgupta.com,https://www.theyashgupta.com,https://theyashgupta-app.fly.dev" \
  EMAIL_HOST_PASSWORD="re_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
  DEFAULT_FROM_EMAIL="Yash Gupta <yash@theyashgupta.com>" \
  LEAD_NOTIFICATION_EMAIL="yash@theyashgupta.com" \
  DJANGO_ADMIN_USERNAME="yash" \
  DJANGO_ADMIN_EMAIL="yash@theyashgupta.com" \
  DJANGO_ADMIN_PASSWORD="<pick a strong admin password>"
```

(Replace `theyashgupta-app` with your actual Fly app name.)

### 7. Create the persistent volume for SQLite
```bash
fly volumes create tyg_data --region bom --size 1 --yes
```

### 8. Deploy
```bash
fly deploy
```

This takes ~3–5 minutes the first time (it builds the Docker image, builds the Vite frontend inside, runs migrations on boot, and starts gunicorn).

When it finishes, open the app at `https://theyashgupta-app.fly.dev/` — the site should be fully live.

---

## Pointing your domain (`theyashgupta.com`)

### 1. Tell Fly to expect the domain
```bash
fly certs add theyashgupta.com
fly certs add www.theyashgupta.com
```

Fly prints the DNS records you need to add. Two records (A for `theyashgupta.com`, AAAA + CNAME for `www`).

### 2. Add the DNS records at your registrar
- `theyashgupta.com` → `A` record pointing to the IPv4 Fly shows.
- `www.theyashgupta.com` → `CNAME` pointing to `theyashgupta-app.fly.dev`.

Cloudflare is **recommended** — it gives you free CDN, free DDoS protection, and faster propagation. If you use Cloudflare, set the records to **"DNS only"** (grey cloud) initially, then switch to "Proxied" (orange cloud) after Fly issues the SSL cert.

### 3. Wait for SSL
Run `fly certs show theyashgupta.com` until it shows **`Configured: Yes`**. Usually 1–10 minutes.

Visit https://theyashgupta.com — done.

---

## Common operations after launch

| What you want to do | Command |
|---|---|
| Tail live logs | `fly logs` |
| Open a Django shell | `fly ssh console -C 'python manage.py shell'` |
| Run a one-off migration | `fly ssh console -C 'python manage.py migrate'` |
| Open the admin | https://theyashgupta.com/admin/ (login with the username/password from step 6) |
| Edit a blog post | Admin → Blog posts → Add post / edit existing. Sitemap auto-updates. |
| Change an env var | `fly secrets set KEY="value"` (auto-redeploys) |
| Roll back a bad deploy | `fly releases` then `fly deploy --image registry.fly.io/your-app:deployment-XXXXX` |
| Restart the app | `fly apps restart` |

---

## Free-tier limits you should know

| Resource | Free quota | What this site uses |
|---|---|---|
| VM time | 2,344 hours / month total across all apps | ~720 hrs (one VM always on) |
| Outbound bandwidth | 160 GB / month | < 1 GB at this stage |
| Persistent volume | 3 GB | ~50 MB (SQLite + media) |
| Custom domains | unlimited | 2 (`theyashgupta.com`, `www.theyashgupta.com`) |
| Resend emails | 3,000 / month | likely < 100 |

You'd have to **5×** your traffic before this approaches the free ceiling.

---

## When to upgrade

Switch to a paid tier when **any** of these happen:
- You consistently exceed the free VM hours (would require more than one always-on machine).
- Traffic pushes outbound bandwidth past 100 GB / month.
- SQLite writes become a bottleneck (concurrent admin edits + many blog comments). Migrate to managed Postgres (Fly has it; Supabase / Neon are free alternatives).

For where this site is today, free works indefinitely.
