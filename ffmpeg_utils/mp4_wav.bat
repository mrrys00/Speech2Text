@REM @echo off
echo %1 will be converted to %2
ffmpeg -i %1 %2
echo SUCCESS