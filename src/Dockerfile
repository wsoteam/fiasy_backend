FROM python:3.7

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /fiasy
RUN mkdir /fiasy/src
WORKDIR /fiasy/src
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
