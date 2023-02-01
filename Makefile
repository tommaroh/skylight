.PHONY: build
build:
	docker build -t skylight .

.PHONY: run
run: build
	docker run -p0.0.0.0:8000:80 skylight
