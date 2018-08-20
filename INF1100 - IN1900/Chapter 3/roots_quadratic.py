# Exercise 3.8

import numpy as np

def roots(a, b, c):
	d = b**2 - 4 * a * c

	if d < 0:
		de = np.sqrt(-d)
		dr = '%.2f' % de
		dc = complex(0, float(dr))

		x1 = (-b + dc) / 2. * a
		x2 = (-b - dc) / 2. * a
  
		solutions = [x1, x2]
	
		return solutions
	else:
		x1 = (-b + np.sqrt(d)) / 2. * a
		x2 = (-b - np.sqrt(d)) / 2. * a
		
		x1 = '%.2f' % x1
		x2 = '%.2f' % x2
		
		solutions = [x1, x2]
		
		return solutions

def test_root_float():	
	expected = [-0.59, -3.41]
	computed = roots(1, 4, 2)
	
	for i in range(len(expected)):
		tol = 1E-14
		success = abs(expected[i] - float(computed[i])) < tol
		msg = 'computed=%g != %g (expected)' % (float(computed[i]), expected[i])
		assert success, msg  

def test_root_complex():
	expected = [-1+1.73j, -1-1.73j]
	computed = roots(1, 2, 4)
	
	for i in range(len(expected)):
		tol = 1E-14
		success = abs(expected[i] - computed[i]) < tol
		msg = 'computed=%.5s != %.5s (expected)' % (computed[i], expected[i])
		assert success, msg 

test_root_float()
test_root_complex()

"""
Terminal> python3 roots_quadratic.py

"""
