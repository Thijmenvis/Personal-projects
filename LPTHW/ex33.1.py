i = 0
numbers = []
six = 6

def printNumbers(i):
    if i < six:
        print "at the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "numbers now: ", numbers
        print "at the bottom i is %d" % i
        printNumbers(i)
    else:
        print "the numbers: "
        for num in numbers:
            print num

printNumbers(i)
