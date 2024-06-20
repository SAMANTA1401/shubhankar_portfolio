# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# Set environment variables to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python and necessary tools
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Create a Python virtual environment
RUN python3 -m venv venv

# Activate the virtual environment and install dependencies
RUN /bin/bash -c "source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"

# Copy the current directory contents into the container at /app
COPY . /app

# Command to run the app using the virtual environment
CMD ["/bin/bash", "-c", "source venv/bin/activate && python manage.py runserver 0.0.0.0:8000"]


