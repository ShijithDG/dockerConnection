FROM python:3.11-slim-buster

# Install dependencies
RUN pip install -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Build the package
RUN python setup.py sdist

# Run unit tests
RUN python -m unittest discover tests