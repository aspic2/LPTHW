'''
Aliens have invaded a space ship and our hero has to go through a
 maze of rooms defeating them so he can escape into an escape pod to
 the planet below. The game will be more like a Zork or Adventure type
 game with text outputs and funny ways to die. The game will involve
 an engine that runs a map full of rooms or scenes. Each room will
 print its own description when the player enters it and then tell the
 engine what room to run next out of the map.
 '''

class Scene(object):
    description = None

    def __init__(self):
        self.completed = False
        while completed = False:
            print(description)
            self.enter()

    def enter(self):
        start_scene()



class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = Map.maps

    def play(self):
        pass

class Death(Scene):

    description = "Death is always right around the corner. \
    \nLooks like it finally caught up with you."

    def enter(self, description):
        sys.exit(0)

class CentralCorridor(Scene):

    description = "You find yourself in an unfamiliar dark hallway, and your\
    head hurts. You look around to get your bearings. You realize you are on\
    an alien ship. Judging by the view out the window, it is headed for\
    planet Perscal #25\n\nYou need to get out of here, and quick. There's no\
    escape once you reach the planet.\nThese ships typically have ecape\
    pods, so you'll need to find one to get away."

    completed = False
    while completed is False:

    def enter(self):
            print(description)





class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        maps = [central_corridor, laser_weapon_armory, the_bridge,
        escape_pod, death]

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

'''
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
'''

deathscene = Death.enter()

deathscene
