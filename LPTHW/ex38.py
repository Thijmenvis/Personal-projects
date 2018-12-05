tenThings = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# make a list from a string. splitting the items at each space in this case.
# also deletes the spaces
stuff = tenThings.split(' ')
print stuff
moreStuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

# len(list)
# counts how many items are in a list
while len(stuff) != 10:
    nextOne = moreStuff.pop()
    print "Adding: ", nextOne
    stuff.append(nextOne)
    print "there are %d items now." % len(stuff)

print ""
print "there we go: ", stuff

print "let's do some things with stuff"

# first item in list
print stuff[1]
# last item in list.
print stuff[-1]
# pops off the last item in the list
print stuff.pop()
# string.join(iterable)
# return a string with before the string before .
# stuffed in between each thing in the iterable list.
# [1:7] = start at 1 and end before 7 range.
# 7 - 1 = 6 items printed.
print ' '.join(stuff)
print '#'.join(stuff[2:6])
