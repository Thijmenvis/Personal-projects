from random import randint
from sys import exit

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # set the current scene to opening_scene() from the scenemap
        current_scene = self.scene_map.opening_scene()

        #while the current scnene is not the last scene
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene =
