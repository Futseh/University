# Exercise 2.1

F = 0
dF = 10

print('------------------------')
print('Fahrenheit \t Celcius')
while F <= 100:
  C = (5 / 9.0) * F - 32
  print("%g \t\t %.2f" % (F, C))
  F += dF
print('------------------------')

"""
Terminal> python3 f2c_table.py
  ------------------------
  Fahrenheit    Celcius
  0        -32.00
  10        -26.44
  20        -20.89
  30        -15.33
  40        -9.78
  50        -4.22
  60        1.33
  70        6.89
  80        12.44
  90        18.00
  100       23.56
  ------------------------
"""
