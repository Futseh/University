# Exercise 5.28

from numpy import pi, sin, exp, linspace
import matplotlib.pyplot as plt

def f(x, t):
	e = exp(-(x - 3*t)**2)
	s = sin(3*pi * (x - t))
	es = e * s
	return es

t0 = 0
x0 = linspace(-4, 4, 729)

ax = plt.subplot(111)

ax.plot(x0, f(x0, t0))
ax.legend(['wave'])
ax.set_xlabel('x-values')
ax.set_ylabel('location')

plt.show()

"""
Terminal> python3 plot_wavepacket.py

"""
