import sympy as sp

theta = sp.symbols('theta')
phi = sp.symbols('phi')
lamda = sp.symbols('lambda')

"""
a = sp.Symbol('a')
b = sp.Symbol('b')
c = sp.Symbol('c')
d = sp.Symbol('d')
e = sp.Symbol('e')
f = sp.Symbol('f')
g = sp.Symbol('g')
h = sp.Symbol('h')
"""

M = sp.Matrix([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, sp.cos(theta), -sp.sin(theta)],
               [0, 0, sp.sin(theta), sp.cos(theta)]])

eigen = M.eigenvals()
eigenvec = M.eigenvects()

sp.pprint(eigenvec)

determinant = M.det()

sp.pprint(determinant)

N = sp.Matrix([[sp.cos(phi), -sp.sin(phi), 0, 0],
               [sp.sin(phi),  sp.cos(phi), 0, 0],
               [0, 0, sp.cos(theta), -sp.sin(theta)],
               [0, 0, sp.sin(theta),  sp.cos(theta)]])

eigen = N.eigenvals()
eigenvec = N.eigenvects()

sp.pprint(eigenvec)

determinant = N.det()

sp.pprint(determinant)

"""
A = sp.Matrix([[a-lamda, b, 0, 0],
               [c, d-lamda, 0, 0],
               [0, 0, e-lamda, f],
               [0, 0, g, h-lamda]])

eigen = A.eigenvects()

sp.pprint(A.det())

sp.pprint(eigen)
"""