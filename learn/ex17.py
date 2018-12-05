from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print "Copying from %s to %s." % (fromFile, toFile)

# we could do these two on one line, how?
inFile = open(fromFile)
inData = inFile.read()

# inData = open(fromFile).read() #?

print "the input file is %d bytes long" % len(inData)
print "Ready, hit RETURN to continue, CTRL-c to abort."
raw_input()

outFile = open(toFile, 'w')
outFile.write(inData)

print "Alright, all done."

outFile.close()
inFile.close()
