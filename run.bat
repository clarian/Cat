@echo off
SET root=%~dp0
CD /D %root%
SETLOCAL EnableDelayedExpansion
python -V >nul 2>&1 || goto :python
git init . >nul || goto :git
git remote add origin https://github.com/clarian/Cat.git >nul 2>&1
get fetch origin master >nul 2>&1
findstr %findtext% %findfile% >nul 2>&1		
if errorlevel 1 goto forward		
goto run		

:prompt
	choice /t 10 /c yn /d n /m "There is an update for the bot. Download now?, note that by saying yes, you're restoring all your changes"
	if errorlevel 2 goto :run
	if errorlevel 1 goto :update
:forward
	set findfile="tmp.txt"		
	set forwardable="fast-forwardable"		
	findstr %forwardable% %findfile% >nul 2>&1		
	if errorlevel 1 goto prompt
	goto run
:update
	echo Starting update...
	echo Latest update:
	git --no-pager log --pretty=oneline -n1 origin/master ^master
	git pull origin master
	if errorlevel 1 goto force
	echo Finished updating
	echo Starting up...
	ping 127.0.0.1 -n 4 >nul
	goto run
:force
	git fetch --all
	git reset --hard origin/master
	echo Finished updating
	echo Starting up...
	ping 127.0.0.1 -n 4 >nul
	goto run
:git
	TITLE Error!
	echo Git not found, Download here: https://git-scm.com/downloads
	echo Press any key to exit.
	pause >nul
	CD /D "%root%"
	goto :EOF
:python
	TITLE Error!
	echo Python not added to PATH or not installed. Download Python 3.5.2 or above and make sure you add to PATH: https://i.imgur.com/KXgMcOK.png
	echo Press any key to exit.
	pause >nul
	CD /D "%root%"
	goto :EOF
:run
	if exist tmp.txt del tmp.txt
	echo[
	echo[
	FOR /f %%p in ('where python') do SET PYTHONPATH=%%p
	echo Checking requirements...
	echo Requirements satisfied.
	echo Starting the bot (this may take a minute or two)...
	python bot.py
	if %ERRORLEVEL% == 15 goto update