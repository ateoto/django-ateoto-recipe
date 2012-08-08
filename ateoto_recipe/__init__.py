import subprocess

version = '0.0.2'

try:
    version = subprocess.check_output(['git','log','-1','--pretty="%h"']).strip('\"\n')
except:
    pass

__version__ = version
