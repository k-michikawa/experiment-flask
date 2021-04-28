FROM python:3.10.0a7-alpine3.13

WORKDIR /app

RUN pip3 install Flask==1.1.2
