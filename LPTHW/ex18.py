# this one is like your scripts with argv
def printTwo(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def printTwoAgain(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def printOne(arg1):
    print "arg1: %r" % arg1

#this just takes one argument
def printNone():
    print "I got nothin'."

printTwo("Zed","Shaw")
printTwoAgain("Zed","Shaw")
printOne("First!")
printNone()
