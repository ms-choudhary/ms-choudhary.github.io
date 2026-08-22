TIL  := til
META := meta.json

.PHONY: clean build-notes serve

clean:
	rm -rf content/notes/*/ static/_images $(META) public

build-notes: clean
	git submodule update --init --remote $(TIL)
	python3 $(TIL)/build_meta.py > $(META)
	python3 scripts/build_notes.py $(META)
	cp -r $(TIL)/_images static/

serve: build-notes
	zola serve -p 8000
