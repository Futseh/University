import sympy as sp

mat = sp.Matrix([[-6, 2, 2, 6], [-1, 0, -1, -2]])

reduced = mat.rref()

print(reduced)

pcb = reduced[0][:2,2:]
pbc = pcb.inv()

print(pcb)
print()
print(pbc)