SHELL := /bin/bash
PYTHON := $(shell which python2.7)

.PHONY: all clean

all: $(CURDIR)/tail

$(CURDIR)/tail:
	ln -s $@.py $@

clean:
	rm -rf $(CURDIR)/tail
