# Exercise 3.3

def add(A, B):
    C = A + B
    return C

a = 3
b = 2

print(add(a, b))         # Print the result fo the function add with the parameters a (3) and b (2)
print(add(2*a, b+1)*3)   # Print the result fo the function add with the parameters 2*a (6) and b+1 (3) and then times that with 3

"""
Terminal> python explain_func.py
    5
    27
"""
