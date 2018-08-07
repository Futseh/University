# Exercise 1.11

from math import pi

Cd = 0.4
q = 1.2 # kg/m^3
a = 11 / 100.0 # to get 11 cm to meters
A = pi * a**2 # this is the crosssectional area of the ball with a meters

# The speed is 120 km/h
V = 120 / 3.6 # get the speed from km/h to m/s
m = 0.43 # kg
g = 9.81 # m/s^2

Fd = 0.5 * Cd * q * A * V**2
Fg = m * g

print('The gravity force is: %.2f and the drag force is: %.2f' % (Fg, Fd))

print('The ratio is %.2f' % (Fd / Fg))

# The speed is 30 km/h
V = 30 / 3.6 # get the speed from km/h to m/s

Fd = 0.5 * Cd * q * A * V**2
Fg = m * g

print('The gravity force is: %.2f and the drag force is: %.2f' % (Fg, Fd))

print('The ratio is %.2f' % (Fd / Fg))

"""
Terminal> python kick.py
    The gravity force is: 4.22 and the drag force is: 10.14
    The gravity force is: 4.22 and the drag force is: 0.63
    The ratio is 0.15
"""
