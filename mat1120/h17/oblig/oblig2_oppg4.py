import numpy as np

Y = np.array([[0.08, 4.05], [0.12, 4.15], [0.2, 3.85], [0.38, -0.22]])

Aa = np.zeros(shape=(4, 3))
Ab = np.zeros(shape=(4, 2))
b = np.zeros(4)

for i in range(4):
	Aa[i][0] = 1
	Aa[i][1] = Y[i][0]
	Aa[i][2] = Y[i][0]**2
	Ab[i][0] = np.sin(np.pi * 2 * Y[i][0])**2
	Ab[i][1] = np.cos(np.pi * 2 * Y[i][0])**2
	b[i] = Y[i][1]

xa = np.dot(np.linalg.inv(np.dot(Aa.T, Aa)), np.dot(Aa.T, b))
xb = np.dot(np.linalg.inv(np.dot(Ab.T, Ab)), np.dot(Ab.T, b))

print 'f(x) = %.4f + %.4fx + %.4fx^2' % (xa[0], xa[1], xa[2])
print 'f(x) = %.4f*sin(2*pi*x) + %.4f*cos(2*pi*x)' % (xb[0], xb[1])

erra = np.linalg.norm(b.T - np.dot(xa, Aa.T))
errb = np.linalg.norm(b.T - np.dot(xb, Ab.T))

print 'Feil med metode A: %.5f' % erra
print 'Feil med metode B: %.5f' % errb

"""
Terminal> python oblig2_oppg4.py
    f(x) = 3.0473 + 17.8362x + -69.5494x^2
    f(x) = 3.2241*sin(2*pi*x) + 2.6705*cos(2*pi*x)
    Feil med metode A: 0.04530
    Feil med metode B: 3.66556
"""