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

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t deploy-fastapi .
	docker tag deploy-fastapi:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/deploy-fastapi:latest
	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/deploy-fastapi:latest

all: install format lint test deploy