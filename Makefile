all: build

clean:
	rm -rf public
	
build:
	mkdir -p public
	python app.py
	cp -rf static public/static/

run: build
	python -m http.server -d public
