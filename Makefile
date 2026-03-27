install:
	uv sync

run:
	uv run gendiff 1 2

help:
	uv run gendiff -h

lint:
	uv run ruff check --fix gendiff

check: test lint

build:
	uv build

package-install:
	uv tool install --force dist/*.whl