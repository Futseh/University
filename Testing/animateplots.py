import numpy as np
import matplotlib.pyplot as plt

n = 1000

a = 3.0
b = 5.0

t = np.linspace(0, 10*np.pi, n)
x = np.zeros(n)
y = np.zeros(n)

fig = plt.figure(1)
ax = fig.add_subplot(111)

for i in range(n):
    x[i] = 16 * np.sin(t[i])**3
    y[i] = 13 * np.cos(t[i]) - 5 * np.cos(2*t[i]) - 2 * np.cos(3*t[i]) - np.cos(4*t[i])
        
    plt.cla()
    ax.plot(x[:i], y[:i])
    plt.pause(0.001)

plt.show(block=True)    