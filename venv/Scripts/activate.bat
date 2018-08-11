@echo off
<<<<<<< HEAD
set "VIRTUAL_ENV=D:\PycharmProjects\Practice2\venv"
=======
<<<<<<< HEAD
set "VIRTUAL_ENV=D:\PycharmProjects\Practice\venv"
=======
<<<<<<< HEAD
set "VIRTUAL_ENV=C:\Users\LAKSHYAJIT LAXMIKANT\PycharmProjects\venv"
=======
set "VIRTUAL_ENV=G:\Pycharm Projects\python_prac\venv"
>>>>>>> da640fa0050c6ca621a2f80c0cb8fb0a44ac2b3f
>>>>>>> bf9ec1b50b9a105f9d7e270e398763a0ccb4d098
>>>>>>> 3fd2e0bf3056c187a4af3d5a6e8bb83949d7212a

if not defined PROMPT (
    set "PROMPT=$P$G"
)

if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
)

if defined _OLD_VIRTUAL_PYTHONHOME (
    set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"
)

set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
set "PROMPT=(venv) %PROMPT%"

if defined PYTHONHOME (
    set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
    set PYTHONHOME=
)

if defined _OLD_VIRTUAL_PATH (
    set "PATH=%_OLD_VIRTUAL_PATH%"
) else (
    set "_OLD_VIRTUAL_PATH=%PATH%"
)

set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

:END
