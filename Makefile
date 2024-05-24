DESIGN_SYSTEM_VERSION=`cat .design-system-version`

load-design-system-templates:
	./scripts/load_release.sh onsdigital/design-system $(DESIGN_SYSTEM_VERSION)

run:
	./scripts/load_release.sh onsdigital/design-system $(DESIGN_SYSTEM_VERSION)
	flask --app application run

generate-backstopjs:
	python3 -m generate_backstop_config

reference:
	backstop reference

test:
	backstop test

approve:
	backstop approve