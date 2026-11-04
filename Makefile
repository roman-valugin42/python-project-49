install:
	uv sync

brain-games:
	uv run brain-games

test:
    npm run test

build:
	UV_PYTHON=python3.12 uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games
