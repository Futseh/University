x = int(input('Tast inn et tall: '))

if x >= 20:
    print('Tallet er større enn eller lik 20')
elif 10 < x < 20:
    print('Tallet er mellom 10 og 20')
else:
    print('Tallet er mindre enn eller lik 10')

"""
Terminal> python3 mindre_større.py
    Tast inn et tall: 123
    Tallet er større enn eller lik 20
"""