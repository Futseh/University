# Exercise 2.13

ia = 100
p = 5.5
amount = ia
years = 0

while amount <= 1.5 * ia:
  amount = amount + (p / (100 * amount))
  years = years + 1

print(years)

"""
Terminal> python3 interest_rate_loop.py
  113637
"""
