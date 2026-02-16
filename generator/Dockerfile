FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app

# Copy requirements (relative to context ./generator)
COPY requirements.txt .

# Install dependencies
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Copy source code
COPY . /app/generator

# Set PYTHONPATH
ENV PYTHONPATH=/app

CMD ["python", "-m", "generator.src.main"]
