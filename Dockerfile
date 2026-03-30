# 1. Use a slim Python image
FROM python:3.12-slim

# 2. Optimization: prevent Python from writing .pyc files & buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set work directory
WORKDIR /app

# 4. Install system dependencies for PostgreSQL (psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the code
COPY . .

# 7. Run as a non-root user for security (Industry Standard)
RUN useradd -m appuser
USER appuser

# 8. Start the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]