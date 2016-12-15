#finish the map (variable names) and the Engine to run

'''
Aliens have invaded a space ship and our hero has to go through a
 maze of rooms defeating them so he can escape into an escape pod to
 the planet below. The game will be more like a Zork or Adventure type
 game with text outputs and funny ways to die. The game will involve
 an engine that runs a map full of rooms or scenes. Each room will
 print its own description when the player enters it and then tell the
 engine what room to run next out of the map.
 '''
'''
*Player initializes. *Player moves to first *Scene. Player completes Scene.task
Player moves to next Scene

'''

'''
Scenes
    v(description)
    f(gameplay)
    -Bridge
    -Central Corridor
    -Death
    -Escape Pod
    -Laser Weapon Armory

Engine
    list of scenes
    f(next scene)
Character
    v(name)
    v(health)
    f(attack)
    f(enter scene)
    -Player
    -Gothons
Bomb
    v(T till explosion)
    v(location)
    f(explode)
    f(disarm)
Map
    v(list of scenes)
    v(player location)
    v(queue engine)
'''

from sys import exit
import random



class Scene(object):

    def __init__(self):
        self.completed = False
        self.description = None

    def enter(self):
        print(self.description)





class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('youwin')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene

class Death(Scene):

    description = "Death is always right around the corner. \
    \nLooks like it finally caught up with you."

    def enter():
        print(Death.description)
        return exit(0)


class CentralCorridor(Scene):

    description = "This is the Central Corridor.\nYou find yourself in an unfamiliar dark hallway, and your head hurts.\nYou look around to get your bearings. You realize you are on an alien ship.\nJudging by the view out the window, it is headed for planet Percal #25.\n\nYou need to get out of here, and quick. There's no escape once you reach the planet.\nThese ships typically have ecape pods, so you'll need to find one to get away.\nAdditionally, you will need to clear the ship of Gothons so they don't chase you down."

    def enter():
        print(CentralCorridor.description)
        step1 = input("Do you head forward through the hall or back?\n> ")
        if step1 == 'forward':
            print("You run into your first Gothon")
            step2 = input("You can fight, run, or outdance it. Which do you choose?\n> ")
            if 'outdance' in step2:
                print("That Gothon was no match for your moves.")
                print("You proceed to the Light Weapons Armory.")
                return 'lwa'
            else:
                print("That was a bad idea.")
                print("Gothons are fast and very good at fighting.")
                return 'death'
        else:
            print("You stall and stall. Eventually you land on Percal #25.")
            print("The Gothons disembark the ship and find you cowering in a corner.")
            print("They rip you to shreds.")
            return 'death'




class Player(object):
    def __init__(self, name):
        self.name = name

    def enter_scene():
        pass

class LaserWeaponArmory(Scene):

    description = "This is the Laser Weapon Armory. To your surprise, there are more than laser weapons in here. You find a pretty cool bomb that you think can take out the whole ship. You hatch a plan to time it to detonate after some minutes, which should give you enough time to escape."

    def enter():
        print(LaserWeaponArmory.description)
        print("The bomb has a keypad lock on it. Can you guess the one digit code keeping it locked? (Gothons are not very good at weapons security.)")
        correct_code = random.randint(0,10)
        print(correct_code)
        tries = 0
        while tries < 10:
            guess = input("Enter a number\n> ")
            try:
                guess = int(guess)
            except ValueError:
                print("Don't be a funny guy. Enter a regular keypad number.")
                LaserWeaponArmory.enter()
            if guess != correct_code:
                print("\a\a\a\aBZZZZDT!")
                tries += 1
                print("Try again. %d more chances." % 10 - tries)
            else:
                print("Nice. You have 10 minutes on the clock.")
                print("Take that bomb to the Bridge and blow this ship to smithereens!")
                return 'bridge'
        print("Out of chances. The bomb has engaged with 5 seconds on the clock. Realizing you can't outrun it, you stand there with a sad look on your face and await your fate.")
        return 'death'



class TheBridge(Scene):

    description = "This is The Bridge. There are several Gothons guarding it, too many to outdance, even for you. You try to sneak up on them, but they hear you and point their guns at you"

    def enter():
        print(TheBridge.description)
        step1 = input("Do you give up or try to outsmart them?\n> ")
        if step1 == 'outsmart':
            print("'Smart' thinking! You point your gun at the bomb. They know what that means and they slowly back away from you. Two more come by, see what's going on and sneak away as though they were never here. You have set the bomb and now need to get out of here.")
            return 'ep'
        else:
            print("You sniveling worm. After all this work, you give up?")
            return 'death'

class EscapePod(Scene):

    description = "This is the Escape Pod. Pick one and go!"

    def enter():
        print(EscapePod.description)
        step1 = input("There are three pods here. Do you want pod 1, 2, or 3?\n> ")
        if step1 == '1' or step1 == '2' or step1 == '3':
            return 'youwin'
        else:
            print("You really should listen to me more...")
            return 'death'


class YouWin(Scene):

    description = "Nice work! You picked a good pod and you blast out into space. A few seconds go by and you hear a shockwave. The Gothon shop ignited like a sun. You sit back, relax, and catch some Z's as you head home."

    def enter():
        print(Death.description)
        return exit(0)


class Map(object):

    scenes = {
    'cc': CentralCorridor.enter(),
    'lwa': LaserWeaponArmory.enter(),
    'bridge': TheBridge.enter(),
    'ep': EscapePod.enter(),
    'death': Death.enter(),
    'youwin': YouWin.enter()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        Map.scenes[scene_name]

    def opening_scene(self):
        Map.scenes['cc']


#my version
start_map = Map('cc')
new_game = Engine(start_map)
new_game.play()
