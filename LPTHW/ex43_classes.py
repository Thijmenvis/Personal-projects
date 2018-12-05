from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "this scene is not finished"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        # the init makes a new variable that takes the variable when engine(variable)
        # was used and makes it available for use in this class as scene_map. 
        # scene map is central corridor in the beginning (a_map)
        self.scene_map = scene_map

    def play(self):
        # sets the variable current_scene to the opening scene in scene_map
        current_scene = self.scene_map.opening_scene()
        # sets the variable last_scene to the finished class.
        last_scene = self.scene_map.next_scene('finished')

        # while the current scene is not the last scene (finished)
        while current_scene != last_scene:
            # next_scene_name is equal to the current scene .enter (the first lines
            # of dialogue)
            next_scene_name = current_scene.enter()
            # the current scene is the scene
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "you died, you kinda suck at this.",
        "your mom would be proud... if she were smarter.",
        "such a loser.",
        "i have a small puppy that's better at this"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "the gothons of planet percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an"
        print "escape pod.\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking  the door to the"
        print "Armory and about to pull a weapon to blast you"

        action = raw_input("> ")

        if action == "shoot":
            print "he dodges you and gets enraged and eats you"
            return 'death'
        elif action == "dodge":
            print "you slip and pass out. When you wake up he eats you"
            return 'death'
        elif action == "tell a joke":
            print "it is so funny he gets distracted and after killing him"
            print "you jump through to the Weapon Armory door."
            return 'laser_weapon_armory'
        else:
            print "Does not compute"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "you quickly scan the armory room. You see the neutron bomb in its"
        print "container. There is a keypad on it. If you get the code wrong 10 times"
        print "the lock closes forever. Better get it right. The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZZD"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "you got the bomb and run to the bridge"
            return 'the_bridge'
        else:
            print "that's was your last try. you sit contemplating your failure"
            print "as the gothons blow up your ship"
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "you enter the bridge and see 5 gothons fiddeling with the helm"
        print "they are weary of the bomb under your arm so they seem hesitant"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "you panic and throw the bomb"
            print "it beeps a little and you pray for your life as you see"
            print "the counter reach 0"
            return 'death'
        elif action == "slowly place the bomb":
            print "you place the bomb down and set the timer. all the while paying"
            print "attention to the gothons that are looking"
            print "you jump into the escape shoot that goes to the pods"
            return 'escape_pod'
        else:
            print "does not compute"
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print "there are 5 pods in varying states of disrepair. which one do you take?"
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "the pod is bad and immediately explodes when you enter it"
            return 'death'
        else:
            print "you jump into pod %s and hit the eject button" % guess
            print "you escape successfully"
            return 'finished'

class Finished(Scene):

    def enter(self):
        print "you won, good job"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    #whenever you call next_scene('test') it will return a val with
    #a value that corresponds with the key 'test'
    # map.scenes.get('test') searches in a dictonary named scenes in the class map
    # for the key with the name test and then returns the corresponding value.
    def next_scene(self, scene_name):
        val = map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
