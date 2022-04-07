install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest  --nbval-lax *.ipynb
	python -m pytest -vv --cov=hello --cov=cli test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install format lint test