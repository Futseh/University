# Exercise 4.12

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

tb = (2 * v0) / g

if t > 0 and t < tb:
    y = v0*t - 0.5*g*t**2

    print y
else:
    print "When v0 is %.2f the value of t needs to be between 0 and %.2f" % (v0 ,tb)
    sys.exit(1)

"""
The checks for IndexError and ValueError was shown in Exercise 4.11 "ball_cml_qa.py"

Will check when t is less than 0
Terminal> python ball_cml_tcheck.py 5 -1
When v0 is 5.00 the value of t needs to be between 0 and 1.02

Will check when t is bigger than tb
Terminal> python ball_cml_tcheck.py 5 1234
When v0 is 5.00 the value of t needs to be between 0 and 1.02

Will check when t is between 0 and tb
Terminal> python ball_cml_tcheck.py 5 1
0.095
"""
