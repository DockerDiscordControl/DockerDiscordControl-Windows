# =============================================================================
# DDC Windows-Optimized Multi-Stage Debian Build
# Target: Optimized for Windows Docker Desktop with WSL2 backend
# Addresses all CVEs: CVE-2024-23334, CVE-2024-30251, CVE-2024-52304, 
# CVE-2024-52303, CVE-2025-47273, CVE-2024-6345, CVE-2024-47081, CVE-2024-37891
# =============================================================================

# Build stage - Minimal build environment
FROM python:3.12-slim AS builder
WORKDIR /build

# Install only essential build dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        make \
        libffi-dev \
        libssl-dev \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy only production requirements for optimal layer caching
COPY requirements-production.txt .

# Build wheels without any caching to minimize layer size
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip wheel --no-cache-dir --wheel-dir=/wheels -r requirements-production.txt && \
    # Verify security-critical packages are built
    ls -la /wheels/ | grep -E "(aiohttp|setuptools|requests|urllib3)" && \
    # Clean up pip cache immediately
    rm -rf /root/.cache /tmp/*

# =============================================================================
# Final stage - Windows-optimized runtime
FROM python:3.12-slim
WORKDIR /app

# Security and optimization environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONOPTIMIZE=2 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONPATH=/app \
    # Security: Disable unnecessary Python features
    PYTHONHASHSEED=random

# Install only absolutely essential runtime dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        supervisor \
        curl \
        wget \
        ca-certificates \
        tzdata && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user for security (Windows-compatible)
RUN groupadd -g 1000 ddc && \
    useradd -u 1000 -g ddc -s /bin/bash -m ddc

# Copy pre-built wheels and install them
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/*.whl && \
    rm -rf /wheels /root/.cache

# Copy optimized supervisor configuration
COPY supervisord-optimized.conf /etc/supervisor/conf.d/supervisord.conf

# Copy application code with proper ownership
COPY --chown=ddc:ddc . .

# Create necessary directories with proper permissions
RUN mkdir -p /app/config /app/logs && \
    chown -R ddc:ddc /app/config /app/logs && \
    chmod 755 /app/config /app/logs

# Health check for Docker and Kubernetes
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8374/health || exit 1

# Switch to non-root user
USER ddc

# Expose port
EXPOSE 8374

# Use supervisor to manage processes
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"] 