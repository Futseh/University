# Exercise 4.11

import sys

g = 9.81

try:
    v0 = float(sys.argv[1]) # v0 is at index 1 since the filename you run is at index 0
    t = float(sys.argv[2])
except IndexError:
    print "Both v0 and t need to be supplied on the command line."
    v0 = float(raw_input("v0 = "))
    t = float(raw_input("t = "))
except ValueError:
    print 'v0 and t must be pure numbers'
    sys.exit(1)

y = v0*t - 0.5*g*t**2

print y

"""
Will check first when no argument is given
Terminal> python ball_cml_qa.py
Both v0 and t need to be supplied on the command line.
v0 = 5
t = 1
0.095

Will check when one of the arguments aren't a number
Terminal> python ball_cml_qa.py 5 hey
v0 and t must be pure numbers

will check when both arguments are numbers
Terminal> python ball_cml_qa.py 5 1
0.095
"""
