# https://makefiletutorial.com

.PHONY: clean uninstall test doc-serve doc-deploy

TARGET := homegrown
SHELL  := /bin/bash


PYTHON ?= /usr/bin/env python
PIP    ?= $(PYTHON) -m pip

SOURCE_DIR := $(PWD)/src
BUILD_DIR  := $(PWD)/build
DIST_DIR   := $(PWD)/dist
GIT_ROOT   := "$(shell git rev-parse --show-toplevel)"
TOOL_DIR   := "$(GIT_ROOT)/util"

SRC := $(shell find $(SOURCE_DIR) -type f) setup.py

# Default rule to run if `make` is executed with no arguments
all: help

# List all make rules and prefixed informational comments
help:
	@REGEX='^([^\$$: \.]+):.*$$'; \
	grep -B 1 -o -E "$$REGEX" $(abspath $(lastword $(MAKEFILE_LIST))) \
	| sed -E -e "s/$$REGEX/\1/g" \
	| awk '{line[NR]=$$0} END {for (i=NR; i>=1; i--) print line[i]}' \
	| paste -d' ' -s - \
	| sed -E -e $$'s/--/\\\n/g' -e $$'s/#/\\\t- /g' \
	| sed $$'s/^ //g' \
	| awk '{line[NR]=$$0} END {for (i=NR; i>=1; i--) print line[i]}'

# A simple alias for creating a module directory
build: $(BUILD_DIR)

# Build an installable module directory
$(BUILD_DIR): $(SRC)
	$(PYTHON) setup.py build
	
# A simple alias for building an uploadable/installable module tarball
dist: $(DIST_DIR)
	
# Build an uploadable/installable module tarball
$(DIST_DIR): $(BUILD_DIR)
	$(PYTHON) setup.py sdist

# Clean up build artifacts and cached bytecode
clean:
	$(PYTHON) setup.py clean
	find . -type f -name '*.pyc' -exec rm -rf {} \;       2>/dev/null ||:
	find . -type d -name '__pycache__' -exec rm -rf {} \; 2>/dev/null ||:
	find . -name '*.egg-info' -exec rm -rf {} \;          2>/dev/null ||:
	rm -rfv \
		.pytest_cache \
		build         \
		dist          \
		*.egg-info    \
		$(BUILD_DIR)  \
		VERSION
		
# Install this module from source code using setup.py
install-setup: clean
	$(PYTHON) setup.py install

# Install this module from source code using pip
install-pip: clean
	$(PIP) install --upgrade .
	
# Install this module in editable mode so source code changes are immediately used on import
install-edit: clean
	$(PIP) install --upgrade --editable .

# Uninstall this module
uninstall:
	$(PIP) uninstall $(TARGET)

# Use a temporary virtual environment to run pytest tests
test:
	@"$(TOOL_DIR)/run-tests.sh"
	
# Build and serve mkdocs documentation site on your local machine
docs-serve:
	@"$(TOOL_DIR)/mkdocs-serve-local.sh"
	
# Build and deploy mkdocs documentation site to the GitHub Pages site
docs-deploy:
	@"$(TOOL_DIR)/mkdocs-deploy-github-pages.sh"