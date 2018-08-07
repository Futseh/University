# Exerise 2.7 a

coords = []
n = 10
h = 0.01

for i in range(n + 1):
    coords.append((1 + i) * h)

for x in range(len(coords)):
    print('%3.2f' % x)

# Exerise 2.7 b

coord = [((1 + i) * h) for i in range(n + 1)]

print('\n')

for x in range(len(coords)):
    print('%3.2f' % x)

"""
Terminal> python coor.py
    0.00
    1.00
    2.00
    3.00
    4.00
    5.00
    6.00
    7.00
    8.00
    9.00
    10.00


    0.00
    1.00
    2.00
    3.00
    4.00
    5.00
    6.00
    7.00
    8.00
    9.00
    10.00

"""
