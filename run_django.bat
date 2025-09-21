@echo off
set PYTHONPATH=%~dp0venv\Lib\site-packages
%~dp0venv\Scripts\python.exe manage.py %*
