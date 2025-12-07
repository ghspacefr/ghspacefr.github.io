all: build

clean:
	rm -rf public
	
build:
	mkdir -p public
	cp -rf static public/static/
	python app.py

run: build
	python -m http.server -d public
