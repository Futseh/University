# Exercise 3.7

def sum_1k(M):
    s = 0
    
    for k in range(M):
        s += 1.0 / (k + 1)
    
    return s

def test_sum_1k():
    expected = 1.5
    computed = sum_1k(2)
    
    tol = 1E-15
    success = abs(computed - expected) < tol
    msg = 'computed %g != %g (expected)' % (computed, expected)
    assert success, msg
    
test_sum_1k()

"""
Terminal> python3 sum_func.py

"""