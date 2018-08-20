# Exercise 5.41

from numpy import pi, sin, linspace, where, zeros
import matplotlib.pyplot as plt

t = linspace(0, 2*pi, 1000)
k = 4/pi


def S(t, n, T):
	calc = zeros(len(t))
	for i in range(1, n + 1):
		p1 = 1./(2.*i - 1.)
		p2 = sin(2.*(2.*i - 1.)*pi*t/T)
		calc += p1*p2
	return calc*k

def f(t, T):
	tt = zeros(len(t))
	for i in t:
		if 0 < i < T/2.:
			tt += 1
		elif i == T/2.:
			tt += 0
		else:
			tt += -1
	return tt

ax = plt.subplot(111)

ax.plot(t, S(t, 1, 2*pi))
ax.plot(t, S(t, 3, 2*pi))
ax.plot(t, S(t, 20, 2*pi))
ax.plot(t, S(t, 200, 2*pi))

ax.plot(t, f(t, 2*pi))
ax.set_xlabel('t-values')
ax.set_ylabel('y-values')

plt.legend(['n = 1', 'n = 3', 'n = 20', 'n = 200', 'f(t, T)'])

plt.show()

"""
Terminal> python3 sinesum1_plot.py

"""
