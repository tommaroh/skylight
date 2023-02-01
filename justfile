build:
	docker build -t skylight:latest .

run: build
	docker run --rm -p 8080:8080 skylight:latest
