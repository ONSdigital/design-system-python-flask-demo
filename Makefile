DESIGN_SYSTEM_VERSION=`cat .design-system-version`

load-design-system-templates:
	./scripts/load_release.sh onsdigital/design-system $(DESIGN_SYSTEM_VERSION)

run:
	./scripts/load_release.sh onsdigital/design-system $(DESIGN_SYSTEM_VERSION)
	flask --app application run

  