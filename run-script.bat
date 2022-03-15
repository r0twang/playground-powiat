@echo off 
CALL c:\Working\python-gym\PowiatWarBot\venv\Scripts\activate.bat 
FOR /L %%A IN (1,1,800) DO (
	python c:\Working\python-gym\playground-powiat\main.py %*
	echo.
)
pause