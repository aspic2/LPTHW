#New Adventure style game.
#Trapped at the zoo
'''Player gets trapped at zoo after dark. Various scenes follow where player:
    travels to different areas,
    enters different enclosures, and
    meets new animal friends.

Animals can:
    talk to player,
    help player, or
    harm player.

There will be challenges throughout where player must:
    identify friends and foes,
    decide which direction to go,
    solve a puzzle,
    etc.
'''

'''Object structure:

Character
    -name
    -health
    -speak()

    Player
    Animal
        snake
        giraffe
        monkey
        tiger
        penguin
        bugs
            beetle
            ant
            bee

Zoo [map]

Scene
    Enclosure
        polar
        safari/jungle
        monkey
        marine

Impasse [obstacles]
'''

class Character(object):

    def __init__(self, name):
        self.name = name
        self.health = 100

    def speak(self, sentence):
        print(self.name, "\b:", sentence)


miket = Character("Michael T")

miket.speak("Daz wuz up!")
