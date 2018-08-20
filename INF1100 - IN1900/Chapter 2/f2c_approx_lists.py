# Exercise 2.16

F = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
C = []
C_approx = []
Temp = [F, C, C_approx]

for i in range(0, len(F), 1):
  C.append((5 / 9.0) * F[i] - 32)
  C_approx.append((F[i] - 30.0) / 2)

print('----------------------------------')
print('Fahrenheit \t Celcius \t Approx Celcius')

for j in range(len(F)):
  print('%.2f \t\t %.2f \t\t %.2f' % (Temp[0][j], Temp[1][j], Temp[2][j]))

print('----------------------------------')

"""
Terminal> python3 f2c_approx_lists.py
  ----------------------------------
  Fahrenheit    Celcius     Approx Celcius
  0.00       -32.00         -15.00
  10.00      -26.44         -10.00
  20.00      -20.89         -5.00
  30.00      -15.33         0.00
  40.00      -9.78      5.00
  50.00      -4.22      10.00
  60.00      1.33      15.00
  70.00      6.89      20.00
  80.00      12.44      25.00
  90.00      18.00      30.00
  100.00      23.56      35.00
  ----------------------------------
"""
