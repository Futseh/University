import sympy as sp

M = sp.Matrix([[-6,  4, 0,  9],
               [-3,  0, 1,  6],
               [-1, -2, 1,  0],
               [-4,  4, 0,  7]])

eigen = M.eigenvals()
eigenvec = M.eigenvects()

P, D = M.diagonalize()

print(eigen)

for i in range(0, len(eigenvec)):
    for j in range(0, len(eigenvec[i][2])):
        sp.pprint(eigenvec[i][2][j])

sp.pprint(P)
sp.pprint(D)