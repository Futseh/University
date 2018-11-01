import sympy as sp

M = sp.Matrix([[5, -3, 0,  9],
               [0,  3, 1, -2],
               [0,  0, 2,  0],
               [0,  0, 0,  2]])

P, D = M.diagonalize()

sp.pprint(P)
sp.pprint(D)

print(P*D*P**-1 == M)