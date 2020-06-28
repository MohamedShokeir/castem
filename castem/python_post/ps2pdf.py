#!/usr/bin/env python

import math
import subprocess
import os
import glob as glob
import itertools
from pathlib import Path

local = Path.cwd()

fics = set()
champs = ('P', 'TRIAXIALITY', 'VMIS', 'POROSITY')
for champ in champs:
    args = "*/*/*/" + champ + "_*.ps"
    fics.update(glob.glob(args))
#ficss = sorted(fics)
#print(ficss)

#for fich in itertools.chain(fics):
#    print(fich)

for fich in fics:
    elem, NT, post, filee = fich.split('/')
    go_path = "/".join((elem, NT, post))
    path = Path(go_path)
    #print(path)
    os.chdir(path)
    command = 'ps2pdf ' + filee
    print(f"processing : {NT, elem} {command}")
    subprocess.call(command, shell=True)
    os.chdir(local)
      

