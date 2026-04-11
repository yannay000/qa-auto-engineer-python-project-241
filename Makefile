install:
	uv sync

run:
	uv run gendiff file1.json file2.json

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

help:
	uv run gendiff -h

lint:
	uv run ruff check --fix gendiff

check: test lint

build:
	uv build

package-install:
	uv tool install --force dist/*.whl