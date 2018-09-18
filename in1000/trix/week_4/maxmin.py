nums = [6, -4,  7, -2, 8, -3, 9, -11]

res = 0

for i in nums:
    if i < res:
        res = i

print(res)

for i in nums:
    if i > res:
        res = i

print(res)

"""
Terminal> python3 maxmin.py
    -11
    9
"""