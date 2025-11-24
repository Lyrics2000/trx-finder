FROM python:3.9-slim

# Set working directory
WORKDIR /password1/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY trx.py .
COPY docker-entrypoint.sh .

# Make entrypoint executable
RUN chmod +x docker-entrypoint.sh

# Create volume for storing results
VOLUME /password1/app/results

# Set entrypoint
ENTRYPOINT ["./docker-entrypoint.sh"]