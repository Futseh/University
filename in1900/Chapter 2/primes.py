# Exercise 2.3

primes = [2, 3, 5, 7, 11, 13]

for i in range(0, len(primes), 1):
  print(primes[i])

p = 17
primes.append(p)

print(primes)

"""
Terminal> python3 primes.py
  2
  3
  5
  7
  11
  13
  [2, 3, 5, 7, 11, 13, 17]
"""
