# Exercise 1.17

from math import sqrt

a = 2
b = 1
c = -2

q = b * b - 4 * a * c # This number will be negative unless you change the variables
q_sr = sqrt(q)

x1 = (-b + q_sr) / 2 * a
x2 = (-b - q_sr) / 2 * a

print x1
print x2

"""
Terminal> python find_errors_roots.py
    3.12310562562
    -5.12310562562
"""
