"""
Denne koden virker ikke, oppgitt i oppgave 3.07.

tall = input(Tast inn et siffer: )
dobbelt = 2 * tall
print("Det dobbelte er" dobbel)
"""
"""
Det som er feil er:

Du har ikke teksten i input market som en streng.
Printen fungerer ikke.
Det kan skrives på en av disse måtene:
    print("Volumet er:", volum)
    print("Volumet er: " + str(volum))

Feil variabel navn i printen.

Kan også nevnes at ut ifra spørsmålet så vil de ha et tall
og da må du kaste variablen tall over til float eller int
Dette kan bli sett på som den fjerde feilen
"""

tall = float(input('Tast inn et siffer: '))
dobbelt = 2 * tall
print('Det dobbelte er:', dobbelt)

"""
Terminal> python3 feilretting.py
    Tast inn et siffer: 123
    Det dobbelte er: 246.0
"""