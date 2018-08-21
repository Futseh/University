s = [1, 1]

for i in range(2, 1001):
    s.append(s[i-1] + s[i-2])
    print(s[i])