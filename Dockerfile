# Multi-stage Debian Build for Windows Docker Desktop
# Optimized for Windows environments with WSL2 backend
FROM python:3.12-slim-bookworm AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libc6-dev \
    libffi-dev \
    libssl-dev \
    cargo \
    rustc \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install wheel
RUN pip install --no-cache-dir --upgrade pip wheel

# Install Python dependencies
RUN pip install --no-cache-dir \
    Flask==3.1.1 \
    Werkzeug==3.1.3 \
    py-cord==2.6.1 \
    gunicorn==23.0.0 \
    gevent==24.11.1 \
    docker==7.1.0 \
    cryptography>=45.0.5 \
    APScheduler==3.10.4 \
    python-dotenv==1.0.1 \
    PyYAML==6.0.1 \
    requests==2.32.4 \
    aiohttp>=3.12.14 \
    Flask-HTTPAuth==4.8.0 \
    Jinja2>=3.1.4 \
    python-json-logger==2.0.7 \
    pytz==2024.2 \
    cachetools==5.3.2 \
    itsdangerous>=2.2.0 \
    click>=8.1.7 \
    blinker>=1.8.2 \
    MarkupSafe>=2.1.5 \
    flask-limiter>=3.5.0 \
    limits>=3.9.0 \
    greenlet>=3.0.3 \
    zope.event>=5.0 \
    zope.interface>=6.2 \
    audioop-lts==0.2.1

# Production stage
FROM python:3.12-slim-bookworm AS production

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    supervisor \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create user for security
RUN groupadd -r -g 1000 ddcuser && \
    useradd -r -u 1000 -g ddcuser -s /bin/bash -d /app ddcuser

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy application files
COPY --chown=ddcuser:ddcuser bot.py .
COPY --chown=ddcuser:ddcuser app/ app/
COPY --chown=ddcuser:ddcuser utils/ utils/
COPY --chown=ddcuser:ddcuser cogs/ cogs/
COPY --chown=ddcuser:ddcuser gunicorn_config.py .

# Copy supervisord configuration
COPY supervisord-optimized.conf /etc/supervisor/conf.d/supervisord.conf
COPY supervisord-optimized.conf /etc/supervisord.conf

# Create directories and set permissions
RUN mkdir -p /app/config /app/logs /app/data && \
    chown -R ddcuser:ddcuser /app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DDC_PLATFORM=windows \
    DDC_CONTAINER_TYPE=debian

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=45s --retries=3 \
    CMD curl -f http://localhost:9374/health || exit 1

# Switch to non-root user
USER ddcuser

# Expose ports
EXPOSE 9374

# Start application
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]