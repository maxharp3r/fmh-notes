basedir = docs

clean:
	rm -rf $(basedir)/_build
	rm $(basedir)/conf.py

dev:
	jupyter-book config sphinx $(basedir)
	sphinx-autobuild $(basedir) $(basedir)/_build/html -b html

build: clean
	jupyter-book build $(basedir)
