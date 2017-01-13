import Scenes

class Character(object):
    name = None
    health = 100


class Protagonist(Character):
    def __init__(self, name):
        self.points = 0
        self.health = 50
        self.name = name
        self.isAlive = True
        #name = input("What is your name?\n> ")
        print("Hello, %s. You have been initialized." % self.name)

    def live(self):
        if self.health <= 0:
            self.isAlive = False
            print("That was the final blow. Your poor withered body couldn't take it.")
            return Scenes.Death.enter_scene()
        return None

    def change_health(self, change):
        if self.health + change > 100:
            self.health = 100
        elif self.health + change <= 0:
            self.health = 0
        else:
            self.health += change
        print("%s, your health is now at %d" % (self.name, self.health))
        return self.health

    def change_points(self, points):
        self.points += points
        return self.points


protag = Protagonist('Michael')
protag.live()
