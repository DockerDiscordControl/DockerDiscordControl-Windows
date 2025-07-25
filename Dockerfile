# Multi-Stage Build for a smaller and more secure final image
# --- Builder Stage ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build-time dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt


# --- Final Stage ---
FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    wget \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -g 1000 ddc && \
    useradd -u 1000 -g ddc -s /bin/bash -m ddc

# Copy Python packages from builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# Copy application code
COPY . .

# Create directories and set permissions
RUN mkdir -p /app/config /app/logs /app/data && \
    chown -R ddc:ddc /app

# Configure supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

USER ddc

EXPOSE 8374 9374

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:9374/health || exit 1

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf", "-n"]
