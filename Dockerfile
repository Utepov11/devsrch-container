# pull official base image
FROM python:3.12.8

# set work directory
WORKDIR /devsearch

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY devsearch /devsearch