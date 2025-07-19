# DockerDiscordControl for Windows - Quick Start

Get up and running in 5 minutes!

## Prerequisites
- Windows 10/11 with Docker Desktop
- Git for Windows
- Discord bot token

## Quick Installation
```powershell
git clone https://github.com/DockerDiscordControl/DockerDiscordControl-Windows.git
cd DockerDiscordControl-Windows
copy env.template .env
notepad .env  # Add your Discord bot token
docker-compose up --build -d
start http://localhost:8374
```

## Discord Setup
1. Go to https://discord.com/developers/applications
2. Create application → Add bot → Copy token
3. Add token to .env file
4. Add bot to your Discord server

Login: admin/admin (change immediately!)
