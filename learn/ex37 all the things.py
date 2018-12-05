#and
True and False == False
#as. part of the with-as statement
with x as y: pass
#assert. assert (ensure) that something is true.
assert False, "Error!"
#break. stop this loop right now.
while True: break
#class. define a class
class Person(object)
#continue. don't process more of the loop
while True: continue
#def. define a function.
def X(): pass
#del. delete from dictionary
del X[Y]
#elif. else if condition.
if: X
elif: Y
else: J
#else.
if: X
elif: Y
else: J
#except. if an exception happens, do this.
except ValueError, e: print e
#exec. run a string as python (execute)
exec 'print "hello"'
#finally. exceptions or nog, finally do this no matter what.
finally:pass
#for. loop over a collection of things.
for X in Y: pass
#from. importing specific parts of a module.
from x import Y
#global. declare that you want a global variable.
global X
#if. if condition.
if: X;
elif: Y
else: J
#import. import a module into this one to use.
import os
#in. part of for-loops. also a test of X in Y.
for X in Y: pass
1 in [1] == True
"string" in "stringcheese" == True
#is. like == to test equality
1 is 1 == True
#lambda. create a short anonymous function.
s = lambda y: y ** y: s(3)
#not. logical not.
not True == False
#or. logical or.
True or False == True
#pass. this block is empty
def empty(): pass
#print. print this string
print 'this string'
#raise. raise an exception when things go wrong.
raise ValueError("no")
#return. exit the function with a return value.
def X(): return Y
#try. try this block, and if exception, go to excerpt.
try: pass
#while. while loop
while X: pass
#with. with an expression as a variable do.
with X as Y: pass
#yield. pause here and return to caller.
def X(): yield Y; X().next()

# __DataTypes__

#True
#False
True of False == True
False and True == False
#None
x = None
#strings
x = "hello"
#numbers
i = 100
#floats
i = 10.2245
#lists
j = [1,2,3,4]
#dicts
e = {'x': 1, 'y': 2}

# __string formats__
# all of them start with %

# %d decimal integers(not floating point)
"%d" % 45 =='45'
# %i same as %d
"%i" % 45 =='45'
# %o octal number
"%o" % 1000 == '1750'
# %u unsigned decimal
"%u" % -1000 == '-1000'
# %x hexadecimal lowercase
"%x" % 1000 == '3e8'
# %X hexadecimal uppercase
"%X" % 1000 == '3E8'
# %e exponntial notation, lowercase 'e'
"%e" % 1000 == '1.000000e+03'
# %E exponential notation, uppercase 'E'
"%E" % 1000 == '1.000000E+03'
# %f floating point real number.
"%f" % 10.34 == '10.340000'
# %F same as %f
"%F" % 10.34 == '10.340000'
# %g either %e or %f, whichever is shorter.
"%g" % 10.34 == '10.34'
