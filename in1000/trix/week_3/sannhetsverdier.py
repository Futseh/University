b = False
x = 0

print(b and x == 0) # Frue
# print(b or x == 0;) Denne lager en error melding pga ; på slutten
print(not b and x == 0) # False
print(not b or x == 0) # True
print(b and x != 0) # False
print(b or x != 0) # False
print(not b and x != 0) # False 
print(not b or x != 0) # True

"""
Terminal> python3 sannhetsverdier.py
    False
    True
    True
    False
    False
    False
    True
"""