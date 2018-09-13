n = 0
tall = int(input('Hvilket tall vil du ha? '))

while n <= tall:
    print(n)
    n += 1

num = 0

while num != 10:
    num = int(input('Skriv inn et tall. '))

print("Du tastet 10, programmet avsluttes")

"""
Terminal> python3 lokker.py
    Hvilket tall vil du ha? 10
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    Skriv inn et tall. 19
    Skriv inn et tall. 9
    Skriv inn et tall. 2
    Skriv inn et tall. 10
    Du tastet 10, programmet avsluttes
"""