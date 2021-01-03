install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	pip install --user ~/Projects/python-project-lvl1/dist/*.whl
brain-games:
	poetry run brain-games