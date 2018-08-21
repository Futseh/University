# Exercise 2.15

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

print q[0][0]
print q[1]
print q[2][1]
print q[1][0]
print q[-1][-2]

for i in q:
  for j in range(len(i)):
    print(i[j])

"""
Terminal> python3 index_nested_lists.py
  a
  ['d', 'e', 'f']
  h
  d
  g
  a
  b
  c
  d
  e
  f
  g
  h
"""
