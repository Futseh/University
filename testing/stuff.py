import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 21)
y = np.linspace(-10, 10, 21)

lin1x = []
lin1y = []
lin2x = []
lin2y = []

for i in x:
    for j in y:
        if i + 3*j + 4 == 0:
            lin1x.append(i)
            lin1y.append(j)
        
        if i + 3*j - 4 == 0:
            lin2x.append(i)
            lin2y.append(j)

plt.plot(lin1x, lin1y)
plt.plot(lin2x, lin2y)
plt.plot([i for i in range(-5, 6)], [0 for i in range(-5, 6)])

plt.show()