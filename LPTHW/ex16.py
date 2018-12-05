from sys import argv

script, filename = argv

print "we're going to erase %r." % filename
print "If you don't want that, hit CTRL-C"
print "If you do wan't that hit RETURN."

raw_input("?")

# the 'w' is to say to the open method that I can write to the file.
print "Opening the file"
target = open(filename, 'w')

print "truncating the file..."
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
