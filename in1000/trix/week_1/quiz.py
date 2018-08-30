svar = input('Hva heter hovedstaden i Marokko? ')

riktig = 'rabat'

if svar.lower() == riktig:
    print('Helt rett!')
else:
    print('Beklager, svaret var ', riktig)

"""
Terminal> python3 quiz.py
    Helt rett!
"""