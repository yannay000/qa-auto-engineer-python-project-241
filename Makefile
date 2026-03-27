install:
	uv sync

gendiff:
	uv run gendiff 1 2

lint:
	uv run ruff check --fix gendiff

check: test lint

build:
	uv build

package-install:
	uv tool install --force dist/*.whl