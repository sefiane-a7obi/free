@echo off
title SEFIANE STORE Il2Cpp Dumper
echo ====================================================
echo Starting SEFIANE STORE Il2Cpp Dumper Server...
echo Engine: SEFIANE STORE Dumper (Free Fire + Unity OB55)
echo Open your browser at: http://localhost:8000
echo ====================================================
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000 ^| findstr LISTENING') do taskkill /f /pid %%a >nul 2>&1
python server.py
pause
