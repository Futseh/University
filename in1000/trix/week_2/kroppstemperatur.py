import sys

temp = float(sys.argv[1])

if temp < 36.5:
    print('Du har lavere kroppstemperatur enn normalen')
elif temp > 37.5:
    print('Du har høyere kroppstemperatur enn normalen')
else:
    print('Du har normal kroppstemperatur')

"""
Terminal> python3 kroppstemperatur 37
    Du har normal kroppstemperatur
"""