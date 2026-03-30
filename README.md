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

### Admin Panel (Manage FAQ / Policies / Settings)

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- `http://127.0.0.1:8000/admin/`

In admin, update:
- FAQs
- Policies
- Site Settings (email, phone, WhatsApp, business name)

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
