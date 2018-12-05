theCount = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in theCount:
    print "This is count %d" % number

# same as above. It can be the same name..... confusing.
for fruits in fruits:
    print "A fruit of type: %s" % fruits

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
# link to array docs:
# https://docs.python.org/2/library/array.html?highlight=array#module-array
elements = []

# then use the range function to do 0 to 5 counts
for i in range (0, 20):
    print "Adding %d to the list." % i
    # append is a function that lists understand. it adds i to the elements list
    # specifically at the end.
    elements.append(i)

# range(start, stop, step)
# range(stop)
# This is a versatile function to create lists containing arithmetic progressions. It is most often used in for loops. The arguments must be plain integers. If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0. The full form returns a list of plain integers [start, start + step, start + 2 * step, ...]. If step is positive, the last element is the largest start + i * step less than stop; if step is negative, the last element is the smallest start + i * step greater than stop. step must not be zero (or else ValueError is raised).
elements.range()


# python docs: array.append(x)
# Append a new item with value x to the end of the array.

# no we can print them out too
for i in elements:
    print "element was %d" % i
