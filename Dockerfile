# Use the official Python 3.11 slim image
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Build the package
RUN python setup.py sdist

# Run unit tests
RUN python -m unittest discover -s tests

# Command to run your application (optional, adjust as needed)
# CMD ["python", "your_script.py"]
