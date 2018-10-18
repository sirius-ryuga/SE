import os
path=str(os.getcwd())+"\Env"
if os.path.exists(path):
        os.system(r'start.bat')
else:
        os.system(r'prepare.bat')
        os.system(r'start.bat')
