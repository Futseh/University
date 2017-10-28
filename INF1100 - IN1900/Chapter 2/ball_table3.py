# Exercise 2.17

import numpy as np

y = []
t = []

v0 = 10 # m/s
g = 9.81 # m/s**2
ts = 0
te = (2 * v0) / g
n = 20

tr = np.linspace(ts, te, num=n)

for l in range(len(tr)):
    t.append(tr[l])
    yh = tr[l]
    ys = v0 * yh - 0.5 * g * yh**2
    y.append(ys)

ty1 = [t, y]

print '---------------------'
print 'Time \t Height \n'

for i in range(len(t)):
    print '%.2f \t %.2f' % (ty1[0][i], ty1[1][i])
print '---------------------'

ty2 = []

for i in range(len(t)):
    x = t[i]
    z = y[i]
    k = [x, z]
    ty2.append(k)

print '---------------------'
print 'Time \t Height \n'
for i in range(len(ty2)):
    print '%.2f \t %.2f' % (ty2[i][0], ty2[i][1])
print '---------------------'

"""
Terminal> python ball_table3.py
    ---------------------
    Time     Height

    0        0.00
    1        95.09
    2        180.38
    3        255.85
    4        321.52
    5        377.38
    6        423.42
    7        459.65
    8        486.08
    9        502.69
    10       509.50
    11       506.50
    12       493.68
    13       471.05
    14       438.62
    15       396.38
    16       344.32
    17       282.45
    18       210.78
    19       129.29
    20       38.00
    ---------------------
    ---------------------
    Time     Height

    0        0.00
    1        95.09
    2        180.38
    3        255.85
    4        321.52
    5        377.38
    6        423.42
    7        459.65
    8        486.08
    9        502.69
    10       509.50
    11       506.50
    12       493.68
    13       471.05
    14       438.62
    15       396.38
    16       344.32
    17       282.45
    18       210.78
    19       129.29
    20       38.00
    ---------------------
"""
