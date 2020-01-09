
FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /TreloSinc

WORKDIR /TreloSinc

ADD . /TreloSinc/

RUN pip install -r requirements.txt