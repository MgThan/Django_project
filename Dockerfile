#Base Image
FROM python:3

#Set default environment variables
ENV PYTHONUNBUFFERED 1

#create and set working directory
RUN mkdir /app
WORKDIR /app
#Add current directory code to working directory
ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/
