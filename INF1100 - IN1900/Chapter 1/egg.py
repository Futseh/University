# Exercise 1.12

from math import log, pi

Ms = 47 # weight in grams for a small egg
Ml = 67 # weight in grams for a large egg
p = 1.038 # g/cm**3 density
c = 3.7 # heat capacity J/(g*K)
K = 5.4 * 10**(-3) # thermal conductivity W/(cm * K)
Tw = 100 # degrees in C for boiling water

# degrees = 4
To = 4 # degrees in C for the egg
Ty = 70 # degrees in C

ln = log(0.76*((To - Tw)/(Ty - Tw)))
mass = (Ml**(2/3) * c * p**(1/3))/(K * pi**2 * ((4 * pi) / 3)**(2/3))

t = mass * ln

print(t)

# degrees = 20
To = 20 # degrees in C for the egg

ln = log(0.76*((To - Tw)/(Ty - Tw)))
mass = (Ml**(2/3) * c * p**(1/3))/(K * pi**2 * ((4 * pi) / 3)**(2/3))

t = mass * ln

print(t)

"""
Terminal> python egg.py
    396.5763425294507
    315.2178637859262
"""
