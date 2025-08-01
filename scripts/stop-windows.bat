@echo off
REM DockerDiscordControl Windows Stop Script

echo 🪟 Stopping DockerDiscordControl...
echo ====================================

docker-compose down

if %ERRORLEVEL% EQU 0 (
    echo ✅ DockerDiscordControl stopped successfully!
) else (
    echo ❌ Error stopping DockerDiscordControl
)

echo.
pause