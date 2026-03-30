# theyashgupta.com - Professional Django + Vite Website

This repository contains a **Django backend** and a **professional frontend** served via Vite, focused on digital marketing services.

## Project Structure

- `backend/` - Django API (`/api/homepage/`)
- `frontend/` - Professional marketing website (Vite static frontend) with image-rich sections

## Run Backend (Django)

Compatible with Python 3.9+.

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Django API endpoint:
- `http://127.0.0.1:8000/api/homepage/`

## Production readiness checklist

1. Copy env template and set secure values:
   ```bash
   cp backend/.env.example backend/.env
   ```
2. Set a strong `DJANGO_SECRET_KEY`.
3. Set:
   - `DJANGO_DEBUG=false`
   - `DJANGO_ALLOWED_HOSTS` with your domain(s)
   - `DJANGO_CSRF_TRUSTED_ORIGINS` with HTTPS origins
4. Collect static files and run with Gunicorn:
   ```bash
   cd backend
   python manage.py collectstatic --noinput
   gunicorn config.wsgi:application --bind 0.0.0.0:8000
   ```

### Admin Panel (Manage FAQ / Policies / Settings)

```bash
python manage.py migrate
python manage.py runserver
```

Open:
- `http://127.0.0.1:8000/admin/`

Default login created by `./run_dev.sh`:
- Username: `admin`
- Password: `admin`

If you run backend manually and need to create/update that same default admin:

```bash
python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); u, _ = User.objects.get_or_create(username='admin', defaults={'email': 'admin@localhost', 'is_staff': True, 'is_superuser': True}); u.is_staff=True; u.is_superuser=True; u.set_password('admin'); u.save()"
```

In admin, update:
- FAQs
- Policies
- Site Settings (email, phone, WhatsApp, business name)
- Users (change username/password anytime)
- Statistics, Tools, Services, Growth Modules, Pricing Plans, Reviews, Google Reviews, and Process Steps
- Drag-and-drop full homepage section order via **Site Settings → Open drag editor**

Policy pages are pre-seeded with starter content on first migration and can be fully edited from admin.

## Run Backend + Frontend together (single command)

From repo root:

```bash
chmod +x run_dev.sh
./run_dev.sh
```

This starts:
- Backend: `http://127.0.0.1:8000`
- Admin: `http://127.0.0.1:8000/admin/`
- Frontend: `http://127.0.0.1:5173`

If it seems "stuck" on first run, it's usually installing dependencies.
Use verbose mode to debug:

```bash
bash -x ./run_dev.sh
```

## Run Frontend (Vite)

```bash
cd frontend
npm install
npm run dev
```

Frontend local URL:
- `http://127.0.0.1:5173`
