# Exercise 1.14

# The lines I have in comments are for which line of the Exercise it is

# Line 1
C = 21
F = 9 / 5 * C + 32 # It doesn't work because of integer division
print F

# Line 2
C = 21.0
F = (9 / 5) * C + 32 # It doesn't work because of integer division
print F

# Line 3
C = 21.0
F = 9 * C / 5 + 32
print F

# Line 4
C = 21.0
F = 9. * (C / 5.0) + 32
print F

# Line 5
C = 21.0
F = 9.0 * C / 5.0 + 32
print F

# Line 6
C = 21
F = 9 * C / 5 + 32
print F

# Line 7
C = 21.0
F = (1 / 5) * 9 * C + 32 # Since the 1 / 5 is an integer division it will take the number as 0 instead of 0.2
print F

# Line 8
C = 21
F = (1. / 5) * 9 * C + 32
print F

"""
Terminal> python find_errors_division.py
    53
    53.0
    69.8
    69.8
    69.8
    69
    32.0
    69.8
"""
