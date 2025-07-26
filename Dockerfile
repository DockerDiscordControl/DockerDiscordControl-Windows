# =============================================================================
# DDC Ultra-Optimized Multi-Stage Alpine Build
# Target: <100MB final image size with full functionality and security
# Addresses all CVEs: CVE-2024-23334, CVE-2024-30251, CVE-2024-52304, 
# CVE-2024-52303, CVE-2025-47273, CVE-2024-6345, CVE-2024-47081, CVE-2024-37891
# =============================================================================

# Build stage - Minimal build environment
FROM python:3.12-alpine AS builder
WORKDIR /build

# Install only essential build dependencies
RUN apk update && apk upgrade && \
    apk add --no-cache --virtual .build-deps \
        gcc g++ musl-dev python3-dev libffi-dev openssl-dev make && \
    rm -rf /var/cache/apk/*

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
# Final stage - Ultra-minimal runtime (targeting <100MB)
FROM python:3.12-alpine
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
RUN apk update && apk upgrade && \
    apk add --no-cache \
        supervisor \
        docker-cli \
        openssl \
        ca-certificates \
        tzdata \
        curl && \
    # Aggressive cleanup
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/* /usr/share/man/* /usr/share/doc/*

# Install pre-built wheels (no compilers or build tools needed)
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && \
    # Immediate cleanup of wheels and pip cache
    rm -rf /wheels /root/.cache /tmp/* && \
    # Verify security packages are installed correctly
    python -c "import aiohttp, setuptools, requests, urllib3; print('Security packages verified')"

# Security: Create non-root user and docker group for runtime
RUN addgroup -g 997 -S docker && \
    addgroup -g 1000 -S ddcuser && \
    adduser -u 1000 -S ddcuser -G ddcuser && \
    adduser ddcuser docker

# Install dumb-init and su-exec in the final stage
RUN apk add --no-cache dumb-init su-exec

# Copy application code (optimized via .dockerignore)
COPY . .

# Copy optimized supervisor configuration for non-root user
COPY supervisord-optimized.conf /etc/supervisor/conf.d/supervisord.conf

# Create necessary directories and set permissions BEFORE switching user
RUN mkdir -p /app/config /app/logs && \
    chown -R ddcuser:ddcuser /app/config && \
    # Logs directory needs to be writable by root (for supervisord.log) and ddcuser (for app logs)
    chown -R root:ddcuser /app/logs && \
    chmod -R 775 /app/logs

# Security hardening and size optimization
RUN mkdir -p /app/config /app/logs && \
    chown -R ddcuser:ddcuser /app /app/config /app/logs && \
    # Remove unnecessary files to minimize image size
    find /app -name "*.pyc" -delete && \
    find /app -name "__pycache__" -type d -exec rm -rf {} + && \
    find /app -name "*.md" -delete && \
    find /app -name "Dockerfile*" -delete && \
    find /app -name "docker-compose*" -delete && \
    find /app -name "*.log" -delete && \
    find /app -name ".git*" -delete && \
    # Remove unnecessary Python standard library test modules
    find /usr/local/lib/python3.12 -name "test" -type d -exec rm -rf {} + && \
    find /usr/local/lib/python3.12 -name "tests" -type d -exec rm -rf {} + && \
    find /usr/local/lib/python3.12 -name "*.pyo" -delete && \
    # Compile Python files for faster startup
    python -m compileall -b /app 2>/dev/null || true && \
    # Security: Remove setuid binaries
    find /usr -perm +6000 -type f -exec chmod a-s {} \; && \
    # Final cleanup
    rm -rf /tmp/* /var/tmp/* /root/.cache

# PROOF THAT THIS DOCKERFILE IS BEING USED
RUN echo "Build successful with the CORRECT Dockerfile from $(date)" > /BUILD_PROOF.txt

# Security: Health check with minimal overhead
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:9374/ || exit 1

# Expose only necessary port
EXPOSE 9374

# Create necessary directories
RUN mkdir -p /app/config /app/logs && \
    chown -R ddcuser:ddcuser /app

# Security: Use dumb-init and run supervisord as root
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"] 