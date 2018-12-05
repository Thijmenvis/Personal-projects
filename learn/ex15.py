from sys import argv

script, filename = argv

#opens the filename you typed in
txt = open(filename)

# prints out the file
print "Here's your file %r:" % filename
print txt.read()

# asks for a filename using raw_input()
print "Type the filename again:"
fileAgain = raw_input('> ')

# loads fileAgain into textAgain
textAgain = open(fileAgain)

# prints out the second the second file, called by raw_input()
print textAgain.read()
