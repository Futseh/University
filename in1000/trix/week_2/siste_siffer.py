x = int(input('Oppgi en verdi for x: '))
y = int(input('Oppgi en verdi for y: '))
z = int(input('Oppgi en verdi for z: '))

if x % 10 == y % 10:
    print('x og y har samme siste siffer')

if x % 10 == z % 10:
    print('x og z har samme siste siffer')

if y % 10 == z % 10:
    print('y og z har samme siste siffer')

"""
Terminal> python3 siste_siffer.py
    Oppgi en verdi for x: 19
    Oppgi en verdi for y: 12359
    Oppgi en verdi for z: 123459
    x og y har samme siste siffer
    x og z har samme siste siffer
    y og z har samme siste siffer
"""