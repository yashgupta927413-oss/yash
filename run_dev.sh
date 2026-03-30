#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

cd "$BACKEND_DIR"

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# shellcheck source=/dev/null
source .venv/bin/activate
python -m pip install -q --upgrade pip
python -m pip install -q -r requirements.txt
python manage.py migrate >/dev/null

cd "$FRONTEND_DIR"
if [ ! -d "node_modules" ]; then
  npm install >/dev/null
fi

cleanup() {
  echo "\nStopping backend/frontend..."
  kill "$BACKEND_PID" "$FRONTEND_PID" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

cd "$BACKEND_DIR"
python manage.py runserver 127.0.0.1:8000 &
BACKEND_PID=$!

cd "$FRONTEND_DIR"
npm run dev -- --host 127.0.0.1 --port 5173 &
FRONTEND_PID=$!

echo "Backend:  http://127.0.0.1:8000"
echo "Admin:    http://127.0.0.1:8000/admin/"
echo "Frontend: http://127.0.0.1:5173"
echo "Press Ctrl+C to stop both servers."

wait "$BACKEND_PID" "$FRONTEND_PID"
