# DockerDiscordControl for Windows v2.0

> **Manage Docker containers through Discord commands - Windows Edition**

Control your Docker environment directly from Discord with an intuitive web interface and powerful Discord bot commands. This is the **Windows-optimized version** of DockerDiscordControl v2.0.

## Features

### v2.0 New Features
- **Live Logs Viewer**: Real-time container log streaming in the Web-UI
- **Task System**: Schedule tasks (Once, Daily, Weekly, Monthly, Yearly)
- **Container Info**: Password-protected detailed container information
- **Multi-language Support**: English, German, French
- **Mech Evolution System**: 11-stage mech progression with XP and fuel
- **16x Faster Docker Cache**: Optimized from 500ms to 31ms response times
- **Intelligent Bot Retry Loop**: Container stays running when Discord token is missing
- **Auto-Cleanup**: Automatically deactivates missing containers

### Core Features
- Start, stop, restart, and remove Docker containers via Discord
- Real-time container status monitoring
- Beautiful web UI for configuration and management
- Secure password authentication
- Resource usage tracking (CPU, Memory, Network)
- Container logs viewing
- Automated scheduled tasks
- Discord embed messages with rich formatting

## Quick Start

### Prerequisites
- **Docker Desktop for Windows** with WSL 2 backend
- Discord Bot Token ([Create one here](https://discord.com/developers/applications))

### Method 1: Docker Compose (Recommended)

1. Clone this repository:
```bash
git clone https://github.com/DockerDiscordControl/DockerDiscordControl-Windows.git
cd DockerDiscordControl-Windows
```

2. Create a `.env` file:
```bash
# Required
DISCORD_BOT_TOKEN=your_bot_token_here
DISCORD_GUILD_ID=your_guild_id_here
FLASK_SECRET_KEY=your_random_secret_key

# Optional
TZ=America/New_York
LOG_LEVEL=INFO
```

3. Start the container:
```bash
docker-compose up -d
```

4. Access the Web-UI at `http://localhost:9374`

### Method 2: Docker Run

```bash
docker run -d \
  --name ddc-windows \
  -p 9374:9374 \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v ./config:/app/config \
  -v ./logs:/app/logs \
  -e DISCORD_BOT_TOKEN="your_bot_token" \
  -e DISCORD_GUILD_ID="your_guild_id" \
  -e FLASK_SECRET_KEY="your_secret_key" \
  dockerdiscordcontrol/dockerdiscordcontrol-windows:latest
```

### Method 3: Build from Source

```bash
git clone https://github.com/DockerDiscordControl/DockerDiscordControl-Windows.git
cd DockerDiscordControl-Windows
docker build -t ddc-windows:v2.0 .
docker-compose up -d
```

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DISCORD_BOT_TOKEN` | Yes | - | Your Discord bot token |
| `DISCORD_GUILD_ID` | Yes | - | Your Discord server ID |
| `FLASK_SECRET_KEY` | Yes | - | Secret key for web sessions |
| `TZ` | No | UTC | Timezone (e.g., America/New_York) |
| `LOG_LEVEL` | No | INFO | Logging level (DEBUG, INFO, WARNING, ERROR) |
| `DDC_TOKEN_RETRY_INTERVAL` | No | 60 | Bot retry interval in seconds |
| `DDC_TOKEN_MAX_RETRIES` | No | 0 | Max retries (0 = infinite) |

### Web-UI Configuration
1. Navigate to `http://localhost:9374`
2. Log in with default credentials (set via web interface)
3. Configure Discord bot settings
4. Set up container monitoring preferences
5. Create scheduled tasks

## Discord Commands

### Container Management
- `/start <container>` - Start a container
- `/stop <container>` - Stop a container
- `/restart <container>` - Restart a container
- `/remove <container>` - Remove a container
- `/status [container]` - Show container status

### Information
- `/list` - List all containers
- `/logs <container>` - View container logs
- `/stats <container>` - Show resource usage

### Tasks & Automation
- `/task create` - Create a new scheduled task
- `/task list` - List all tasks
- `/task delete <id>` - Delete a task

## Windows-Specific Notes

### Docker Desktop Requirements
- **WSL 2 Backend**: Required for best performance
- **File Sharing**: Ensure config and logs directories are shared
- **Resource Limits**: Adjust in Docker Desktop settings if needed

### Volume Paths
On Windows with WSL 2, use Linux-style paths:
```yaml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock:ro
  - ./config:/app/config
  - ./logs:/app/logs
```

### Networking
- Default port: `9374` (Web-UI)
- Ensure Windows Firewall allows Docker Desktop
- WSL 2 networking is automatic

## Troubleshooting

### Container won't start
- Check Docker Desktop is running
- Verify WSL 2 backend is enabled
- Check Docker socket permissions

### Bot not connecting
- Verify Discord token is correct
- Check bot has proper permissions
- View logs: `docker logs ddc-windows`

### Web-UI not accessible
- Check port 9374 is not in use
- Verify firewall settings
- Check container is running: `docker ps`

### Docker socket permission errors
- Restart Docker Desktop
- Verify WSL 2 integration is enabled
- Check user is in docker group (in WSL)

## Support

- **Documentation**: Check the `wiki/` directory
- **Issues**: [GitHub Issues](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/issues)
- **Discussions**: [GitHub Discussions](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/discussions)

## Security

- Change default passwords immediately
- Use strong `FLASK_SECRET_KEY`
- Keep Discord token secure
- Regularly update the container
- Review container permissions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Developed for the Docker and Discord communities. Special thanks to all contributors!

---

**Windows v2.0** | [Main Repo](https://github.com/DockerDiscordControl/DockerDiscordControl) | [Mac Version](https://github.com/DockerDiscordControl/DockerDiscordControl-Mac) | [Linux Version](https://github.com/DockerDiscordControl/DockerDiscordControl-Linux)
