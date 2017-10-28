# Exercise 3.29

def H(x):
	if x < 0:
		return 0
	else:
		return 1

def test_H():
	values = [H(-10), H(-10**-15), H(0), H(10**-15), H(10)]
	expected_values = [0, 0, 1, 1, 1]
	
	for i in range(len(values)):
		computed = values[i]
		expected = expected_values[i]
		tol = 1E-14
		success = abs(expected - computed) < tol
		msg = 'computed =%g != %g (expected)' % (computed, expected)
		assert success, msg
	
test_H()

"""
Terminal> python Heaviside.py

"""