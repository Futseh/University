# Exercise 1.8

from math import pi
h = 5.0
b = 2.0
r = 1.5

area_parallelogram = h * b
print('The area of the parallelogram is %.3f' % area_parallelogram)

area_square = b ** 2
print('The area of the square is %g' % area_square)

area_circle = pi * r ** 2
print('The area of the circle is %.3f' % area_circle)

volume_cone = 1.0 / 3 * pi * r ** 2 * 2 * h
print('The volume of the cone is %.3f' % volume_cone)

"""
Terminal> python3 formulas_shapes.py
  The area of the parallelogram is 10.000
  The area of the square is 4
  The area of the circle is 7.069
  The volume of the cone is 23.562
"""