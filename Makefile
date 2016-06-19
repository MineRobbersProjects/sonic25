PYFILES=$(wildcard *.py)

bin/sonic25.py: $(PYFILES)
	cat $(PYFILES) > bin/sonic25.py

play: bin/sonic25.py
	@python bin/sonic25.py
