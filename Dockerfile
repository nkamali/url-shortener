FROM python:3.11-slim-buster

WORKDIR /app

COPY . /app

# Install system packages required by psycopg2 if you want to build from source
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    procps \
    && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Install Uvicorn for ASGI support
RUN pip install uvicorn

# Install FastAPI
RUN pip install fastapi

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
