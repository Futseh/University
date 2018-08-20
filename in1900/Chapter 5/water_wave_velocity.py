# Exercise 5.31

from numpy import pi, tanh, sqrt, linspace
import matplotlib.pyplot as plt

def c(lam):
	g = 9.81 # m/s**2
	s = 7.9 * 10**-2 # N/m
	p = 1000 # kg/m**3
	h = 50 # m

	part1 = (g*lam)/(2*pi)
	part2 = 1 + s*((4*pi**2)/(p*g*lam**2))
	part3 = tanh((2*pi*h)/lam)
	result = sqrt(part1*part2*part3)

	return result

lam1 = linspace(0.001, 0.1, 1010)
lam2 = linspace(1, 2000, 4002)

ax = plt.subplot(211)
bx = plt.subplot(212)

ax.plot(lam1, c(lam1))
ax.set_xlabel('lambda in meters')
ax.set_ylabel('wavespeed in m/s')

bx.plot(lam2, c(lam2))
bx.set_xlabel('lambda in meters')
bx.set_ylabel('wavespeed in m/s')

plt.show()

"""
Terminal> python3 water_wave_velocity.py

"""
