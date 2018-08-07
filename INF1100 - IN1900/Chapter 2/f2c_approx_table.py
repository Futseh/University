# Exercise 2.2

F = 0
dF = 10

print('-----------------')
print('Fahrenheit \t Celcius \t Approx Celcius')

while F <= 100:
    C = (5 / 9.0) * F - 32
    Ca = (F - 30) / 2
    print('%g \t\t %.2f \t\t %g' % (F, C, Ca))
    F += dF
print('-----------------')

"""
Terminal> python f2c_approx_table.py
    -----------------
    Fahrenheit       Celcius         Approx Celcius
    0                -32.00                  -15
    10               -26.44                  -10
    20               -20.89                  -5
    30               -15.33                  0
    40               -9.78           5
    50               -4.22           10
    60               1.33            15
    70               6.89            20
    80               12.44           25
    90               18.00           30
    100              23.56           35
    -----------------
"""
