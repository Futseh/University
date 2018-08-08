# Exercise 3.4

def C(F):
    celsius = (5. / 9) * (F - 32)
    return celsius

def F(C):
    Fahrenheit = (9. / 5) * C + 32
    return Fahrenheit

print(C(F(100)))
print(F(C(50)))

"""
Terminal> python f2c.py
    100.0
    50.0
"""
