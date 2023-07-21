FROM python:3.11-slim-buster

WORKDIR /app

# Install system packages required by psycopg2 if you want to build from source
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    procps \
    && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary

# Copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./app

# Install Gunicorn
RUN pip install gunicorn

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
