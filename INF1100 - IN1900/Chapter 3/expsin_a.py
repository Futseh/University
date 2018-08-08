# Exercise 3.2

from math import exp, sin, pi

def h(t, a):
    return exp(-t * a) * sin(pi * t)

print(h(0, 10))
print(h(1, 10))

"""
Terminal> python expsin_a.py
    0.0
    5.55988786651e-21
"""
