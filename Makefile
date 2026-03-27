install:
	uv sync

run:
	uv run gendiff file1.json file2.json

help:
	uv run gendiff -h

lint:
	uv run ruff check --fix gendiff

check: test lint

build:
	uv build

package-install:
	uv tool install --force dist/*.whl