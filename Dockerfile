# Dockerfile

FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY calculator.py .
COPY test_calculator.py .
COPY setup.py .  # Ensure this is included if your project requires it
COPY requirements.txt .  # Include requirements file if needed

# Switch to root to install packages
USER root

# Install necessary packages
RUN apt-get update && apt-get install -y \
    unzip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Switch back to a non-root user (optional)
USER nobody

# Command to run tests
CMD ["python", "-m", "unittest", "test_calculator.py"]
