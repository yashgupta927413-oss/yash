# =============================================================================
# theyashgupta.com — production image
# Stage 1: Build the Vite frontend
# Stage 2: Slim Python image that serves Django + the built static frontend
# =============================================================================

# ---------- Stage 1: Frontend build ------------------------------------------
FROM node:20-alpine AS frontend

WORKDIR /frontend

# Install deps with a clean lockfile-aware install
COPY frontend/package*.json ./
RUN npm ci --no-audit --no-fund

# Copy source and build (vite build → /frontend/dist)
COPY frontend/ ./
RUN npm run build

# ---------- Stage 2: Django runtime ------------------------------------------
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DJANGO_SETTINGS_MODULE=config.settings \
    DATABASE_PATH=/data/db.sqlite3 \
    PORT=8080

WORKDIR /app

# OS-level deps (only what gunicorn / sqlite need)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Python deps
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt

# Application source
COPY backend/ ./

# Built frontend → /app/frontend_dist (served at root via WhiteNoise)
COPY --from=frontend /frontend/dist ./frontend_dist

# Collect static (Django admin + website) into staticfiles/
RUN DJANGO_SECRET_KEY=build-time-placeholder \
    DJANGO_DEBUG=false \
    DJANGO_ALLOWED_HOSTS=localhost \
    python manage.py collectstatic --noinput

# Persistent volume for SQLite (Fly mounts /data here)
RUN mkdir -p /data && chmod 777 /data

EXPOSE 8080

# Entrypoint runs migrations + boots gunicorn
COPY backend/start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
