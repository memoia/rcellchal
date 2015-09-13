SHELL := /bin/bash
PYTHON := $(shell which python2.7)
OPT := $(CURDIR)/opt
export PATH := $(OPT)/bin:$(PATH)

.PHONY: all clean

all: $(OPT) $(CURDIR)/tail

$(OPT):
	virtualenv --python=$(PYTHON) $@
	pip install -U pip setuptools watchdog

$(CURDIR)/tail:
	ln -s $@.py $@

clean:
	rm -rf $(CURDIR)/tail $(OPT)
