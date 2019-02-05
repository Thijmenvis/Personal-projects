s = 0
for _ in range(1000):
    if _ % 3 == 0:
        s += _
    elif _ % 5 == 0:
        s += _
    else:
        continue

print(s)
