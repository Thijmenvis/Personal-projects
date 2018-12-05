def fib(index):
    a = 0
    fiblist = [1, 1]

    for _ in range(index):
        print(fiblist)
        fibvar = fiblist[-_] + fiblist[-_-1]
        fiblist.append(fibvar)
        a += 1
    return fiblist

print(fib(10))
