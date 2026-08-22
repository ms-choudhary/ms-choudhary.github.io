TIL      := til
META     := meta.json
GH_USER  := ms-choudhary
PROJECTS := content/projects/data.toml

.PHONY: clean build-notes projects serve build

clean:
	rm -rf content/notes/*/ static/_images $(META) public

build-notes: clean
	git submodule update --init --remote $(TIL)
	python3 $(TIL)/build_meta.py > $(META)
	python3 scripts/build_notes.py $(META)
	cp -r $(TIL)/_images static/

# write via a temp file so a failed fetch leaves the previous data.toml intact
projects:
	@echo "Fetching latest project metadata from GitHub..."
	python3 scripts/fetch_all_github_projects.py $(GH_USER) > $(PROJECTS).tmp
	mv $(PROJECTS).tmp $(PROJECTS)
	@echo "Successfully updated $(PROJECTS)"

serve: build-notes projects
	zola serve -p 8000

build: build-notes projects
	zola build
