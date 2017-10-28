# Exercise 2.8 a

v0 = 100 # m/s
g = 9.81 # m/s**2
ts = 0
te = (2 * v0) / g
n = 0

print '---------------------'
print 'Time \t Height \n'

for i in range(ts, int(te + 1), n + 1):
    yt = v0 * i - 0.5 * g * i**2
    print '%g | \t %.2f' % (i, yt)
print '--------------------- \n'

# Exercise 2.8 b

print '---------------------'
print 'Time \t Height \n'

while ts < te:
    yt = v0 * ts - 0.5 * g * ts**2
    print '%g | \t %.2f' % (ts, yt)
    ts += 1
print '---------------------'

"""
Terminal> python ball_table1.py
    ---------------------
    Time     Height

    0 |      0.00
    1 |      95.09
    2 |      180.38
    3 |      255.85
    4 |      321.52
    5 |      377.38
    6 |      423.42
    7 |      459.65
    8 |      486.08
    9 |      502.69
    10 |     509.50
    11 |     506.50
    12 |     493.68
    13 |     471.05
    14 |     438.62
    15 |     396.38
    16 |     344.32
    17 |     282.45
    18 |     210.78
    19 |     129.29
    20 |     38.00
    ---------------------

    ---------------------
    Time     Height

    0 |      0.00
    1 |      95.09
    2 |      180.38
    3 |      255.85
    4 |      321.52
    5 |      377.38
    6 |      423.42
    7 |      459.65
    8 |      486.08
    9 |      502.69
    10 |     509.50
    11 |     506.50
    12 |     493.68
    13 |     471.05
    14 |     438.62
    15 |     396.38
    16 |     344.32
    17 |     282.45
    18 |     210.78
    19 |     129.29
    20 |     38.00
    ---------------------
"""
