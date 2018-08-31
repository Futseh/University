pris = 50
tekst = input("Skriv inn alder: ")
alder = int(tekst)

if alder < 12 or alder > 67:
    print("Du må betale", pris*0.5, "kr")
else:
    print("Du må betale", pris, "kr")

"""
På linje 1 setter vi variablen pris lik 50.
Deretter spørr vi brukeren om en alder som vi setter variablen lik.
På linje 3 tar vi verdien vi fikk fra brukeren, som er en streng, og konverterer/caster den til et heltall 
og legger den verdien inn i variablen alder.

På linje 5 sjekker vi om varablen alder er mindre enn 12 eller større enn 67. Hvis den er det så skal vi printet at de må
betale halve prisen, 25 kr.
Hvis alderen er mellom 12 og 67 så printer vi at de må betale hele prisen, som er 50 kr.
"""