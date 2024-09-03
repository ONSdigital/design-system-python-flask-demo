DESIGN_SYSTEM_VERSION=`cat .design-system-version`

load-design-system-templates:
	./scripts/load_release.sh onsdigital/design-system $(DESIGN_SYSTEM_VERSION)

run: load-design-system-templates
	flask --app application run

format-python:
	poetry run isort .
	poetry run black .
	poetry run flake8 .

format:
	npx prettier --write .

generate-backstopjs:
	python3 -m generate_backstop_config

reference:
	backstop reference

test:
	backstop test

approve:
	backstop approve