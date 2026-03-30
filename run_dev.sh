#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

cd "$BACKEND_DIR"
echo "==> Backend setup starting..."

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 not found. Install Python 3 first."
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "Error: npm not found. Install Node.js first."
  exit 1
fi

if [ ! -d ".venv" ]; then
  echo "==> Creating backend virtualenv..."
  python3 -m venv .venv
fi

# shellcheck source=/dev/null
source .venv/bin/activate
echo "==> Installing backend dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo "==> Running backend migrations..."
python manage.py migrate

cd "$FRONTEND_DIR"
if [ ! -d "node_modules" ]; then
  echo "==> Installing frontend dependencies..."
  npm install
fi

cleanup() {
  echo "\nStopping backend/frontend..."
  kill "$BACKEND_PID" "$FRONTEND_PID" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

cd "$BACKEND_DIR"
echo "==> Starting Django backend..."
python manage.py runserver 127.0.0.1:8000 &
BACKEND_PID=$!

cd "$FRONTEND_DIR"
echo "==> Starting Vite frontend..."
npm run dev -- --host 127.0.0.1 --port 5173 &
FRONTEND_PID=$!

echo "Backend:  http://127.0.0.1:8000"
echo "Admin:    http://127.0.0.1:8000/admin/"
echo "Frontend: http://127.0.0.1:5173"
echo "Press Ctrl+C to stop both servers."

wait "$BACKEND_PID" "$FRONTEND_PID"
