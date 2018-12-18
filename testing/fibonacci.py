import numpy as np

s = [1, 1]

for i in range(2, 1001):
    s.append(s[i-1] + s[i-2])
    #print(float(s[i]) / float(s[i-1]))

api = 0
sign = 1.0
for i in range(1, 1000000000000, 2):
    api += sign * 1.0 / i
    sign = -sign
    print(np.pi / 4 - api, i)