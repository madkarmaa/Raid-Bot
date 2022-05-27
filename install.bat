@echo off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)
git clone https://github.com/madkarmaa/Raid-Bot.git
call :colorEcho 0a "Repository successfully cloned"
echo.
cd Raid-Bot
pip install -r requirements.txt
call :colorEcho 0a "Requirements successfully installed. Press any key to run the bot"
echo.
pause >nul
python bot.py
:colorEcho
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1i