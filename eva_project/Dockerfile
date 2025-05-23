# Use slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for PDF and docx processing
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    libpoppler-cpp-dev \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Default command (overridden in docker-compose)
CMD ["python", "scripts/bootstrap_index.py"]# Dummy content for Dockerfile
