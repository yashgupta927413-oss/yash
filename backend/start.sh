#!/usr/bin/env bash
# Container entrypoint for theyashgupta.com.
# - Runs migrations against the persistent SQLite at /data/db.sqlite3
# - Ensures the configured superuser exists (env-driven)
# - Boots gunicorn on $PORT (Fly.io expects 8080)
set -euo pipefail

cd /app

echo "==> Running migrations..."
python manage.py migrate --noinput

# Make sure the Site row for sitemap.xml uses the real domain
if [[ -n "${SITE_DOMAIN:-}" ]]; then
  python manage.py shell -c "
from django.contrib.sites.models import Site
Site.objects.update_or_create(pk=1, defaults={'domain': '${SITE_DOMAIN}', 'name': '${SITE_DOMAIN}'})
"
fi

# Optional: seed an admin user from env (only if vars are set; password must be set securely)
if [[ -n "${DJANGO_ADMIN_USERNAME:-}" && -n "${DJANGO_ADMIN_PASSWORD:-}" ]]; then
  echo "==> Ensuring superuser ${DJANGO_ADMIN_USERNAME}..."
  python manage.py shell -c "
from django.contrib.auth import get_user_model
U = get_user_model()
u, _ = U.objects.get_or_create(username='${DJANGO_ADMIN_USERNAME}', defaults={'email':'${DJANGO_ADMIN_EMAIL:-admin@localhost}','is_staff':True,'is_superuser':True})
u.is_staff = True
u.is_superuser = True
u.set_password('${DJANGO_ADMIN_PASSWORD}')
u.save()
print('Superuser ready:', u.username)
"
fi

echo "==> Starting gunicorn on :${PORT}..."
exec gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT}" \
  --workers 2 \
  --threads 4 \
  --timeout 60 \
  --access-logfile - \
  --error-logfile -
