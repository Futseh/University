import sys

inntekt = float(sys.argv[1])

if inntekt < 10000:
    skatt = inntekt / 10.0
else:
    inn = inntekt - 10000
    skatt1 = 10000 / 10.0
    skatt2 = inn * 30.0 / 100.0
    skatt = skatt1 + skatt2

print('Du har en inntekt på: %gkr.\nDu må betale %.2fkr i skatt' % (inntekt, skatt))

"""
Temrinal> python3 skatt_ruritania.py 12345
    Du har en inntekt på: 12345kr.
    Du må betale 1703.50kr i skatt
"""