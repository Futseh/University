t = [2.38, 2.41, 2.37, 2.76, 2.40, 2.44, 2.79, 2.77]
U = [0.99, 0.81, 0.92, 0.76, 0.92, 0.90, 0.78, 0.78]

res = 0
eps = 0
ta = 0

Ut = 0

NA = 11

for i in range(len(t)):
	Ut = U[i] * 10**(-3)
	res += ((Ut * t[i]) / (2.0 * 2 * NA)) 
	eps += U[i] * 10**(-3)
	ta += t[i]

epsr = eps / len(U)
tar = ta / len(t)

Ba = (epsr * tar) / (2.0 * 2 * NA)

print "B is approximate %s T" % str(res / len(t))
print Ba

"""
Termianl> python EarthMagneticField.py
    B is approximate 4.92247159091e-05 T
    4.95011363636e-05
"""