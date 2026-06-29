DESIGN_SYSTEM_VERSION=`cat .design-system-version`
DESIGN_SYSTEM_ENV_FILE?=.development.env

load-design-system-templates:
	./scripts/load_release.sh onsdigital/design-system $(DESIGN_SYSTEM_VERSION)

link-development-env:
	ln -sf $(DESIGN_SYSTEM_ENV_FILE) .env

run: load-design-system-templates link-development-env
	poetry run flask --app "$${FLASK_APP:-application}" run --host "$${FLASK_RUN_HOST:-127.0.0.1}" --port "$${FLASK_RUN_PORT:-5000}"

format-python:
	poetry run isort .
	poetry run black .
	poetry run flake8 .

format:
	npx prettier --write .
