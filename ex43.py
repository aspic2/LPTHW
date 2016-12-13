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

    def enter(self):
        print(description)


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    description = "Death is always right around the corner. Looks like it finally caught up with you."

    def enter(self):
        sys.exit(0)

class CentralCorridor(Scene):

    def enter(self):
        pass

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
        pass

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
