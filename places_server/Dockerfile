FROM python:3.12-alpine AS build

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /home

COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR



FROM python:3.12-alpine AS production

ENV VIRTUAL_ENV=/home/.venv \
    PATH="/home/.venv/bin:$PATH"

COPY --from=build ${VIRTUAL_ENV} ${VIRTUAL_ENV}

WORKDIR /home

COPY places_server ./places_server
COPY migrations ./migrations
COPY alembic.ini .

ENTRYPOINT ["python", "-m", "places_server.main"]