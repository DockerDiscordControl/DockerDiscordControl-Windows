# DockerDiscordControl for Windows 🪟

Control your Docker containers directly from Discord on Windows! This Windows-native version provides a Discord bot and web interface specifically built for **Windows systems** with **Docker Desktop integration** and **desktop-optimized performance**.

## ✨ Features
- Discord Bot: Full slash command interface for container management
- Web Interface: Secure configuration panel with real-time monitoring
- Container Control: Start, stop, restart any Docker container from Discord
- Windows Native: Optimized for Windows Docker Desktop environments

## 🚀 Performance Metrics
- Memory Usage: ~90MB typical usage (optimized for Windows Docker Desktop)
- CPU Usage: <5% on quad-core system during normal operation
- Container Startup: ~20-30 seconds on Windows Docker Desktop

## 📋 System Requirements
- OS: Windows 10 Pro/Enterprise (version 1903+) or Windows 11
- Architecture: Intel/AMD 64-bit (x64)
- RAM: 4GB minimum (8GB+ recommended)
- Docker: Docker Desktop 4.0+ with WSL2 backend enabled

## 🛠️ Quick Installation

```powershell
# Install Docker Desktop
winget install Docker.DockerDesktop

# Clone repository
git clone https://github.com/DockerDiscordControl/DockerDiscordControl-Windows.git
cd DockerDiscordControl-Windows

# Setup environment
copy env.template .env
notepad .env  # Add your Discord bot token

# Start application
docker-compose up --build -d

# Access web interface
start http://localhost:8374
```

## 📚 Documentation
- [Quick Start](QUICK_START.md): Fast deployment guide
- [Installation](INSTALL_WINDOWS.md): Detailed Windows setup
- [Troubleshooting](TROUBLESHOOTING.md): Common issues

Built with ❤️ for Windows Docker Desktop users 🪟🐳
