FROM python:3.7

RUN mkdir /src
WORKDIR /src
COPY Pipfile, Pipfile.lock ./
RUN pip install -U pipenv
RUN pipenv install --system

