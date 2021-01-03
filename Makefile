install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	pip install --user ~/Projects/python-project-lvl1/dist/*.whl
package-reinstall:
	pip install --user ~/Projects/python-project-lvl1/dist/*.whl --force-reinstall
brain-games:
	poetry run brain-games
lint:
	poetry run flake8 brain_games