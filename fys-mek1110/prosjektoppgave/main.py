import numpy as np
import matplotlib.pyplot as plt

def U(r):
    epsilon = 1
    sigma = 1

    part = (sigma / r)**12 - (sigma / r)**6
    return 4 * epsilon * part

distance = np.linspace(-4, 4, 10000)
potential = U(distance)

plt.plot(distance, potential)
plt.ylim(bottom=-1, top=1)
plt.grid()
plt.show()