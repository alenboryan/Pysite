# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get clean && apt-get update && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    apt-get install -y python3 python3-pip libpq-dev gcc postgresql-client curl zip unzip && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application's code into the container
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
