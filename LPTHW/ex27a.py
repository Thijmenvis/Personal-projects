a = True and True # True
b = False and True # False
c = 1 == 1 and 2 == 1 # False
d = "test" == "test" # True
e = 1 == 1 or 2 != 1 # True
f = True and 1 == 1 # True
g = False and 0 != 0 # False
h = True or 1 == 1  # True
i = "test" == "testing" # False
j = 1 != 0 and 2 == 1 # False
k = "test" != "testing" # True
l = "test" == 1 # False
m = not (True and False)  # True
n = not (1 == 1 and 0 != 1) # False
o = not (10 == 1 or 1000 == 1000) # False
p = not (1 != 10 or 3 == 4) # False
q = not ("testing" == "testing" and "Zed" == "Cool Guy") # True
r = 1 == 1 and (not ("testing" == 1 or 1 == 0)) # True
s = "chunky" == "bacon" and (not (3 == 4 or 3 == 3)) # False
t = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) # False

print a
print b
print c
print d
print e
print f
print g
print h
print i
print j
print k
print l
print m
print n
print o
print "p: %r" % p # made one mistake here
print q
print r
print s
print t
