<<<<<<< HEAD
#!"C:\Users\LAKSHYAJIT LAXMIKANT\PycharmProjects\venv\Scripts\python.exe"
=======
#!"G:\Pycharm Projects\python_prac\venv\Scripts\python.exe"
>>>>>>> da640fa0050c6ca621a2f80c0cb8fb0a44ac2b3f
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==9.0.1','console_scripts','pip3.6'
__requires__ = 'pip==9.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==9.0.1', 'console_scripts', 'pip3.6')()
    )
