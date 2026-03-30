# theyashgupta.com - Professional Django + React Website

This repository now contains a **Django backend** and a **React frontend** focused on digital marketing services.

## Project Structure

- `backend/` - Django API (`/api/homepage/`)
- `frontend/` - React (Vite) professional marketing website with image-rich sections

## Run Backend (Django)

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Django API endpoint:
- `http://127.0.0.1:8000/api/homepage/`

## Run Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

Frontend local URL:
- `http://127.0.0.1:5173`
