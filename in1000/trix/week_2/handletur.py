brodpris = 20
melkpris = 15
ostpris = 40
youghurtpris = 12

total = 0

print('Hei! Velkommen til IFI-Butikken')

brod = int(input('Hvor mange brød vil du ha? '))
total += brod * brodpris

melk = int(input('Hvor mange melk vil du ha? '))
total += melk * melkpris

ost = int(input('Hvor mange ost vil du ha? '))
total += ost * ostpris

youghurt = int(input('Hvor mange youghurt vil du ha? '))
total += youghurt * youghurtpris

print('Du skal betale:', total)

"""
Terminal> python3 handletur.py
    Hei! Velkommen til IFI-Butikken
    Hvor mange brød vil du ha? 13
    Hvor mange melk vil du ha? 14
    Hvor mange ost vil du ha? 15
    Hvor mange youghurt vil du ha? 16
    Du skal betale: 1262
"""