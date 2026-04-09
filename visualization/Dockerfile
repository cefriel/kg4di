FROM python:3.12-slim

WORKDIR /app

# Copy dependency file first for better layer caching
COPY pyproject.toml ./

# Install dependencies
RUN pip install --no-cache-dir .

# Copy application code
COPY main.py .
COPY static/ static/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


