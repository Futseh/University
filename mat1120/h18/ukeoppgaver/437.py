import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return 1 - 8*np.cos(t)**2 + 8*np.cos(t)**4

def g(t):
    return -1 + 18*np.cos(t)**2 - 48*np.cos(t)**4 + 32*np.cos(t)**6

n = 10000

t = np.linspace(0, 2*np.pi, n)

plt.plot(t, f(t))
plt.title('f(t)')
plt.show()

plt.plot(t, 1 + f(t) - f(t))
plt.title('1+f(t)-f(t)')
plt.show()

plt.plot(t, g(t))
plt.title('g(t)')
plt.show()

plt.plot(t, 1 + g(t) - g(t))
plt.title('1+g(t)-g(t)')
plt.show()