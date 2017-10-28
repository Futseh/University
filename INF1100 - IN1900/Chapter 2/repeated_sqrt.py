# Exercise 2.19

from math import sqrt

for n in range(1, 15):
    r = 2.0
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r**2
    print '%d times sqrt and **2: %.16f' % (n, r)

"""
Terminal> python reapeated_sqrt.py
    1 times sqrt and **2: 2.0000000000000004
    2 times sqrt and **2: 1.9999999999999996
    3 times sqrt and **2: 1.9999999999999996
    4 times sqrt and **2: 1.9999999999999964
    5 times sqrt and **2: 1.9999999999999964
    6 times sqrt and **2: 1.9999999999999964
    7 times sqrt and **2: 1.9999999999999714
    8 times sqrt and **2: 2.0000000000000235
    9 times sqrt and **2: 2.0000000000000235
    10 times sqrt and **2: 2.0000000000000235
    11 times sqrt and **2: 2.0000000000000235
    12 times sqrt and **2: 1.9999999999991336
    13 times sqrt and **2: 1.9999999999973286
    14 times sqrt and **2: 1.9999999999973286
"""
