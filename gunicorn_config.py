# Gunicorn Configuration - Windows/WSL2 Optimized
# Optimized for Windows Docker Desktop and WSL2 environments

import multiprocessing
import os

# Server socket - Windows Docker Desktop optimized
bind = "0.0.0.0:9374"  # Bind to all interfaces for Docker Desktop containers
backlog = 1024  # Windows: Moderate backlog for Docker Desktop

# Worker processes - Windows Docker Desktop optimization
workers = max(2, min(3, multiprocessing.cpu_count()))  # Conservative scaling for Windows
worker_class = "sync"  # Sync worker class works best for DDC workload
worker_connections = 500  # Moderate connections per worker for Windows
max_requests = 800  # Restart workers after 800 requests to prevent memory leaks  
max_requests_jitter = 40  # Add jitter to worker restarts

# Timeout settings - Windows Docker Desktop optimized
timeout = 45  # 45 second timeout for Windows environments
keepalive = 3  # Keep connections alive for 3 seconds
graceful_timeout = 25  # Graceful shutdown timeout

# Logging - Windows Docker Desktop optimized paths
loglevel = os.getenv("LOG_LEVEL", "info").lower()
accesslog = "/app/logs/gunicorn_access.log"  # Windows: Standard app log path
errorlog = "/app/logs/gunicorn_error.log"   # Windows: Standard app log path
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "ddc-windows-web"

# Security and performance
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Preload application for better memory usage
preload_app = True

# Process management
pidfile = "/app/logs/gunicorn.pid"
user = 1000  # Run as ddc user (UID 1000)
group = 1000  # Run as ddc group (GID 1000)

# Windows/WSL2-specific optimizations
worker_tmp_dir = "/tmp"  # Use /tmp for Windows Docker Desktop compatibility

def when_ready(server):
    """Called when the server is ready to receive requests"""
    server.log.info("DockerDiscordControl Windows Web Interface ready on %s", bind)

def worker_int(worker):
    """Called when a worker receives the INT signal"""
    worker.log.info("Worker %s interrupted", worker.pid)

def post_fork(server, worker):
    """Called after worker process is forked"""
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def post_worker_init(worker):
    """Called after worker process initialization"""  
    worker.log.info("Worker %s initialized", worker.pid)

def worker_abort(worker):
    """Called when worker process is aborted"""
    worker.log.warning("Worker %s aborted", worker.pid) 