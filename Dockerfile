# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

EXPOSE 5000

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update -yy && \
    apt-get upgrade -yy && \
    apt-get install curl -yy && \
    pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt
