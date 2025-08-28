# ---------- Stage 1: build Next.js ----------
FROM node:20-alpine AS web-build
ENV NEXT_DISABLE_ESLINT=1
WORKDIR /app

# Install deps (npm only for determinism)
COPY frontend/package.json frontend/package-lock.json ./frontend/
RUN cd frontend && npm ci

# Copy source and build (standalone output required)
COPY frontend ./frontend
RUN cd frontend && npm run build

# ---------- Stage 2: runtime ----------
FROM debian:bookworm-slim

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl tini supervisor \
    nodejs npm python3 python3-venv python3-pip \
 && rm -rf /var/lib/apt/lists/*

# --- Create the venv *in this image* and install Python deps
RUN python3 -m venv /venv
COPY requirements.txt /tmp/requirements.txt
RUN /venv/bin/pip install --no-cache-dir -r /tmp/requirements.txt

# --- Backend: copy your code
WORKDIR /srv/backend
# copy the whole backend package folder into /srv/backend/app
COPY app/ /srv/backend/app/
# ensure 'app' is importable as a package even if __init__.py is missing locally
RUN [ -f /srv/backend/app/__init__.py ] || touch /srv/backend/app/__init__.py

# --- Frontend: copy Next standalone artifacts
WORKDIR /srv/frontend
COPY --from=web-build /app/frontend/.next/standalone ./ 
COPY --from=web-build /app/frontend/.next/static ./.next/static
COPY --from=web-build /app/frontend/public ./public
COPY frontend/package.json ./package.json

# --- Supervisor config
WORKDIR /
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# --- Env & ports
# Next listens on PORT; uvicorn listens on 8000 (hard-coded in supervisor)
ENV PORT=8080 \
    HOST=0.0.0.0 \
    API_APP=app.main:app
EXPOSE 8080

ENTRYPOINT ["/usr/bin/tini","--"]
CMD ["supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]
