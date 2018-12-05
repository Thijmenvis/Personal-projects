import random

def flairOrNot():
    attack = ["kill", "murder", "slay", "attack", "stab"]
    grab = ["grab", "take", "steal"]
    walk = ["go to", "walk", "run", "sneak"]
    interact = ["open", "enter", "interact"]
# commands
# weapons and armor to choose from
itemTypes = ["weapons", "armor"]
weapons = ["sword", "dagger", "bow", "staff"]
armor = ["chestplate", "platelegs", "helmet"]
# novelty tags
beforeOrAfter = ['before', 'after']
tagsBefore = ["Dorians ", "mythril ", "adamantium "]
tagsAfter = [" of Gondor", " of Gold", " of magic"]

# choose a random weapon or armorpiece
def generateItemWithPrompt():
    max = raw_input("how many items to generate? > ")
    max = int(max)

    for x in range(max):
        tagChoice = random.choice(beforeOrAfter)
        itemTypeChoice = random.choice(itemTypes)

        tagAcopy = ''
        tagBCopy = ''

        # chooses a random tag
        if tagChoice == 'before':
            tagBCopy = list(tagsBefore)
            tagBCopy = random.choice(tagBCopy)
        elif tagChoice == 'after':
            tagAcopy = list(tagsAfter)
            tagAcopy = random.choice(tagAcopy)
        else:
            print 'error tagchoice'

        if itemTypeChoice == 'weapons':
            itemchoice = list(weapons)
        elif itemTypeChoice == 'armor':
            itemchoice = list(armor)
        else:
            print 'error itemchoice'

        print tagBCopy + random.choice(itemchoice) + tagAcopy

def generateItem():
    tagChoice = random.choice(beforeOrAfter)
    itemTypeChoice = random.choice(itemTypes)

    tagAcopy = ''
    tagBCopy = ''

    # chooses a random tag
    if tagChoice == 'before':
        tagBCopy = list(tagsBefore)
        tagBCopy = random.choice(tagBCopy)
    elif tagChoice == 'after':
        tagAcopy = list(tagsAfter)
        tagAcopy = random.choice(tagAcopy)
    else:
        print 'error tagchoice'

    if itemTypeChoice == 'weapons':
        itemchoice = list(weapons)
    elif itemTypeChoice == 'armor':
        itemchoice = list(armor)
    else:
        print 'error itemchoice'

    item = tagBCopy + random.choice(itemchoice) + tagAcopy
    print "You got a: %r" % item

def firstRoom():
    print "You are in a dark room"
    print "There is a chest in front of you with an item in it"

    prompt = raw_input("Will you take it? > ")

    if prompt == "yes":
        print ''
        generateItem()
    elif prompt == "no":
        print "why?"
    else:
        print "I can't understand that"

def test():
    test = ['stuff', 'otherstuff', 'thirdstuff']

    prompt = raw_input("> ")
    flair = False

    for x in prompt:
        flair = True

    if flair == True:
        print "you did it with style"
    elif flair == False:
        print "you did it sloppily"






#firstRoom()
test()
# weapon and armor stats.
# weapon rarity. Generate a better weapon/armorpiece if higher rarity.
