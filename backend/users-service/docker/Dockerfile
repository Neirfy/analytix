FROM python:3.13-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi --only main

COPY app ./



FROM python:3.13-slim AS dev

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* ./

# ставим ВСЁ включая dev
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi --with dev

# копируем и app и tests
COPY app ./app
# COPY tests ./tests

ENV PYTHONPATH=/app

CMD ["pytest", "-v"]



FROM python:3.13-slim AS prod

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=builder /usr/local/bin /usr/local/bin

COPY app ./app

ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]