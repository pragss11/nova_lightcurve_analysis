# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 10:49:24 2025

@author: pragss
"""

import numpy as np
import matplotlib.pyplot as plt

# Loading data
x = np.loadtxt('D:\\V612_Sct\\Lightcurve\\V612_Sct_LC.txt', delimiter=',', skiprows=1, dtype='<f8', usecols=[0])
z = np.loadtxt('D:\\V612_Sct\\Lightcurve\\V612_Sct_LC.txt', delimiter=',', skiprows=1, dtype='<f8', usecols=[1])
err = 0.01 * z
y = np.loadtxt('D:\\V612_Sct\\Lightcurve\\V612_Sct_LC.txt', delimiter=',', skiprows=1, dtype='S15', usecols=[4])

x = x - 2457964.488576



nV = 1279
nCV = 245
nVis = 718
nB = 825
nR = 144
nI = 607

V = [0 for V in range(nV)]
Vx = [0 for Vx in range(nV)]
Verr = [0 for Verr in range(nV)]



CV = [0 for CV in range(nCV)]
CVx = [0 for CVx in range(nCV)]
CVerr = [0 for CVerr in range(nCV)]

Vis = [0 for Vis in range(nVis)]
Visx = [0 for Visx in range(nVis)]
Viserr = [0 for Viserr in range(nVis)]

B = [0 for B in range(nB)]
Bx = [0 for Bx in range(nB)]
Berr = [0 for Berr in range(nB)]

I = [0 for I in range(nI)]
Ix = [0 for Ix in range(nI)]
Ierr = [0 for Ierr in range(nI)]

R = [0 for R in range(nR)]
Rx = [0 for Rx in range(nR)]
Rerr = [0 for Rerr in range(nR)]

i2, b, v, r, j, h, k = 0, 0, 0, 0, 0, 0, 0
a = len(y)

for i in range(len(y)):
    if y[i] == b'V':
        if y[i + 1] == b'i':
            Vis[v], Visx[v], Viserr[v] = float(z[i]), float(x[i]), err[i]
            v += 1
        else:
            V[j], Vx[j], Verr[j] = float(z[i]), float(x[i]), err[i]
            j += 1
    elif y[i] == b'I':
        I[i2], Ix[i2], Ierr[i2] = float(z[i]), float(x[i]), err[i]
        i2 += 1
    elif y[i] == b'C':
        CV[h], CVx[h], CVerr[h] = float(z[i]), float(x[i]), err[i]
        h += 1
    elif y[i] == b'R':
        R[r], Rx[r], Rerr[r] = float(z[i]), float(x[i]), err[i]
        r += 1
    elif y[i] == b'B':
        B[b], Bx[b], Berr[b] = float(z[i]), float(x[i]), err[i]
        b += 1

plt.clf()
plt.close('all')

fig, ax = plt.subplots(figsize=(15, 9))
ax.invert_yaxis()

ax.errorbar(Ix, I, yerr=Ierr, color='red', fmt='o', markersize=7, label="$\it{I}$", alpha=0.8)
ax.errorbar(Rx, R, yerr=Rerr, color='magenta', fmt='s', markersize=7, label="$\it{R}$", alpha=0.8)
ax.errorbar(Bx, B, yerr=Berr, color='blue', fmt='^', markersize=7, label="$\it{B}$", alpha=0.8)
ax.errorbar(Vx, V, yerr=Verr, color='green', fmt='*', markersize=8, label="$\it{V}$", alpha=0.8)
ax.errorbar(CVx, CV, yerr=CVerr, fmt='gs', markersize=5, rasterized=True)
ax.errorbar(Visx, Vis, yerr=Viserr, fmt='kd', markersize=5, label="Vis.", rasterized=True)

plt.rcParams.update({'font.size': 20})
major_xticks = np.arange(-80, 500, 40) 
minor_xticks = np.arange(-80, 500, 20)
ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True)
 # Set Y-axis limits and labels
ax.tick_params(axis='both', which='major', labelsize=15, length=10, width=2)
ax.tick_params(axis='both', which='minor', labelsize=12, length=5, width=1)
 
ax.set_ylim(15.5, 6.5)
#ax.set_xlim(-50, 130) 
ax.set_xlim(-50, 500) 
ax.legend(bbox_to_anchor=(0.99, 0.98), borderaxespad=0., loc='upper right')
ax.legend(numpoints=1)
plt.tick_params(width=3, length=8) 
plt.tick_params(which='minor', width=2, length=4) 

# Adding vertical lines at x = 0, 50, 70, 90
ax.axvline(x=0, color='black', linestyle='--', linewidth=1.5, label='x=0')
ax.axvline(x=48, color='black', linestyle='--', linewidth=1.5, label='x=50')
ax.axvline(x=68, color='black', linestyle='--', linewidth=1.5, label='x=70')
ax.axvline(x=87, color='black', linestyle='--', linewidth=1.5, label='x=90')
ax.axvline(x=111, color='black', linestyle='--', linewidth=1.5, label='x=90')

# Adding horizontal lines at the specified y-values
'''ax.axhline(y=8.45, color='gray', linestyle='--', linewidth=1.5, label='y=9.5')
ax.axhline(y=10.05, color='gray', linestyle='--', linewidth=1.5, label='y=10.2')
ax.axhline(y=9.7, color='gray', linestyle='--', linewidth=1.5, label='y=10.9')
ax.axhline(y=9.2, color='gray', linestyle='--', linewidth=1.5, label='y=9.9')
'''
 
 
plt.xlabel('Day since peak brightness', fontsize=20)
plt.ylabel('Magnitude', fontsize=20)
plt.tight_layout()
#plt.savefig('V612_Sct_LC_zoom.pdf')
#plt.savefig('V612_Sct_LC_complete.pdf')
plt.show()