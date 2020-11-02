help:
	@echo 'make install:           Install package with pip -e . in your system python'

install: 
	pip install -r requirements.txt

lint:
	flake8 gcli


build:
	pip install devpi-client wheel
	python setup.py sdist bdist_wheel


.PHONY: venv help install test build
