@echo off

echo Packaging code into executable...

REM Step 1: Build project with pyinstaller
pyinstaller --onefile --windowed --icon=ico/letsgo.ico main.py --name inhousetime --add-data "lib/;/"