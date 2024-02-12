run:
	poetry run main

install:
	poetry install

lint:
	poetry run ruff format .
	poetry run ruff check .
	poetry run mypy .

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=places_server