import numpy as np

np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})

P = np.matrix(((.3355, .3682, .3067, .0389), (.2663, .2723, .3277, .5451),
               (.1935, .1502, .1589, .2395), (.3047, .2093, .2067, .1765)))

for i in range(2, 6):
    print(i)
    print(P**i)