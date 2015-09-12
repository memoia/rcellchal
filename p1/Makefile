SHELL := /bin/bash
PYTHON := $(shell which python2.7)

.PHONY: all clean

all: $(CURDIR)/words.txt
	$(PYTHON) -i anagram.py

$(CURDIR)/words.txt:
	gunzip -k $@.gz

clean:
	rm -f $(CURDIR)/words.txt
