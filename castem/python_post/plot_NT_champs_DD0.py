#!/usr/bin/env python

import math
import numpy as np
import matplotlib.pyplot as plt
import glob as glob

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fics = sorted(glob.glob("*/*/*/*_evolution_max.csv"))

# print(fics)

NT_ = ['NT10', 'NT4', 'NT2']

for item in NT_:
    id_plot = [item]

# maximum plastic deformation :
    fig = plt.figure()
    ax1 = plt.subplot()
    ax1.set_xlim(0, 0.25)
    ax1.set_ylim(0, 0.8)
    plt.title(item)
    plt.xlabel(r'$\Delta D/D_0  (mm/mm)$', fontsize=16)
    plt.ylabel(r'$\epsilon_p$', fontsize=16)
    for fic in fics:
        dat = np.genfromtxt(fic)
        name = fic.split('/')[1]
        elem, NT, post, file = fic.split('/')
        id_f, phi = name.split('_')
        print(name, id_f)
        if id_f not in id_plot:
            continue
        ax1.plot(dat[:, 0], dat[:, 1], '-', linewidth=1,
             label=r"\small %s" % (elem))
    ax1.legend(loc='best')
    plt.savefig(item + '_p_DD0.pdf', bbox_inches='tight')
    plt.show()

# maximum VMIS :
    fig = plt.figure()
    ax1 = plt.subplot()
    ax1.set_xlim(0, 0.25)
    ax1.set_ylim(0, 350)
    plt.title(item)
    plt.xlabel(r'$\Delta D/D_0  (mm/mm)$', fontsize=16)
    plt.ylabel(r'$\sigma_{VM} (MPa)$', fontsize=16)
    for fic in fics:
        dat = np.genfromtxt(fic)
        name = fic.split('/')[1]
        elem, NT, post, file = fic.split('/')
        id_f, phi = name.split('_')
        print(name, id_f)
        if id_f not in id_plot:
            continue
        ax1.plot(dat[:, 2], dat[:, 3], '-', linewidth=1,
             label=r"\small %s" % (elem))
    ax1.legend(loc='best')
    plt.savefig(item + '_VMIS_DD0.pdf', bbox_inches='tight')
    plt.show()

# maximum stress triaxiality :
    fig = plt.figure()
    ax1 = plt.subplot()
    ax1.set_xlim(0, 0.25)
    ax1.set_ylim(0, 3)
    plt.title(item)
    plt.xlabel(r'$\Delta D/D_0  (mm/mm)$', fontsize=16)
    plt.ylabel(r'$\frac{\sigma_m}{\sigma_{VM}}$', fontsize=16)
    for fic in fics:
        dat = np.genfromtxt(fic)
        name = fic.split('/')[1]
        elem, NT, post, file = fic.split('/')
        id_f, phi = name.split('_')
        print(name, id_f)
        if id_f not in id_plot:
            continue
        ax1.plot(dat[:, 4], dat[:, 5], '-', linewidth=1,
             label=r"\small %s" % (elem))
    ax1.legend(loc='best')
    plt.savefig(item + '_triax_DD0.pdf', bbox_inches='tight')
    plt.show()

# maximum porosity :
    fig = plt.figure()
    ax1 = plt.subplot()
    ax1.set_xlim(0, 0.25)
    ax1.set_ylim(0, 0.07)
    plt.title(item)
    plt.xlabel(r'$\Delta D/D_0  (mm/mm)$', fontsize=16)
    plt.ylabel(r'$Porosity$', fontsize=16)

    for fic in fics:
        dat = np.genfromtxt(fic)
        name = fic.split('/')[1]
        elem, NT, post, file = fic.split('/')
        id_f, phi = name.split('_')
        print(name, id_f)
        if id_f not in id_plot:
            continue
        try:
            ax1.plot(dat[:, 6], dat[:, 7], '-', linewidth=1,
             label=r"\small %s" % (elem))
        except IndexError as e:
            print(f"simulation without damage ?")
    ax1.legend(loc='best')
    plt.savefig(item + '_f_DD0.pdf', bbox_inches='tight')
    plt.show()
