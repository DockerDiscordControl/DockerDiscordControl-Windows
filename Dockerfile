FROM python:3.11-slim

WORKDIR /app

# Install system dependencies and upgrade to latest security patches
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    curl \
    wget \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -g 1000 ddc && \
    useradd -u 1000 -g ddc -s /bin/bash -m ddc

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create directories and set permissions
RUN mkdir -p /app/config /app/logs /app/data && \
    chown -R ddc:ddc /app

# Install supervisor
RUN pip install supervisor

# Configure supervisord - Create directory first
RUN mkdir -p /etc/supervisor/conf.d && \
    echo "[supervisord]" > /etc/supervisor/conf.d/supervisord.conf && \
    echo "logfile=/app/logs/supervisord.log" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "pidfile=/var/run/supervisord.pid" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "[program:bot]" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "command=python bot.py" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "directory=/app" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "user=ddc" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "autostart=true" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "autorestart=true" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "[program:webapp]" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "command=python app/app.py" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "directory=/app" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "user=ddc" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "autostart=true" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "autorestart=true" >> /etc/supervisor/conf.d/supervisord.conf

USER ddc

EXPOSE 8374 9374

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:9374/health || exit 1

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf", "-n"]
