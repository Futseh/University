# Exercise 4.10

import sys

g = 9.81

v0 = float(sys.argv[1]) # v0 is at index 1 since the filename you run is at index 0
t = float(sys.argv[2]) # v0 is at index 2 since the filename you run is at index 0

y = v0*t - 0.5*g*t**2

print y

"""
Terminal> python ball_cml.py 5 1
0.095
"""
