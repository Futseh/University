maaneder = ['Januar', 'Februar', 'Mars', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Desember']

svar = int(input('Hvilken månede trenger du informasjon om? '))

if not 0 < svar < 13:
    print('Det er ikke en gyldig månede.')
else:
    print(maaneder[svar-1])

"""
Terminal> python3 maaneder.py
    Hvilken månede trenger du informasjon om? 1
    Januar
"""