from math import sqrt

# f = [1,1]
# maxval = 4000000
# fvar = 0
# k = 0

def F(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return F(n-1)+F(n-2)


def Fib(n):
    return ((1+sqrt(5))**n - (1-sqrt(5))**n) / (2**n*sqrt(5))

var = 1
stuff = []
fibvar = 0
while fibvar < 4000000:
    fibvar = Fib(var)
    if fibvar % 2 == 0:
        stuff.append(int(fibvar))
        continue
    else:
        continue

print(stuff)



# while f[::-1][0] < maxval :
#     fvar = f[k] + f[k+1]
#     print (fvar)
#     if fvar % 2 == 0:
#         f.append(fvar)
#         k += 1
#         continue
#     else:
#         k += 1
#
# print(fvar)
#
# sumOfEvens = sum(f)
# print(sumOfEvens)
