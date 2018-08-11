function global:deactivate ([switch]$NonDestructive) {
    # Revert to original values
    if (Test-Path function:_OLD_VIRTUAL_PROMPT) {
        copy-item function:_OLD_VIRTUAL_PROMPT function:prompt
        remove-item function:_OLD_VIRTUAL_PROMPT
    }

    if (Test-Path env:_OLD_VIRTUAL_PYTHONHOME) {
        copy-item env:_OLD_VIRTUAL_PYTHONHOME env:PYTHONHOME
        remove-item env:_OLD_VIRTUAL_PYTHONHOME
    }

    if (Test-Path env:_OLD_VIRTUAL_PATH) {
        copy-item env:_OLD_VIRTUAL_PATH env:PATH
        remove-item env:_OLD_VIRTUAL_PATH
    }

    if (Test-Path env:VIRTUAL_ENV) {
        remove-item env:VIRTUAL_ENV
    }

    if (!$NonDestructive) {
        # Self destruct!
        remove-item function:deactivate
    }
}

deactivate -nondestructive

<<<<<<< HEAD
$env:VIRTUAL_ENV="D:\PycharmProjects\Practice2\venv"
=======
<<<<<<< HEAD
$env:VIRTUAL_ENV="D:\PycharmProjects\Practice\venv"
=======
<<<<<<< HEAD
$env:VIRTUAL_ENV="C:\Users\LAKSHYAJIT LAXMIKANT\PycharmProjects\venv"
=======
$env:VIRTUAL_ENV="G:\Pycharm Projects\python_prac\venv"
>>>>>>> da640fa0050c6ca621a2f80c0cb8fb0a44ac2b3f
>>>>>>> bf9ec1b50b9a105f9d7e270e398763a0ccb4d098
>>>>>>> 3fd2e0bf3056c187a4af3d5a6e8bb83949d7212a

if (! $env:VIRTUAL_ENV_DISABLE_PROMPT) {
    # Set the prompt to include the env name
    # Make sure _OLD_VIRTUAL_PROMPT is global
    function global:_OLD_VIRTUAL_PROMPT {""}
    copy-item function:prompt function:_OLD_VIRTUAL_PROMPT
    function global:prompt {
        Write-Host -NoNewline -ForegroundColor Green '(venv) '
        _OLD_VIRTUAL_PROMPT
    }
}

# Clear PYTHONHOME
if (Test-Path env:PYTHONHOME) {
    copy-item env:PYTHONHOME env:_OLD_VIRTUAL_PYTHONHOME
    remove-item env:PYTHONHOME
}

# Add the venv to the PATH
copy-item env:PATH env:_OLD_VIRTUAL_PATH
$env:PATH = "$env:VIRTUAL_ENV\Scripts;$env:PATH"
