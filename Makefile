help:
	@echo 'make install:           Install package with pip -e . in your system python'

install: 
	pip install -r requirements.txt

hook:
	cp .hooks/pre-commit .git/hooks/pre-commit
	cp .hooks/pre-push .git/hooks/pre-push
	
unhook:
	rm .git/hooks/*

build:
	pip install devpi-client wheel
	python setup.py sdist bdist_wheel


.PHONY: venv help install test build
