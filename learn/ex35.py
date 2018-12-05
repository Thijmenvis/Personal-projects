from sys import exit

def goldRoom():
    print "this room is full of gold. how much do you take?"

    choice = raw_input("> ")

    if "0" in choice or "1" in choice:
        howMuch = int(choice)
    else:
        dead("Man, learn to type a number.")

    if howMuch < 50:
        print "nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("you greedy bastard!")

def bearRoom():
    print "There is a bear here.\nThe bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bearMoved = True

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("the bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bearMoved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bearMoved:
            goldRoom()
        else:
            print "i got no idea what that means"

def cthulhuRoom():
    print "Here you see the great evil cthulhu.\nHe, it, whatever stares at you"
    print "and you go insane.\nDo you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhuRoom()

def dead(why):
    print why, "good job!"
    exit(0)

def start():
    print "you are in a dark room.\nThere is a door to your right and left."
    print "which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bearRoom()
    elif choice =="right":
        cthulhuRoom()
    else:
        dead("You stumble around the room until you starve.")

start()
