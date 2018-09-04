"""
Denne koden fungerer, men det er en feil i den, oppgitt i oppgave 3.08.

x = 0
y = 0

x = int(input("Tast inn et heltall: "))
x = int(input("Tast inn et heltall til: "))

print("Summen av tallene er:", x+y)
"""
"""
Feilen ligger i at du spørr om to tall, men setter x lik de tallene.
Så hvis du skriver inn 2 først, men så skriver du inn 4 så vil x ha verdien 4
"""

x = 0
y = 0

x = int(input("Tast inn et heltall: "))
y = int(input("Tast inn et heltall til: "))

print("Summen av tallene er:", x+y)

"""
Terminal> feilutenvarsel.py
    Tast inn et heltall: 90
    Tast inn et heltall til: 90
    Summen av tallene er: 180
"""