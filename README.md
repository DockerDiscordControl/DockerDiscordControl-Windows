# DockerDiscordControl for Windows 🪟

Control your Docker containers directly from Discord on Windows! This Windows-native version provides a Discord bot and web interface specifically optimized for **Windows systems** with **Docker Desktop integration** and **WSL2 compatibility**.

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

**Homepage:** [DDC for Windows](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows) | **Main Project:** [DockerDiscordControl](https://github.com/DockerDiscordControl/DockerDiscordControl)

[![Version](https://img.shields.io/badge/version-v1.1.2-blue.svg)](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/DockerDiscordControl/DockerDiscordControl-Windows/blob/main/LICENSE)
[![Windows Optimized](https://img.shields.io/badge/Windows-Docker_Desktop-blue.svg)](#performance-metrics)
[![Multi-Architecture](https://img.shields.io/badge/Arch-Intel_AMD_x64-orange.svg)](#installation)
[![Memory Optimized](https://img.shields.io/badge/RAM-~100MB-green.svg)](#performance-metrics)

## 🚀 Revolutionary Windows Performance

**Major Windows-Specific Optimizations Delivered:**

- **Docker Desktop Integration**: Native WSL2 backend support with 100MB typical RAM usage
- **Windows Container Support**: Future-ready for Windows container workloads  
- **Desktop Optimization**: System tray integration and Windows service support (planned)
- **PowerShell Integration**: Native Windows management scripts included
- **Debian Multi-Stage Build**: Optimized Debian-based image for Windows environments

## 🐳 Docker Hub Repository

**Windows-Optimized Image:** \`dockerdiscordcontrol/dockerdiscordcontrol-windows\`

This repository publishes **only** the Windows-optimized Debian-based image, specifically tuned for:
- Windows Docker Desktop integration and WSL2 compatibility
- Optimal resource usage on Windows desktop systems
- Native Windows Docker socket handling
- Multi-stage build for reduced image size and improved security

**Other Platform Images:**
- **Universal/Unraid**: \`dockerdiscordcontrol/dockerdiscordcontrol\`
- **Linux**: \`dockerdiscordcontrol/dockerdiscordcontrol-linux\`  
- **macOS**: \`dockerdiscordcontrol/dockerdiscordcontrol-mac\`

## 🛠️ Quick Installation

### **Docker Hub Installation (Recommended)**
\`\`\`powershell
# Pull the Windows-optimized image
docker pull dockerdiscordcontrol/dockerdiscordcontrol-windows:latest

# Run with docker compose
docker compose up -d

# Or run directly
docker run -d --name ddc \`
  -p 8374:8374 \`
  -v /var/run/docker.sock:/var/run/docker.sock \`
  -v \${PWD}/config:/app/config \`
  -v \${PWD}/logs:/app/logs \`
  dockerdiscordcontrol/dockerdiscordcontrol-windows:latest
\`\`\`

## 🔧 Configuration

1. **Access the Web Interface**: \`http://localhost:8374\`
2. **Default Login**: \`admin\` / \`admin\` (change immediately!)
3. **Configure Discord Bot**: Add your bot token and guild ID
4. **Set Docker Settings**: Configure container refresh intervals
5. **Channel Permissions**: Set up Discord channel access controls

## 🆕 Latest Updates (v1.1.2)

### **✅ Critical ConfigManager Stability Fixes**
- **Fixed ConfigManager**: Resolved missing attributes and cache invalidation issues
- **Eliminated CPU spikes**: Fixed restart loops that caused high CPU usage
- **Enhanced error handling**: Improved subscriber notification system
- **System stability**: Eliminated config cache reload loops

### **✅ Windows Docker Desktop Optimizations**
- **Multi-stage Debian build**: Converted to multi-stage build for smaller, more secure images
- **Resource optimization**: ~100MB RAM usage with minimal CPU impact
- **Health monitoring**: Added \`/health\` endpoint for proper Docker health checks  
- **WSL2 efficiency**: Optimized for Windows Subsystem for Linux v2 backend

**🎉 Ready for production deployment on any Windows Docker Desktop environment!**

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

**🪟 Built with ❤️ for Windows Docker Desktop users**

**🚀 Perfect for Windows desktops, home labs, and development environments!** 

**⭐ Star this repo if DockerDiscordControl helps you manage your Windows containers!**
