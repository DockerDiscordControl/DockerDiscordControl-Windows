# DockerDiscordControl for Windows - Installation Guide

Complete step-by-step installation guide for Windows systems with Docker Desktop.

## Prerequisites
- Windows 10 Pro/Enterprise (version 1903+) or Windows 11
- Intel/AMD 64-bit (x64)
- 4GB RAM minimum (8GB+ recommended)
- Docker Desktop 4.0+ with WSL2 backend

## Installation Steps

### 1. Install Docker Desktop
```powershell
winget install Docker.DockerDesktop
```

### 2. Clone Repository
```powershell
git clone https://github.com/DockerDiscordControl/DockerDiscordControl-Windows.git
cd DockerDiscordControl-Windows
```

### 3. Configure Environment
```powershell
copy env.template .env
notepad .env
```

Add your Discord bot token and server ID to the .env file.

### 4. Start Application
```powershell
docker-compose up --build -d
```

### 5. Access Web Interface
Open http://localhost:8374 in your browser.
Default login: admin/admin (change immediately!)

## Discord Bot Setup
1. Go to Discord Developer Portal
2. Create application and bot
3. Copy bot token to .env file
4. Add bot to your Discord server

For detailed troubleshooting, see TROUBLESHOOTING.md
