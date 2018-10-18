# coding: utf8

import os
import sys

path=str(os.getcwd())+"\Env"
if os.path.exists(path):
        os.system(r'start.bat')
else:
        filecont='"'+sys.exec_prefix+"\python.exe"+'"'+" -m venv %CD%\Env && %CD%\Env\Scripts"+"\\"+"activate.bat"
        filecont+=" && python -m pip install --upgrade pip && pip install chardet && @echo All components installed && @pause"
        file=open('prepare.bat', 'w')
        file.write(filecont)
        file.close()
        os.system(r'prepare.bat')
        os.system(r'start.bat')
