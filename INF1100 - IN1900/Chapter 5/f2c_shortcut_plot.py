# Exercise 5.12

import numpy as np
import matplotlib.pyplot as plt

def approx_f2c(F):
    Ca = (F - 30) / 2.
    return Ca

def exact_f2c(F):
    Ce = (F - 32) * (5 / 9.)
    return Ce

Flist = np.linspace(-20, 120, 141)

ax = plt.subplot(111)

ax.plot(Flist, approx_f2c(Flist))
ax.plot(Flist, exact_f2c(Flist))

ax.set_xlabel('Fahrenheit')
ax.set_ylabel('Celsius')

plt.legend(['Shortcut F2C', 'Exact F2C'])

plt.show()

"""
Terminal> python f2c:shortcut_plot.py

"""
