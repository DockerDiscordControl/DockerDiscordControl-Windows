@echo off
REM DockerDiscordControl Windows Startup Script
REM Batch file for easy Windows deployment

echo 🪟 DockerDiscordControl for Windows
echo ====================================

REM Check if Docker is running
docker info >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Docker is not running. Please start Docker Desktop first.
    echo.
    echo Starting Docker Desktop...
    start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    echo Waiting for Docker to start...
    timeout /t 10 /nobreak >nul
)

REM Start the application
echo 🚀 Starting DockerDiscordControl...
docker-compose up -d --build

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ DockerDiscordControl started successfully!
    echo.
    echo 🌐 Web UI: http://localhost:9374
    echo 📚 Documentation: See README.md
    echo.
) else (
    echo.
    echo ❌ Failed to start DockerDiscordControl
    echo Check the logs with: docker-compose logs
    echo.
)

pause