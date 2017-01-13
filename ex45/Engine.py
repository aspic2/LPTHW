
import Scenes
from Characters import protag

class GameMap(object):
    scenes = {
    'away': Scenes.Away,
    'bed': Scenes.Bed,
    'bedroom': Scenes.Bedroom,
    'gym': Scenes.Gym,
    'home': Scenes.Home,
    'jail': Scenes.Jail,
    'death': Scenes.Death,
    'publictrans': Scenes.PublicTrans,
    'kitchen': Scenes.Kitchen,
    'quit': Scenes.Quit,
    'workplace': Scenes.Workplace
    }


class Gameplay(object):
    def __init__(self, first_scene):
        self.first_scene = first_scene
        self.last_scene = Scenes.Bed

    def play(self):
        print("-" * 50)
        print("ONE DAY AT A TIME")
        current_scene = self.first_scene
        final = self.last_scene
        while current_scene != final:
            current_scene = current_scene.enter_scene()



new_game = Gameplay(Scenes.Bedroom)


new_game.play()
