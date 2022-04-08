# functions-from-zero2
This is a new repo for building functions from zero

[![Python application test with Github Actions](https://github.com/noahgift/functions-from-zero2/actions/workflows/main.yml/badge.svg)](https://github.com/noahgift/functions-from-zero2/actions/workflows/main.yml)

[![Code Build](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiaUxCMHhMQXdpRWloZmhhRlVPQnBsd2xsSHR3eGZxZTQwQ1k2bndjakg5T1RaQW1rTUhNbWhHV3JjR1pWVDViSEVORUJjSlU0RHBTaCtmOWxSOUdnWVQwPSIsIml2UGFyYW1ldGVyU3BlYyI6IlNRdjFQOU9qakZpTzJjZHQiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

## Step One for New Project

Use a production mindset from Day One

## Step Functions


![Step functions](https://user-images.githubusercontent.com/58792/162226407-7d522759-2eb4-4276-8d26-7dffa13b1a17.png)

## Containerized FastAPI

`docker build .`
`docker run -p 127.0.0.1:8080:8080 a92690211e75`


![Drawing-7 sketchpad](https://user-images.githubusercontent.com/58792/162333520-fd42b304-8e6f-46fd-b372-96a4fd4fa2e1.png)

Continuous Delivery is one line of code via [buildspec.yaml](https://github.com/noahgift/functions-from-zero2/blob/main/buildspec.yml) and the `make deploy` command:  [make deploy](https://github.com/noahgift/functions-from-zero2/blob/4eb6360e7d6dddbca6f4a497e197abb93b0966cf/Makefile#L15-L19)

```make
deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t deploy-fastapi .
	docker tag deploy-fastapi:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/deploy-fastapi:latest
	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/deploy-fastapi:latest
```

## References

### Continuous Delivery of Microservice
* [Watch on YouTube-Functions to Containerized Microservice Continuous Delivery to AWS App Runner with Fast API](https://www.youtube.com/watch?v=8qRYu4Q7RQU)
* [Watch on O'Reilly-Functions to Containerized Microservice Continuous Delivery to AWS App Runner with Fast API](https://learning.oreilly.com/videos/functions-to-containerized/04072022VIDEOPAIML/)

### Step Functions with AWS Lambda
* [O'Reilly-Getting Started With Aws Lambda Step Functions](https://learning.oreilly.com/videos/getting-started-with/040722022VIDEOPAIML/040722022VIDEOPAIML-c1_s0/)
* [YouTube-Getting Started With AWS Lambda Step Functions](https://www.youtube.com/watch?v=7CCUnHblg2s)

### Python Fire CLI
* [YouTube-Python-Fire-CLI](https://youtu.be/DKWd-QUytPo)
* [O'Reilly-Quickstart Python Fire Command Line Interface (CLI)](https://learning.oreilly.com/videos/quickstart-python-fire/040812022VIDEOPAIML/)

### Refactoring a Python script into a library called by Python Click CLI
* [YouTube-Refactoring a Python script into a library called by Python Click CLI](https://youtu.be/0x261nI5Yws)
* [O'Reilly-Refactoring a Python script into a library called by Python Click CLI](https://learning.oreilly.com/videos/refactoring-a-python/04082022VIDEOPAIML/)

### Learn Python in Five Minutes with Colab

* [YouTube-Learn Python in Five Minutes with Colab](https://www.youtube.com/watch?v=BTmJR3x_35c)
* [O'Reilly-Learn Python in five Minutes with Colab Notebook](https://learning.oreilly.com/videos/learn-python-in/04083022VIDEOPAIML/)

