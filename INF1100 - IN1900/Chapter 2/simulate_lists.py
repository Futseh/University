# Exercise 2.10

a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c

b[0] = -1
d = [e + 1 for e in a]
print d

d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2:]

for e1 in a:
    for e2 in b:
        print e1 + e2

"""
Terminal> python simulate_lists.py
    [1, 3, 5, 7, 11, 13, 17]
    [2, 4, 6, 8, 12]
    [0, 18]
    0
    18
    2
    20
    4
    22
    6
    24
    10
    28
"""
