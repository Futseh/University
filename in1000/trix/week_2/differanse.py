x = int(input('Oppgi verdien til x: '))
y = int(input('Oppgi verdien til y: '))

if x > y:
    print('Differansen er: ' + str(x - y))
else:
    print('Differansen er: ' + str(y - x))

"""
x = 5, y = 10
terminal> python3 differanse.py
    Differansen er: 5

x = 10, y = 5
terminal> python3 differanse.py
    Differansen er: 5
"""