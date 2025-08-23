# Use a small base
FROM python:3.11-slim

# Avoid .pyc and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps (build tools only if you need wheels compiled)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create a non-root user (recommended for Cloud Run)
RUN useradd -m appuser
USER appuser

# Expose is optional for Cloud Run, but fine for local runs
EXPOSE 8080

# Start server; expand $PORT at runtime with a local default 8080
# IMPORTANT: use sh -c so ${PORT} is expanded by the shell.
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
