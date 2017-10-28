# Exercise 1.10

from math import exp, pi, sqrt

m = 0.0
s = 2.0
x = 1.0

e = exp((-1 / 2.0) * (((x - m) / s)**2))
f = (1 / (sqrt(2 * pi) * s))

fe = f * e

print fe

"""
Terminal> python gaussian1.py
        0.176032663382
"""
