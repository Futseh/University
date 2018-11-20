import sympy as sp

theta = sp.symbols('theta')
phi = sp.symbols('phi')

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