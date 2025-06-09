#!/bin/sh

set -e

cd /app

echo "run: Alembic migrations..."
alembic upgrade head

echo "run: FastAPI app..."
exec uvicorn backend.api:app --host 0.0.0.0 --port 8000