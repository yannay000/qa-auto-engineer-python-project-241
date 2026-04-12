install:
	uv sync

run:
	uv run gendiff files/file1.json files/file2.json

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

help:
	uv run gendiff -h

lint:
	uv run ruff check --fix gendiff tests

check: test lint

build:
	uv build

package-install:
	uv tool install --force dist/*.whl