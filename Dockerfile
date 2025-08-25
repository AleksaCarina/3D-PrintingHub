# Use a small base
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# (Optional) build tools – only needed if a wheel must compile
# bcrypt ships wheels for linux/py3.11, so you can usually skip this.
# RUN apt-get update -y && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps first (cache-friendly)
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy only your application code (avoid copying venv/.git/etc.)
COPY app /app/app

# Create a non-root user
RUN useradd -m appuser
USER appuser

# Cloud Run uses $PORT; default to 8080 for local
EXPOSE 8080
ENV PORT=8080

# Start server — NOTE: module path changed to app.main:app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
