import numpy as np
import matplotlib.pyplot as plt

mu0 = 4 * np.pi *10**(-7)
a = 2 * 10**(-3)
b = 4 * 10**(-3)
t = 1 * 10**(-3)

I = 1

r = np.linspace(0, b + t + 2*10**(-3), 1000)
B = np.zeros(len(r))

for i in range(len(r)):
	if r[i] < a:
		B[i] = (mu0 * I * r[i]) / (2 * np.pi * a**2)
	elif a < r[i] < b:
		B[i] = (mu0 * I) / (2 * np.pi * r[i])
	elif b < r[i] < b + t:
		B[i] = (mu0 * I) / (2 * np.pi * r[i]) * ((b + t)**2 - r[i]**2) / (2*b*t + t**2)
	elif b + t < r[i]:
		B[i] = 0
	else:
		pass

plt.plot(r, B)
plt.title("Plot av B-Feltet")
plt.xlabel("r [m]")
plt.ylabel("B(r) [T]")
plt.show()