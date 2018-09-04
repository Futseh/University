"""
Denne koden virker ikke, oppgitt i oppgave 3.05.

lengde = 3
volum = lengde * bredde * høyde
print("Volumet er:" volum)
"""

"""
Det som er feil med den koden i den øverste kommentaren er:
Bredde og høyde er ikke definert.
Printen fungerer ikke.
Det kan skrives på en av disse måtene:
    print("Volumet er:", volum)
    print("Volumet er: " + str(volum))
"""

hoyde = 3
lengde = 3
bredde = 3
volum = lengde * bredde * hoyde
print("Volumet er:", volum)

"""
Terminal> python3 volum.py
    Volumet er: 27
"""