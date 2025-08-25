FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY app /app/app

# Either A) use /tmp DB (no chown needed), or B) chown /app.
# --- Option B shown here:
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080
ENV PORT=8080

# IMPORTANT: use shell so $PORT expands
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
