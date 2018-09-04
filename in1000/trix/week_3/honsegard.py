honer = int(input('Hvor mange høner er det på gården? '))
reven = input('Kommer reven? ')
bonden = input('Sover bonden? ')

reveskinn = 190

if reven.lower() == bonden.lower() == 'ja':
    print('Det bor nå', honer, 'høns på gården. Bonden selger ett reveskinn og tjener', reveskinn, ' kr.')
elif reven.lower() == 'ja' and bonden.lower() == 'nei':
    print('Det bor nå', honer-1, 'høns på gården.')
else:
    print('Det bor nå', honer, 'høns på gården.')

"""
Terminal> python3 honsegard.py
    Hvor mange høner er det på gården? 10
    Kommer reven? ja
    Sover bonden? ja
    Det bor nå 10 høns på gården. Bonden selger ett reveskinn og tjener 190  kr.
    
    Hvor mange høner er det på gården? 10
    Kommer reven? ja
    Sover bonden? nei
    Det bor nå 9 høns på gården.
    
    Hvor mange høner er det på gården? 10
    Kommer reven? nei
    Sover bonden? nei
    Det bor nå 10 høns på gården.
"""