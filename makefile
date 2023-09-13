clean:
	rm -rf notebooks/_build

dev: clean
	jupyter-book config sphinx notebooks
	sphinx-autobuild notebooks _build/html -b html

build:
	jupyter-book build notebooks
