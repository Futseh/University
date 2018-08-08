# Exercise 3.16

import numpy as np
import math as ma

def triangle_area(vertices):

    x1 = vertices[0][0]
    x2 = vertices[1][0]
    x3 = vertices[2][0]

    y1 = vertices[0][1]
    y2 = vertices[1][1]
    y3 = vertices[2][1]

    points = np.abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 + x2 * y1)
    A = 1/2.0 * points

    return A

def test_triangle_area():
    """
    Verify the area of a triangle with vertex coordinates
    (0, 0), (1, 0), (0, 2)
    """
    v1 = (0, 0)
    v2 = (1, 0)
    v3 = (0, 2)

    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed area=%g != %g (expected)' % (computed, expected)
    assert success, msg

test_triangle_area()

"""
Terminal> python area_triangle.py
    
"""
