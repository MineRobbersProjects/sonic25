PYFILES=$(wildcard *.py)

bin/sonic25.py: $(PYFILES)
	cat $(PYFILES) > bin/sonic25.py

.PHONY: play
play: bin/sonic25.py
	@clear; python bin/sonic25.py
