# DockerDiscordControl Windows Installation Script
# PowerShell script for Windows-specific installation

param(
    [switch]$Service,
    [switch]$TaskScheduler,
    [string]$InstallPath = "$env:ProgramFiles\DockerDiscordControl"
)

Write-Host "🪟 DockerDiscordControl Windows Installer" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green

# Check if running as administrator
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "❌ This script requires administrator privileges." -ForegroundColor Red
    Write-Host "Please run PowerShell as Administrator and try again." -ForegroundColor Yellow
    exit 1
}

# Check Docker Desktop installation
Write-Host "🐳 Checking Docker Desktop..." -ForegroundColor Cyan
try {
    $dockerVersion = docker --version
    Write-Host "✅ Docker found: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker Desktop not found. Please install Docker Desktop first." -ForegroundColor Red
    Write-Host "Run: winget install Docker.DockerDesktop" -ForegroundColor Yellow
    exit 1
}

# Create installation directory
Write-Host "📁 Creating installation directory..." -ForegroundColor Cyan
New-Item -ItemType Directory -Path $InstallPath -Force | Out-Null

# Copy files
Write-Host "📦 Copying application files..." -ForegroundColor Cyan
Copy-Item -Path ".\*" -Destination $InstallPath -Recurse -Force

# Create Windows service if requested
if ($Service) {
    Write-Host "🔧 Installing as Windows Service..." -ForegroundColor Cyan
    
    $serviceName = "DockerDiscordControl"
    $serviceDisplayName = "Docker Discord Control"
    $serviceDescription = "Discord bot for Docker container management"
    $pythonPath = (Get-Command python).Source
    $servicePath = "$InstallPath\bot.py"
    
    # Install service using NSSM or native Windows service
    Write-Host "⚠️  Windows Service installation requires additional setup." -ForegroundColor Yellow
    Write-Host "Please use Task Scheduler option for easier deployment." -ForegroundColor Yellow
}

# Create Task Scheduler entry if requested
if ($TaskScheduler) {
    Write-Host "⏰ Creating Task Scheduler entry..." -ForegroundColor Cyan
    
    $taskName = "DockerDiscordControl"
    $pythonPath = (Get-Command python).Source
    $scriptPath = "$InstallPath\bot.py"
    
    $action = New-ScheduledTaskAction -Execute $pythonPath -Argument $scriptPath -WorkingDirectory $InstallPath
    $trigger = New-ScheduledTaskTrigger -AtStartup
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
    $principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
    
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force
    
    Write-Host "✅ Task Scheduler entry created: $taskName" -ForegroundColor Green
}

Write-Host ""
Write-Host "🎉 Installation completed!" -ForegroundColor Green
Write-Host "Installation path: $InstallPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Configure your Discord bot token in config/bot_config.json"
Write-Host "2. Start the application with: docker-compose up -d"
Write-Host "3. Access Web UI at: http://localhost:9374"
Write-Host ""
Write-Host "For more information, see INSTALL_WINDOWS.md" -ForegroundColor Cyan