clean:
	rm -rf notebooks/_build
	rm notebooks/conf.py

dev:
	jupyter-book config sphinx notebooks
	sphinx-autobuild notebooks notebooks/_build/html -b html

build: clean
	jupyter-book build notebooks
