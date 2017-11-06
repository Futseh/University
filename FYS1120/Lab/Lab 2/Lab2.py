import numpy as np
import matplotlib.pyplot as plt

S1 = [-1869, -1693, -1579, -1476, -1693]
S2 = [-2318, -2318, -2359, -2333, -2607]

I1 = [0.48, 0.95, 1.70, 2.47, 3.51]
I2 = [-0.63, -1.11, -2.08, -3.05, -4.37]

H = []
B = []
M = []

Imaks = 0
Smaks = 0

k = 1.01 * 10**(-6)
D = 20
N = 667
n = 100
R2 = 1.16 * 10**(-2)
r2 = 8.6 * 10**(-3)
my = 4 * np.pi * 10**(-7)

A = np.pi * (r2 / 2.0)**2

Br = (k * D * np.sqrt((-1907 + 2332)**2)) / (2 * n * A)

for i in range(5):
    Imaks = (np.sqrt(I1[i]**2) + np.sqrt(I2[i]**2)) / 2.0
    Smaks = np.sqrt((S1[i] - S2[i])**2)
    
    H.append((N * Imaks) / (2 * np.pi * (R2 / 2.0)))
    B.append((k * D * Smaks) / (2 * n * A))
    M.append((B[i] / my) - H[i])

print Br

plt.plot(H, M)
plt.title("Plot av M(H, B)")
plt.xlabel("H-Felt")
plt.ylabel("M-Felt")
plt.show()

"""
Terminal> python Lab2.py
    0.738964405865
"""