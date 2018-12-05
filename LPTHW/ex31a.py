# this is my game
from sys import argv


prompt = "> "

script, startPosition = argv

name = raw_input("what is your name?")
age = raw_input("what is your age?")

print """
%s awakens on a beach with some items by his side.
There is an axe\nAn anvil\nAnd a screwdriver\nWhich one do you wanna pick up?
""" % (name)
pickupOne = raw_input(prompt)
if startPosition = 1
    if "screwdriver" in pickupOne:
        inventory = "screwdriver"
        print "you picked up the screwdriver"
    elif "anvil" in pickupOne:
        inventory = "anvil"
        print "for some reason you thought the anvil was useful"
    elif "axe" in pickupOne:
        inventory = "axe"
        print "you picked up the axe. Wise choice"
    else:
        inventory = "nothing"
        print "that's not a real answer"

elif startPosition = 2:
print "after you decided to take the %s. You decided to look around." % inventory
print "there isn't much to see exept for some trees."
print "there also is a mountain with a smoke plume coming out of it."



# commands
