#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt
import glob as glob

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fics = sorted(glob.glob("*/*/*/*_evolution.csv"))
ficsexp = sorted(glob.glob("*/*/*/*.res+"))

# print(ficsexp)
# print(fics)

NT_ = ['NT10', 'NT4', 'NT2']

for item in NT_:
    id_plot = [item]
    
    fig = plt.figure()
    ax1 = plt.subplot()
    ax1.set_xlim(0, 0.25)
    ax1.set_ylim(0, 500)
    plt.xlabel(r'$\Delta D/D_0  (mm/mm)$', fontsize=16)
    plt.ylabel(r'$F/S_0 (MPa)$', fontsize=16)

    for fic in fics:
        dat = np.genfromtxt(fic)
        name = fic.split('/')[1]
        elem, NT, post, filee = fic.split('/')
        id_f, phi = name.split('_')
        print(name, id_f)
        if id_f not in id_plot:
            continue
        ax1.plot(dat[:, 2], dat[:, 1], '--', marker='.', linewidth=1,
             markersize=4, label=r"\small %s" % (elem))

    for fic in ficsexp:
        dat = np.genfromtxt(fic)
        name = fic.split('/')[1]
        elem, NT, post, filee = fic.split('/')
        id_f, phi = name.split('_')
        print(name, id_f)
        if id_f not in id_plot:
            continue
        exp, = ax1.plot(dat[:, 0], dat[:, 1], '-k')

    exp.set_label('experimental')
    ax1.legend(loc='best')
    plt.savefig(item + '_FS0_DD0.pdf', bbox_inches='tight')
    plt.show()
