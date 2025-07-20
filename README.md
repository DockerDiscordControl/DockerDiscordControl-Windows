# DockerDiscordControl - Windows Edition

[![Docker Hub](https://img.shields.io/docker/v/dockerdiscordcontrol/dockerdiscordcontrol-windows?label=docker%20hub)](https://hub.docker.com/r/dockerdiscordcontrol/dockerdiscordcontrol-windows)
[![Docker Pulls](https://img.shields.io/docker/pulls/dockerdiscordcontrol/dockerdiscordcontrol-windows)](https://hub.docker.com/r/dockerdiscordcontrol/dockerdiscordcontrol-windows)
[![Image Size](https://img.shields.io/docker/image-size/dockerdiscordcontrol/dockerdiscordcontrol-windows/latest)](https://hub.docker.com/r/dockerdiscordcontrol/dockerdiscordcontrol-windows)

**Control your Docker containers directly from Discord on Windows!**

DockerDiscordControl-Windows is a specialized version optimized for Windows environments, allowing you to manage Docker containers through Discord bot commands with enhanced Windows-specific features and compatibility.

**🌐 Homepage: [https://ddc.bot](https://ddc.bot)**

## 🚀 Quick Start

### Using Docker Hub

```bash
# Pull the latest Windows-optimized image
docker pull dockerdiscordcontrol/dockerdiscordcontrol-windows:latest

# Run with Docker Compose
docker-compose up -d
```

### Using Docker Run

```bash
docker run -d \
  --name dockerdiscordcontrol-windows \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v ./config:/app/config \
  -e DISCORD_BOT_TOKEN=your_bot_token_here \
  -e ALLOWED_CHANNELS=channel_id_1,channel_id_2 \
  -e ALLOWED_ROLES=role_id_1,role_id_2 \
  -p 8080:8080 \
  dockerdiscordcontrol/dockerdiscordcontrol-windows:latest
```

## ✨ Windows-Specific Features

- **Enhanced Windows Container Support**: Optimized for both Linux and Windows containers
- **Windows Service Integration**: Built-in support for Windows service management
- **PowerShell Commands**: Native PowerShell script execution support
- **Windows Authentication**: Integration with Windows authentication systems
- **WSL2 Compatibility**: Seamless operation with Docker Desktop on WSL2

## 🏗️ Architecture

This Windows-optimized version includes:

- **Debian Slim Base**: Lightweight and secure foundation
- **Python 3.13**: Latest Python runtime with Windows optimizations
- **Supervisor**: Process management with Windows-specific configurations
- **Multi-Architecture**: Supports both AMD64 and ARM64 platforms

## 📋 Requirements

### System Requirements
- **Docker Desktop for Windows** 4.0+ with WSL2 backend
- **Windows 10/11** (64-bit) or **Windows Server 2019/2022**
- **Memory**: Minimum 512MB RAM (1GB+ recommended)
- **Storage**: 500MB+ free disk space

### Discord Requirements
- Discord bot token with necessary permissions
- Guild/server with appropriate permissions
- Channel IDs for command execution

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DISCORD_BOT_TOKEN` | Your Discord bot token | ✅ Yes | - |
| `ALLOWED_CHANNELS` | Comma-separated channel IDs | ✅ Yes | - |
| `ALLOWED_ROLES` | Comma-separated role IDs | ✅ Yes | - |
| `LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | ❌ No | `INFO` |
| `WEB_UI_PORT` | Web interface port | ❌ No | `8080` |
| `MAX_CONTAINERS` | Maximum containers to manage | ❌ No | `50` |
| `COMMAND_TIMEOUT` | Command execution timeout (seconds) | ❌ No | `30` |

### Docker Compose Example

```yaml
version: '3.8'
services:
  dockerdiscordcontrol:
    image: dockerdiscordcontrol/dockerdiscordcontrol-windows:latest
    container_name: dockerdiscordcontrol-windows
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./config:/app/config
      - ./logs:/app/logs
    environment:
      - DISCORD_BOT_TOKEN=${DISCORD_BOT_TOKEN}
      - ALLOWED_CHANNELS=${ALLOWED_CHANNELS}
      - ALLOWED_ROLES=${ALLOWED_ROLES}
      - LOG_LEVEL=INFO
    ports:
      - "8080:8080"
    networks:
      - dockerdiscordcontrol
    labels:
      - "com.dockerdiscordcontrol.version=1.0.4"
      - "com.dockerdiscordcontrol.platform=windows"

networks:
  dockerdiscordcontrol:
    driver: bridge
```

## 🎮 Discord Commands

### Container Management
- `/docker ps` - List running containers
- `/docker start <container>` - Start a container
- `/docker stop <container>` - Stop a container
- `/docker restart <container>` - Restart a container
- `/docker logs <container>` - View container logs
- `/docker stats` - Show container statistics

### System Information
- `/system info` - Display system information
- `/system resources` - Show resource usage
- `/docker version` - Docker version information

### Advanced Commands
- `/compose up <service>` - Start Docker Compose services
- `/compose down` - Stop Docker Compose services
- `/network ls` - List Docker networks
- `/volume ls` - List Docker volumes

## 🌐 Web Interface

Access the web interface at `http://localhost:8080` for:

- **Real-time Container Monitoring**: Live status and metrics
- **Configuration Management**: Easy setup and configuration
- **Log Viewer**: Centralized log management
- **Task Scheduler**: Automated container operations
- **User Management**: Role and permission configuration

## 🔒 Security Features

### Built-in Security
- **Role-based Access Control**: Discord role verification
- **Channel Restrictions**: Limit commands to specific channels
- **Command Auditing**: Full audit trail of all commands
- **Rate Limiting**: Prevention of command spam
- **Input Validation**: Sanitized command parameters

### Best Practices
- Use non-root user inside container
- Read-only Docker socket mounting
- Environment-based configuration
- Regular security updates
- Network isolation

## 🔍 Monitoring & Logging

### Log Levels
- **DEBUG**: Detailed debugging information
- **INFO**: General operational messages
- **WARNING**: Warning messages for attention
- **ERROR**: Error conditions

### Health Checks
The container includes built-in health checks:

```bash
# Check container health
docker inspect --format='{{.State.Health.Status}}' dockerdiscordcontrol-windows

# View health check logs
docker inspect dockerdiscordcontrol-windows | grep -A5 Health
```

## 🛠️ Troubleshooting

### Common Issues

#### Bot Not Responding
```bash
# Check bot token and permissions
docker logs dockerdiscordcontrol-windows --tail 50

# Verify Discord connectivity
docker exec dockerdiscordcontrol-windows python -c "import discord; print('Discord.py version:', discord.__version__)"
```

#### Docker Socket Issues
```bash
# Verify Docker socket permissions
ls -la /var/run/docker.sock

# Test Docker connectivity
docker exec dockerdiscordcontrol-windows docker version
```

#### Windows-Specific Issues
- Ensure Docker Desktop is running with WSL2 backend
- Verify Windows container support if using Windows containers
- Check Windows Firewall settings for port 8080

### Performance Optimization
- Adjust `MAX_CONTAINERS` based on system resources
- Use specific tags instead of `latest` for production
- Enable Docker Compose for complex deployments
- Monitor container resource usage

## 📦 Tags & Versions

| Tag | Description | Architecture |
|-----|-------------|--------------|
| `latest` | Latest stable release | `linux/amd64`, `linux/arm64` |
| `1.0.4` | Version 1.0.4 | `linux/amd64`, `linux/arm64` |
| `1.0.3` | Version 1.0.3 | `linux/amd64`, `linux/arm64` |
| `debian` | Debian-based image | `linux/amd64`, `linux/arm64` |
| `alpine` | Alpine-based image | `linux/amd64`, `linux/arm64` |

## 🤝 Support

### Documentation
- **🌐 Official Homepage**: [https://ddc.bot](https://ddc.bot)
- **Main Repository (Unraid)**: [DockerDiscordControl](https://github.com/DockerDiscordControl/DockerDiscordControl)
- **Windows Repository**: [DockerDiscordControl-Windows](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows)
- **Installation Guide**: [Windows Setup Instructions](https://github.com/DockerDiscordControl/DockerDiscordControl/blob/main/INSTALL_WINDOWS.md)
- **Wiki**: [Comprehensive Documentation](https://github.com/DockerDiscordControl/DockerDiscordControl/wiki)

### Community
- **Discord Server**: Join our community for support
- **GitHub Issues**: Report bugs and feature requests
- **GitHub Discussions**: Community Q&A and discussions

### Professional Support
For enterprise support and custom implementations, please contact our team through GitHub.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/DockerDiscordControl/DockerDiscordControl/blob/main/LICENSE) file for details.

## 🎉 Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/DockerDiscordControl/DockerDiscordControl/blob/main/CONTRIBUTING.md) for details.

## 💝 Support DDC Development

Help keep DockerDiscordControl growing and improving for Windows Docker Desktop users:

- **[☕ Buy Me A Coffee](https://buymeacoffee.com/dockerdiscordcontrol)** - Quick one-time support for development
- **[💳 PayPal Donation](https://www.paypal.com/donate/?hosted_button_id=XKVC6SFXU2GW4)** - Direct contribution to the project

**Your support helps:**
- 🛠️ Maintain DDC for Windows with latest Docker Desktop compatibility
- ✨ Develop new Windows-specific features and optimizations  
- 🔒 Keep DockerDiscordControl zero-vulnerability secure for Windows environments
- 📚 Create comprehensive Windows documentation and guides
- 🚀 Performance optimizations for Windows Docker Desktop users

**Thank you for supporting open source development!** 🙏

---

**Made with ❤️ for the Windows Docker community**

[![GitHub](https://img.shields.io/badge/GitHub-DockerDiscordControl-blue?logo=github)](https://github.com/DockerDiscordControl)
[![Docker Hub](https://img.shields.io/badge/Docker%20Hub-dockerdiscordcontrol-blue?logo=docker)](https://hub.docker.com/u/dockerdiscordcontrol)
