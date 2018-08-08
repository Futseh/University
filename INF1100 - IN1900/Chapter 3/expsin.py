# Exercise 3.1

from math import exp, sin, pi

def g(t):
    return exp(-t) * sin(pi * t)

print(g(0))
print(g(1))

"""
Terminal> python expsin.py
    0.0
    4.50522380103e-17
"""
