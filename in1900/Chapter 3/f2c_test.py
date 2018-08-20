# Exercise 3.5

def C(F):
  celsius = (5. / 9) * (F - 32)
  return celsius

def F(C):
  Fahrenheit = (9. / 5) * C + 32
  return Fahrenheit

def test_F_C(c, f):
  expected_C = c
  expected_F = f
  
  computed_C = C(F(c))
  computed_F = F(C(f))
  
  tol = 1E-14
  success = abs(expected_C - computed_C) < tol and abs(expected_F - computed_F) < tol
  msg = 'computed C %g != %g (expected) and computed F %g != %g (expected)' % (computed_C, expected_C, computed_F, expected_F)
  assert success, msg

test_F_C(0, 32)

"""
terminal> python3 3 f2c_test.py

"""