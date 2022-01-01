FROM python:3.10-alpine

LABEL maintainer="AZHAR IQBAL"
LABEL version="1.0.0"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D app
USER app
