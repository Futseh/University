hoyde = int(input('Hei! Hvor høy er du i centimeter? '))

if hoyde < 140:
    print('Du er lav')
elif 140 <= hoyde <= 190:
    print('Du er middels')
else:
    print('Du er høy')

"""
Terminal> python3 hoyde.py
    Hei! Hvor høy er du i centimeter? 190
    Du er middels
"""