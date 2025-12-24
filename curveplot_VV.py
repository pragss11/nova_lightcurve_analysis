# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:03:48 2025

@author: pragss
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# LOADING DATA
# ---------------------------------------------------------

file = 'D:\\V612_Sct\\Lightcurve\\V612_Sct_LC.txt'

x = np.loadtxt(file, delimiter=',', skiprows=1, dtype='<f8', usecols=[0])   # JD
z = np.loadtxt(file, delimiter=',', skiprows=1, dtype='<f8', usecols=[1])   # magnitude
err = 0.01 * z                                                              # simple error model
y = np.loadtxt(file, delimiter=',', skiprows=1, dtype='S15', usecols=[4])   # filter band

# Converting JD → days since peak (your chosen reference)
x = x - 2457964.488576

# ---------------------------------------------------------
# EXTRACTING V-BAND DATA
# ---------------------------------------------------------

Vx, V, Verr = [], [], []

for i in range(len(y)):
    if y[i] == b'V' and y[i+1] != b'i':   # avoid VI confusion
        V.append(float(z[i]))
        Vx.append(float(x[i]))
        Verr.append(err[i])

Vx = np.array(Vx)
V = np.array(V)
Verr = np.array(Verr)

# ---------------------------------------------------------
# COMPUTING PEAK, t2, t3
# ---------------------------------------------------------

# Peaking magnitude
V_peak = np.min(V)
peak_index = np.argmin(V)
t_peak = Vx[peak_index]

# Defining thresholds
V_t2 = V_peak + 2
V_t3 = V_peak + 3

mask_after_peak = Vx >= t_peak
V_after = V[mask_after_peak]
Vx_after = Vx[mask_after_peak]

# Finding t2 (first time V >= V_peak + 2 AFTER peak)
t2_candidates = Vx_after[V_after >= V_t2]
t2 = t2_candidates[0] if len(t2_candidates) > 0 else None

# Finding t3 (first time V >= V_peak + 3 AFTER peak)
t3_candidates = Vx_after[V_after >= V_t3]
t3 = t3_candidates[0] if len(t3_candidates) > 0 else None

print("Peak V magnitude =", V_peak)
print("t_peak =", t_peak)
print("t2 =", t2)
print("t3 =", t3)

# ---------------------------------------------------------
# PLOTTING
# ---------------------------------------------------------

plt.clf()
plt.close('all')

fig, ax = plt.subplots(figsize=(15, 9))
ax.invert_yaxis()

# Shading region for "Nova behind the Sun"
start_day = 122
end_day = 227
ax.axvspan(start_day, end_day, color='orange', alpha=0.3, label="Nova behind the Sun")

# Plotting V-band
ax.errorbar(Vx, V, yerr=Verr, color='green', fmt='*', markersize=8, label="$\it{V}$", alpha=0.8)

# Adding vertical lines for peak, t2, t3
ax.axvline(t_peak, color='black', linestyle='--', linewidth=1.5, label=f"Peak (V={V_peak:.2f})")

if t2 is not None:
    ax.axvline(t2, color='blue', linestyle='--', linewidth=1.5, label=f"$t_2$ = {t2:.1f} d")

if t3 is not None:
    ax.axvline(t3, color='red', linestyle='--', linewidth=1.5, label=f"$t_3$ = {t3:.1f} d")

# Annotating text
ax.text(t_peak + 3, V_peak + 0.2, f"Peak V={V_peak:.2f}", fontsize=14)

if t2 is not None:
    ax.text(t2 + 3, V_peak + 2.2, f"$t_2$={t2:.1f} d", fontsize=14, color='blue')

if t3 is not None:
    ax.text(t3 + 3, V_peak + 3.2, f"$t_3$={t3:.1f} d", fontsize=14, color='red')

# Axis formatting
plt.rcParams.update({'font.size': 20})
major_xticks = np.arange(-80, 500, 40)
minor_xticks = np.arange(-80, 500, 20)
ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor=True)

ax.tick_params(axis='both', which='major', labelsize=15, length=10, width=2)
ax.tick_params(axis='both', which='minor', labelsize=12, length=5, width=1)

ax.set_ylim(15.5, 6.5)
ax.set_xlim(-50, 500)

ax.legend(bbox_to_anchor=(0.99, 0.98), borderaxespad=0., loc='upper right')
ax.legend(numpoints=1)

plt.tick_params(width=3, length=8)
plt.tick_params(which='minor', width=2, length=4)

plt.xlabel('Day since peak brightness', fontsize=20)
plt.ylabel('Magnitude', fontsize=20)
plt.tight_layout()

plt.savefig('V612_Sct_LC_Vband_with_t2_t3.pdf')
plt.show()