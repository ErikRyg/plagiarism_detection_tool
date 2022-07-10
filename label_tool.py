import os
import subprocess
file = './data/tmp1.c'
try:
    subprocess.call([os.environ['EDITOR'], file])
except:
    try:
        subprocess.call(['gedit', file])
    except:
        subprocess.call(['nano', file])