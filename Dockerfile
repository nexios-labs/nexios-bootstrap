FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create logs and migrations directories
RUN mkdir -p logs migrations

# Set Python path
ENV PYTHONPATH=/app

# Expose port
EXPOSE 52789

# Run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "52789","--reload"]
