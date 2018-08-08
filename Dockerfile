# Use an official Python runtime as a parent image
FROM python:3-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD hello_world.py /app

# Logs can be collected here
RUN mkdir /logs
RUN mkdir /results
