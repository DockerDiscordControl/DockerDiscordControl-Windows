# DockerDiscordControl for Windows v2.0

[![Version](https://img.shields.io/badge/Version-v2.0.0-brightgreen?style=for-the-badge)](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/releases/tag/v2.0.0) [![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge)](https://python.org) [![Base Image](https://img.shields.io/badge/Base-Alpine%203.22.2-blueviolet?style=for-the-badge)](#ultra-optimized-alpine-image) [![Windows](https://img.shields.io/badge/Windows-10%20%2F%2011-0078D6?style=for-the-badge)](https://www.microsoft.com/windows)

> **Manage Docker containers through Discord - Windows Edition with WSL2 optimization**

Control your Docker environment directly from Discord with an intuitive web interface and powerful Discord bot. This is the **Windows-optimized version** of DockerDiscordControl v2.0, specifically designed for Docker Desktop on Windows 10/11 with WSL 2 backend.

**Main Repository:** [DockerDiscordControl](https://github.com/DockerDiscordControl/DockerDiscordControl) | **Homepage:** [https://ddc.bot](https://ddc.bot)

---

## 💖 **Support DDC Development**

**Help keep DockerDiscordControl growing and improving across all platforms!**

<div align="center">

[![Buy Me A Coffee](https://img.shields.io/badge/☕_Buy_Me_A_Coffee-Support_DDC-orange?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://buymeacoffee.com/dockerdiscordcontrol)
&nbsp;&nbsp;&nbsp;
[![PayPal Donation](https://img.shields.io/badge/💝_PayPal_Donation-Support_DDC-blue?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/dockerdiscordcontrol)

**Your support helps maintain DDC across Windows, Linux, macOS, and Universal versions!**

</div>

---

## Platform Selection

**DockerDiscordControl is available with platform-optimized versions!**

| Platform | Repository | Best For |
|----------|------------|----------|
| **Windows** | **[DockerDiscordControl-Windows](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows)** *(You are here)* | Windows 10/11 + Docker Desktop |
| **Linux** | **[DockerDiscordControl-Linux](https://github.com/DockerDiscordControl/DockerDiscordControl-Linux)** | Ubuntu, Debian, CentOS, RHEL |
| **macOS** | **[DockerDiscordControl-Mac](https://github.com/DockerDiscordControl/DockerDiscordControl-Mac)** | Apple Silicon & Intel Mac |
| **Universal** | **[DockerDiscordControl](https://github.com/DockerDiscordControl/DockerDiscordControl)** | Unraid, NAS, servers |

---

## v2.0.0 - MAJOR UPDATE - Complete Rewrite

### EVERYTHING via Discord - Complete Control

- **NEW:** Live Logs Viewer - Monitor container output in real-time directly in Discord
- **NEW:** Task System - Create, view, delete tasks (Once, Daily, Weekly, Monthly, Yearly) entirely in Discord
- **NEW:** Container Info System - Attach custom info and password-protected info to containers
- **NEW:** Public IP Display - Automatic WAN IP detection with custom port support
- Full container management without leaving Discord (start, stop, restart, bulk operations)

### Multi-Language Support

- **NEW:** Full Discord UI translation in German, French, and English
- Complete language coverage for all buttons, messages, and interactions
- Dynamic language switching via Web UI settings
- 100% translation coverage across entire bot interface

### Mech Evolution System

- **NEW:** 11-stage Mech Evolution with animated WebP graphics
- Continuous power decay system for fair donation tracking
- Premium key system for power users
- Visual feedback with stage-specific animations and particle effects

### Performance Improvements

- **IMPROVED:** 16x faster Docker status cache (500ms → 31ms)
- 7x faster container processing through async optimization
- Smart queue system with fair request processing
- Operation-specific timeout optimization

### Modern UI/UX Overhaul

- **IMPROVED:** Beautiful Discord embeds with consistent styling
- Advanced spam protection with configurable cooldowns
- Enhanced container information system
- Real-time monitoring and status updates

### Security & Optimization

- **IMPROVED:** Alpine Linux 3.22.2 base (94% fewer vulnerabilities)
- Ultra-compact image (<200MB RAM usage)
- Production-ready security hardening
- Enhanced token encryption and validation

### Critical Fixes

- **FIXED:** Intelligent Bot Retry Loop - Container stays running when Discord token is missing
- **FIXED:** Web-UI startup crash prevention - Graceful handling when Docker is unavailable
- **FIXED:** Auto-Cleanup - Automatically deactivates missing containers
- Interaction timeout issues with defer() pattern
- Container control reliability improvements

---

## Features - EVERYTHING via Discord

### Discord Container Control
- **Start, Stop, Restart** individual containers or **ALL containers at once**
- **Live Logs Viewer** - Monitor container output in real-time directly in Discord
- **Attach Custom Info** to containers (e.g., current WAN IP address, connection details)
- **Password-Protected Info** for secure data sharing within your Discord community
- **Container Status** monitoring with real-time updates

### Discord Task Scheduler
- **Create, view, and delete** automated tasks directly in Discord channels
- **Flexible Scheduling**: Once, Daily, Weekly, Monthly, Yearly
- **Full Task Management** - Complete control without leaving Discord
- **Timezone Configuration** for accurate scheduling across regions

### Flexible Permissions System
- **Status Channels**: All members see container status and public info
- **Status Channels**: Admin users get admin panel access for full control
- **Control Channels**: Everyone gets full admin access to all features
- **Granular Container Permissions**: Fine-grained control per container (Status, Start, Stop, Restart, Active visibility)
- **Hide Containers** from Discord or configure custom visibility per container
- **Password-Protected Info**: Viewable by anyone who knows the password
- **Spam Protection**: All Discord commands and button clicks protected by configurable cooldowns

### Web Interface
- **Secure Configuration Panel** with real-time monitoring
- **Container Management**: Configure permissions, custom info, and visibility
- **Task Management**: Create and manage scheduled tasks
- **Admin User Management**: Define who gets admin panel access in status channels
- **Security Audit**: Built-in security scoring and recommendations

### Customization & Localization
- **Multi-Language Support**: Full Discord UI in English, German, and French
- **Customizable Container Order**: Organize containers in your preferred display order
- **Mech Evolution System**: 11-stage evolution with animated graphics and premium keys
- **Custom Branding**: Configure container display names and information

### Performance & Optimization
- **16x Faster Docker Cache**: Optimized from 500ms to 31ms response time
- **7x Faster Processing**: Through async optimization and smart queue system
- **Alpine Linux 3.22.2**: 94% fewer vulnerabilities, less than 200MB RAM usage
- **Production Ready**: Supports 50 containers across 15 Discord channels
- **Intelligent Caching**: Background refresh for real-time data

---

## Quick Start

### Prerequisites

1. **Docker Desktop for Windows** with WSL 2 backend
   - [Download Docker Desktop](https://docs.docker.com/desktop/install/windows-install/)
   - Enable WSL 2 backend in Docker Desktop settings
   - Ensure WSL 2 integration is enabled for your distribution

2. **Discord Bot Token**
   - [Create a Discord Bot](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Discord‐Bot‐Setup)
   - Get your Bot Token and Guild (Server) ID

### Installation Methods

#### Method 1: Docker Compose (Recommended)

```bash
# Clone Windows-optimized repository
git clone https://github.com/DockerDiscordControl/DockerDiscordControl-Windows.git
cd DockerDiscordControl-Windows

# Create directories
mkdir config logs

# Create .env file with secure secret key
echo "FLASK_SECRET_KEY=$(openssl rand -hex 32)" > .env

# Start container
docker-compose up -d
```

#### Method 2: Docker Run

```bash
docker run -d \
  --name ddc-windows \
  -p 9374:9374 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ./config:/app/config \
  -v ./logs:/app/logs \
  -e FLASK_SECRET_KEY="$(openssl rand -hex 32)" \
  --restart unless-stopped \
  dockerdiscordcontrol/dockerdiscordcontrol-windows:latest
```

#### Method 3: Build from Source

```bash
git clone https://github.com/DockerDiscordControl/DockerDiscordControl-Windows.git
cd DockerDiscordControl-Windows
docker build -t ddc-windows:v2.0 .
docker-compose up -d
```

---

## First-Time Setup

**Easy Web Setup (Recommended)**

1. **Access Web UI**: `http://localhost:9374`

2. **Setup Options - Choose ONE method:**

   **Method 1: Guided Web Setup** (Easiest)
   - Visit: `http://localhost:9374/setup`
   - Follow the guided setup wizard
   - Create your admin password
   - Configure Discord bot token and Guild ID

   **Method 2: Temporary Credentials** (Quick Start)
   - Login with: `admin` / `setup`
   - **CRITICAL**: Change password immediately after first login!
   - Navigate to settings and configure bot token

   **Method 3: Environment Variable** (Most Secure)
   - Set `DDC_ADMIN_PASSWORD=your_secure_password` in `.env` file before starting
   - Start container with your custom password already configured

3. **Configure Bot Settings**:
   - Discord Bot Token (from Discord Developer Portal)
   - Discord Guild ID (your Discord server ID)
   - Container permissions and visibility
   - Language preference (EN, DE, FR)

4. **Restart Container**: `docker-compose restart` after initial configuration

**Security Warning**: Default password is `setup` for initial access. You **MUST** change this immediately after first login for security! For production deployments, set `DDC_ADMIN_PASSWORD` before first start.

**Password Security**: All passwords are hashed with PBKDF2-SHA256 (600,000 iterations) for maximum security.

---

## Configuration

### Environment Variables

#### Security & Authentication

```bash
# Option 1: Set admin password before first start (Recommended)
DDC_ADMIN_PASSWORD=your_secure_password_here

# Option 2: Use temporary credentials for web setup
# Visit http://localhost:9374 and login with: admin / setup
# Then change password immediately through the web interface

# Flask security (auto-generated if not provided)
FLASK_SECRET_KEY=your-64-character-random-secret-key
```

#### Discord Configuration

```bash
# Discord Bot Settings (configured via Web UI or environment)
DISCORD_BOT_TOKEN=your_discord_bot_token_here
DISCORD_GUILD_ID=your_discord_server_id_here
```

#### Performance Optimization

```bash
# Docker Cache Settings
DDC_MAX_CACHED_CONTAINERS=100          # Maximum containers in cache (default: 100)
DDC_DOCKER_CACHE_DURATION=45           # Cache duration in seconds (default: 45)
DDC_ENABLE_BACKGROUND_REFRESH=true     # Enable background cache refresh (default: true)

# Bot Retry Settings (Windows-specific)
DDC_TOKEN_RETRY_INTERVAL=60            # Retry interval in seconds (default: 60)
DDC_TOKEN_MAX_RETRIES=0                # Max retries, 0 = infinite (default: 0)

# Web Server Settings
GUNICORN_WORKERS=1                     # Number of workers (default: 1 for Discord Bot)
GUNICORN_TIMEOUT=45                    # Request timeout in seconds (default: 45)

# Logging
LOG_LEVEL=INFO                         # Logging level (DEBUG, INFO, WARNING, ERROR)
TZ=America/New_York                    # Timezone (default: UTC)
```

### Web-UI Configuration

1. Navigate to `http://localhost:9374`
2. Login with your credentials (see First-Time Setup above)
3. Configure:
   - Discord bot token and Guild ID
   - Container permissions and visibility
   - Admin users for status channels
   - Language preference (EN, DE, FR)
   - Task scheduling
   - Custom container information
   - Password-protected info

---

## Windows-Specific Notes

### Docker Desktop Requirements

**WSL 2 Backend (Required)**
- Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11
- WSL 2 installed and enabled
- Docker Desktop configured to use WSL 2 backend
- Enable WSL 2 integration for your distribution

**File Sharing**
- Ensure config and logs directories are accessible to Docker
- WSL 2 handles volume sharing automatically

**Resource Limits**
- Adjust CPU and memory limits in Docker Desktop settings if needed
- Recommended: 2 CPU cores, 2GB RAM minimum

### Volume Paths

On Windows with WSL 2, use **Linux-style paths** in docker-compose.yml:

```yaml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock
  - ./config:/app/config
  - ./logs:/app/logs
```

**Do NOT use Windows paths** like `C:\Users\...` - let WSL 2 handle the translation.

### Networking

- **Default Port**: `9374` (Web-UI)
- **Firewall**: Ensure Windows Firewall allows Docker Desktop
- **WSL 2 Networking**: Automatic, no manual configuration needed
- **Access**: `http://localhost:9374` from Windows host

### Docker Socket Permissions

**Windows/WSL 2 Specifics:**
- Docker socket GID is typically `281` (docker group)
- **NO `--group-add 0` flag needed** (only required on macOS)
- User `ddc` (UID 1000) is automatically added to docker group in container
- WSL 2 handles socket permissions automatically

### Common Windows Issues

**Container won't start:**
- Check Docker Desktop is running
- Verify WSL 2 backend is enabled in Docker Desktop settings
- Ensure WSL 2 integration is enabled for your distribution
- Check Docker socket is accessible: `docker ps`

**Permission errors:**
- Restart Docker Desktop
- Verify WSL 2 integration is enabled
- Check file permissions on config/logs directories

**Web-UI not accessible:**
- Check port 9374 is not in use: `netstat -ano | findstr :9374`
- Verify Windows Firewall settings
- Check container is running: `docker ps`
- Access using `http://localhost:9374` (not IP address)

---

## System Requirements

### Minimum Requirements
- **CPU**: 1 core (1.5 cores recommended)
- **RAM**: 150MB (200MB limit, <200MB typical usage)
- **Storage**: 100MB for application + config/logs space
- **OS**: Windows 10 (Build 19041+) or Windows 11
- **Docker**: Docker Desktop 4.0+ with WSL 2 backend

### Production Limits
- **Maximum Containers**: 50 Docker containers
- **Maximum Channels**: 15 Discord channels
- **Concurrent Operations**: 10 pending Docker actions
- **Cache Size**: 50 status entries with intelligent cleanup

---

## Troubleshooting

### First-Time Setup Issues

**Can't Login:**
- Visit `/setup` for guided setup
- Use temporary credentials: `admin` / `setup`
- Set `DDC_ADMIN_PASSWORD` environment variable

**"Authentication Required" Error:**
- Use default credentials: `admin` / `setup`
- Visit `/setup` to create new password
- Check `DDC_ADMIN_PASSWORD` environment variable

**Password Reset:**
```bash
docker exec -it ddc-windows python3 scripts/reset_password.py
```

### Configuration Issues

**Configuration Not Saving:**
- Check file permissions: `docker exec ddc-windows ls -la /app/config`
- Run permission fix: `docker exec ddc-windows /app/scripts/fix_permissions.sh`
- Check logs: `docker logs ddc-windows`

**Bot Not Responding:**
- Verify Discord bot token in Web UI
- Check Guild ID is correct
- Verify bot has proper permissions in Discord
- Check logs: `docker logs ddc-windows | grep -i "bot\|discord\|token"`

### Docker Socket Issues

**"Cannot access Docker daemon":**
- Restart Docker Desktop
- Verify WSL 2 backend is enabled
- Check Docker socket exists: `docker exec ddc-windows ls -la /var/run/docker.sock`
- Verify container can access Docker:
  ```bash
  docker exec ddc-windows python3 -c "import docker; docker.from_env().ping()"
  ```

### Performance Issues

**High Memory Usage:**
- Reduce `DDC_MAX_CACHED_CONTAINERS`
- Reduce `GUNICORN_WORKERS` to 1
- Check for container leaks: `docker stats`

**Slow Response Times:**
- Increase `DDC_DOCKER_CACHE_DURATION`
- Enable `DDC_ENABLE_BACKGROUND_REFRESH=true`
- Check Docker Desktop resource limits

---

## Docker Images

**Ultra-optimized Alpine Linux image:**
- **Size**: 176MB with multi-stage build optimization
- **Base**: Alpine Linux 3.22.2 (latest secure version)
- **Architecture**: Service-oriented modular design (v2.0)
- **Security**: Latest dependencies with all CVEs fixed
- **Performance**: Optimized for minimal resource usage and fast startup

```bash
docker pull dockerdiscordcontrol/dockerdiscordcontrol-windows:latest
```

---

## Security Notice

**Docker Socket Access Required**: This application requires access to `/var/run/docker.sock` to control containers. Only run in trusted environments and ensure proper host security.

**First-Time Setup Required**: DDC v2.0+ uses temporary default password `setup` for initial access. Use one of these secure setup methods:
- **Web Setup**: Visit `/setup` and create your password
- **Temporary Access**: Login with `admin` / `setup`, then set real password
- **Environment Variable**: Set `DDC_ADMIN_PASSWORD` before starting container

**Password Security**: All passwords are hashed with PBKDF2-SHA256 (600,000 iterations) for maximum security.

---

## Quick Help

**Common Issues:**

```bash
# View logs
docker logs ddc-windows

# Check container status
docker ps | grep ddc-windows

# Restart container
docker-compose restart

# Fix permissions
docker exec ddc-windows /app/scripts/fix_permissions.sh

# Reset password
docker exec -it ddc-windows python3 scripts/reset_password.py

# Access Web UI
http://localhost:9374
```

**Need Help?**
- Check [Troubleshooting Guide](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Troubleshooting)
- Create an issue: [GitHub Issues](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/issues)
- Join discussions: [GitHub Discussions](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/discussions)

---

## Documentation

| Topic | Link |
|-------|------|
| **Installation Guide** | [Wiki - Installation](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Installation‐Guide) |
| **Configuration** | [Wiki - Configuration](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Configuration) |
| **Discord Bot Setup** | [Wiki - Bot Setup](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Discord‐Bot‐Setup) |
| **Task System** | [Wiki - Tasks](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Task‐System) |
| **Performance** | [Wiki - Performance](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Performance‐and‐Architecture) |
| **Security** | [Wiki - Security](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Security) |
| **Troubleshooting** | [Wiki - Troubleshooting](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Troubleshooting) |

---

## Contributing

We welcome contributions! See our [Contributing Guide](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki/Development) for setup instructions and coding standards.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Support & Links

**Like DDC? Star the repository!** | **Found a bug?** [Report it](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/issues) | **Feature idea?** [Suggest it](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/discussions)

**Other Platforms:**
- **[Main Repository](https://github.com/DockerDiscordControl/DockerDiscordControl)** - Universal version (Unraid, NAS, servers)
- **[Linux Version](https://github.com/DockerDiscordControl/DockerDiscordControl-Linux)** - Native Linux optimization
- **[macOS Version](https://github.com/DockerDiscordControl/DockerDiscordControl-Mac)** - Apple Silicon & Intel Mac

---

## 🌟 **Show Your Support**

If DockerDiscordControl helps you manage your Windows containers, please consider supporting the project:

<div align="center">

### **💖 Support DDC Development**

[![⭐ Star on GitHub](https://img.shields.io/badge/⭐_Star_on_GitHub-Show_Support-brightgreen?style=for-the-badge&logo=github)](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows)

[![☕ Buy Me A Coffee](https://img.shields.io/badge/☕_Buy_Me_A_Coffee-orange?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://buymeacoffee.com/dockerdiscordcontrol)
&nbsp;&nbsp;
[![💝 PayPal Donation](https://img.shields.io/badge/💝_PayPal_Donation-blue?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/dockerdiscordcontrol)

**Your support helps maintain DDC across all platforms and develop new features!**

</div>

---

**Windows v2.0.0** | Built for Windows 10/11 with Docker Desktop WSL 2 optimization

**🪟 Built with ❤️ for Windows Docker Desktop users**

**⭐ Star this repo if DockerDiscordControl helps you manage your Windows containers!**
