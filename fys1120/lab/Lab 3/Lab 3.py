import numpy as np
import matplotlib.pyplot as plt

B = [6.00, 36.0, 63.0, 89.0, 115., 139.]    # mT
I = [0.00, 0.10, 0.20, 0.30, 0.40, 0.50]    # A
Vh = [1.6, 5.2, 9.0, 12.9, 16.8, 20.4]      # mV

p = np.polyfit(B, Vh, 1)
n = np.polyval(p, B)

print("Stigningstallet til grafen er: %.4f og \
konstanten hvor Vh(B) = 0 er: %.4f" % (p[0], p[1]))

plt.scatter(B, Vh)
plt.xlabel("B [mT]")
plt.ylabel("Vh [mV]")
plt.title("Vh(B) for p-Ge")
plt.plot(B, n, color="red")
plt.show()

"""
Terminal> python Lab3.py
    Stigningstallet til grafen er: 0.1428 og konstanten hvor Vh(B) = 0 er: 0.3206
"""