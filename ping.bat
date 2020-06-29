@ECHO OFF
@SETLOCAL

::Set the address you wish to ping
SET adress=155.133.232.98

::Set the speed between pings (In seconds)
SET speed=2

GOTO :ping

:ping
::Ping and extract time= into variable
for /F "tokens=7 delims== " %%G in ('ping -4 -n 1 %adress%^|findstr /i "time="') do set ping=%%G
echo Current ping for %adress%: %ping%


::Wait for x second before next ping
PING localhost -n %speed% >NUL

goto :ping