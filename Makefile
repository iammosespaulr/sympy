run: test

antlr:
	python setup.py antlr

test:
	pytest sympy/parsing/tests/test_latex.py

install:
	pip install . --target ../package/ --upgrade

install_loc: install
	pip install . --upgrade
