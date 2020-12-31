# Inherit from other images
FROM python:3.6

MAINTAINER Tahir Shaukat

ENV PYTHONUNBUFFERED 1

# copy from local to docker image
COPY ./requirements.txt /requirements.txt 

# RUN - command triggers while we build the docker image.
RUN pip install -r /requirements.txt
RUN mkdir /app
WORKDIR /app
COPY . /app
EXPOSE 8099
CMD ["python", "app/main.py"]

