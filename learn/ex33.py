i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
# adds i to numbers while i is still under 6
    numbers.append(i)
# adds 1 every time the while loop runs (which is until i becomes 6)
    i = i + 1
    print "numbers now: ", numbers
    print "at the bottom i is %d" % i

print "the numbers: "

# runs until there are no more numbers in the list to print.
for num in numbers:
    print num
