million = 100

def collatz(startNr):
    x = startNr/2
    y = 3*x + 1
    return (x, y)

lst = []

for n in range(million):
    x = n
    while x != 1:
        first = x/2
        lst.append(first)
        second = first*3 + 1
        lst.append(second)

print(lst)
