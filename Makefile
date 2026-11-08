install:
	uv sync

brain-games:
	uv run brain-games

test:
	uv run pytest

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games

ci-build:
	uv sync --frozen && make build

setup:
	ci-build install lint test
