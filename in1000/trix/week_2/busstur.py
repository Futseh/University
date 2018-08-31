mennesker = 0
plasser = 30

antall = int(input('Stasjon 1! Hvor mange går på bussen? '))

if mennesker + antall > plasser:
    print('Bussen er full. ' + str(mennesker + antall - plasser) + ' må gå.')
    mennesker = 30
else:
    mennesker += antall

antall = int(input('Stasjon 2! Hvor mange går på bussen? '))

if mennesker + antall > plasser:
    print('Bussen er full. ' + str(mennesker + antall - plasser) + ' må gå.')
    mennesker = 30
else:
    mennesker += antall

antall = int(input('Stasjon 3! Hvor mange går på bussen? '))

if mennesker + antall > plasser:
    print('Bussen er full. ' + str(mennesker + antall - plasser) + ' må gå.')
    mennesker = 30
else:
    mennesker += antall

print('Bussen er fremme med', mennesker, 'passasjerer ombord.')

"""
Terminal> python3 busstur.py
    Stasjon 1! Hvor mange går på bussen? 12
    Stasjon 2! Hvor mange går på bussen? 12
    Stasjon 3! Hvor mange går på bussen? 12
    Bussen er full. 6 må gå.
"""