import numpy as np

def f(x):
  res = []

  for i in x:
    if np.sin(i) > 0:
      res.append(np.sin(i))
    else:
      res.append(0)
  
  return res

x = np.linspace(0, 2 * np.pi, 50)
res = f(x)

for i in range(len(x)):
  print(x[i], '\t %.2f' % res[i])