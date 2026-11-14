@echo off
pushd "%~dp0"

set PYTHONWARNINGS=default
set PYTHONPYCACHEPREFIX=out\pycache
set UNIVERSALFLASHCARDSDEV=1
set QTWEBENGINE_REMOTE_DEBUGGING=8080
set QTWEBENGINE_CHROMIUM_FLAGS=--remote-allow-origins=https://chrome-devtools-frontend.appspot.com,http://localhost:8080
set UNIVERSALFLASHCARDS_API_PORT=40000
set UNIVERSALFLASHCARDS_API_HOST=127.0.0.1

@if not defined PYENV set PYENV=out\pyenv
  
call tools\ninja pylib qt || exit /b 1
%PYENV%\Scripts\python tools\run.py %* || exit /b 1
popd
