PYFILES=$(wildcard *.py)

all: $(PYFILES)
	cat $(PYFILES) > bin/sonic25.py

play:
	python bin/sonic25.py
