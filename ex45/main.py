
import Scenes
import characters

class GameMap(object):
    scenes = {
    'bed': Bed,
    'bedroom': Bedroom,
    'gym': Gym,
    'home': Home,
    'jail': Jail,
    'death': Death,
    'publictrans': PublicTrans,
    'kitchen': Kitchen,
    'quit': Quit,
    'workplace': Workplace
    }


class Gameplay(object):
    def __init__(self, first_scene):
        self.first_scene = first_scene
        self.last_scene = Bed

    def play(self):
        print("-" * 50)
        print("ONE DAY AT A TIME")
        current_scene = self.first_scene
        final = self.last_scene
        while current_scene != final:
            current_scene = current_scene.enter_scene()



protag = Characters.Protagonist('Michael')
protag.live()

new_game = Gameplay(Scenes.Bedroom)

if __name__ == '__main__':
    new_game.play()
