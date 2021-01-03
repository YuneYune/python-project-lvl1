install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	pip install --user ~/Projects/python-project-lvl1/dist/hexlet_code-0.1.0-py3-none-any.whl
brain-games:
	poetry run brain-games