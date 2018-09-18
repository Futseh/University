import numpy as np

np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})

P = np.matrix(((.9871, .0027), (.0129, .9973)))
x = (1, 0)

for i in range(1, 101):
    print(i)
    print(np.dot(P**i, x))