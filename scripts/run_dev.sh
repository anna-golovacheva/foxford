#!/bin/bash

# Run migrations
alembic upgrade head

# Start the FastAPI application
uvicorn src.main:app --host 0.0.0.0 --port 8000