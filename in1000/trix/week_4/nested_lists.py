olist = []
starlist = []
rutenett = []

for i in range(5):
    olist.append('o')
    starlist.append('*')

rutenett.append(olist)
rutenett.append(starlist)
rutenett.append(olist)

for i in range(3):
    print(rutenett[i])

"""
Terminal> python3 nested_lists.py
    ['o', 'o', 'o', 'o', 'o']
    ['*', '*', '*', '*', '*']
    ['o', 'o', 'o', 'o', 'o']
"""