#You make a game.
#Fun game
'''Make a game with more than one way to reach the end.

Title: Making it through the day

Premise: Perform a series of daily actions, and have the character survive.

Objects

Characters:
    player
    antagonists?
        wife
        workplace bully

Scenes:
    Home
      Bedroom
      Kitchen
      Garage
    Public Trans
    Workplace
      Desk
      Lunchroom
    Gym
    Jail
    Death
'''

import random
from sys import exit
from Characters import protag


class Scene(object):
    def __init__(self):
        self.description = description
        self.been_here = False

    def enter_scene():
        pass


class Death(Scene):

    def enter_scene():
        print("You up?\nYa dead.")
        print("%s, here is your score:\n%d points" % (protag.name, protag.points))
        exit(0)


class Home(Scene):
    description = "Your home. Your hallway."
    been_here = False

    def enter_scene():
        print(Home.description)
        return Home.decision_time()

    def decision_time():
        if Workplace.been_here:
            print("Long day, huh? Why don't you get some rest?")
            next_step = input("Kitchen or Bed?\n> ").lower()
            if 'kitchen' in next_step:
                'kitchen'
            elif 'bed' in next_step:
                'bed'
        decision = input("Where to? Kitchen, Work, or back to bed?\n> ").lower()
        if "work" in decision or "out" in decision:
            return 'garage'
        elif 'kitchen' in decision:
            return 'kitchen'
        elif 'bed' in decision:
            return 'bed'
        else:
            print("Invalid input.")
            Home.decision_time()

    #returns only home locations
    #return Bedroom
    #return Kitchen
    #return Garage


class Bedroom(Scene):
    description = ("This is your bedroom.",
    "You awake to a beam of sunrise on your face.",
    "Someone didn't close the blinds last night.",
    "You sit up to find your room a mess. Not out of the ordinary.")
    ending = False

    def enter_scene():
        for line in Bedroom.description:
            print(line)
        return Bedroom.decision_time()

    def decision_time():
        print("Are you ready to get up and start the day?")
        decision = input("Y or N:\n> ").lower()
        if decision == 'y':
            print("Every day is a new adventure!\nThis adventure begins in the hallway\n")
            protag.change_points(10)
            return 'home'
        else:
            print("You stay in bed and avoid your problems.")
            print("It's a nice, safe choice, but also condemns you to mediocrity.")
            print("That's the prce to pay for comfort. As long as you're happy...")
            return 'death'


class Kitchen(Scene):
    description = ("Eat well. You are going to need your strength today.", "This meal of pancakes, and syrup should do the trick.")
    been_here = False

    def enter_scene():
        if Kitchen.been_here:
            print("No more food for you, tubby.")
            protag.change_points(-5)
        else:
            for line in Kitchen.description:
                print(line)
            protag.change_health(50)
            protag.change_points(10)
            protag.live()
            Kitchen.been_here = True
        return 'home'


class Bed(Scene):
    description = ("Somehow you managed to make it through the day without something killing you.",\
    "The sad part is you must do it all over again tomorrow.",\
    "Pyhrric victory, if I have ever seen one.")

    def enter_scene():
        for line in Bed.description:
            print(line)
        print("%s, here is your score:\n%d points" % (protag.name, protag.points))
        exit(0)


class Garage(Scene):
    description = 'This is the garage.'
    been_here = False

    def enter_scene():
        print(Garage.description)
        if Garage.been_here:
            print("Welcome Home")
            return 'home'
        print("Time to head out!")

        Garage.been_here = True
        return 'publictrans'


class PublicTrans(Scene):
    description = ("You decide to take the train.",\
    "Saving money, saving the environment, go you!")
    been_here = False

    def enter_scene():
        for line in PublicTrans.description:
            print(line)
        return PublicTrans.decision_time()

    def decision_time():
        if PublicTrans.been_here:
            print("What a day it has been!")
            decision = input("Want to head home or to the gym?\n> ")
            if 'gym' in decision:
                return 'gym'
            return 'home'
        print("\nIn comes a troublemaker, asking for money.")
        decision = input("What do you do: give money or ignore?\n> ")
        if 'give' in decision or 'money' in decision:
            print("That troublemaker thanks you, then pisses on your leg.", "Yuck!")
            protag.change_health(-10)
            protag.change_points(30)
        elif 'ignore' in decision:
            print("You hold up your WSJ magazine and pretend like you didn't hear anything.")
            print("The troublemaker proceeds to beat you up and then piss on your leg.")
            print("Yuck!")
            protag.change_health(-70)
            protag.change_points(-10)
        else:
            print("Invalid input")
            'publictrans'
        PublicTrans.been_here = True
        protag.live()
        protag.change_points(10)
        return 'workplace'


class Workplace(Scene):
    description = "This is your workplace."
    been_here = False

    def enter_scene():
        print(Workplace.description)
        print("Workplace decisions. Do work or not. Eat lunch out or in cafeteria. etc.")
        Workplace.been_here = True
        return Workplace.decision_time()

    def decision_time():
        print("You are at your desk. You see 300 new emails in your inbox.")
        decision = input("Do you get to work or ignore your duties?\n> ")
        if 'work' in decision:
            print("Well aren't you a good little employee?")
            print("The boss comes by and pats you on the back.")
            print("\tB: \"Nice work, %s.\nI am sure you can burn through this extra stuff in no time!\"" % protag.name)
            print("The boss gives you 5 more assignments to take care of today.\n\n")
            print("You go to the breakroom", "grab some coffee,"\
            "return to your desk",\
            "and bury your head in work for the rest of the day.")
            protag.change_points(50)
        elif 'ignore' in decision:
            print("The boss comes by and sees you on Twitter.")
            print('\tB: Where\'s that report I asked you for, %s?' % protag.name)
            print("You are fired on the spot.", "At least now you get to leave...")
            protag.change_health(-30)
            protag.change_points(-10)
            protag.live()
            return 'publictrans'
        d2 = input("Some nerd from accounting has some questions for you.\nDo you assist him or beat him up?\n> ")
        if 'assist' in d2:
            print("\n\nThe nerd thanks you for your help.")
            print("Afterwards, nerdy mentions how helpful you are to your boss.")
            print("You get a nice bonus and the rest of the day off.")
            protag.change_health(+20)
            protag.change_points(50)
            protag.live()
            return 'publictrans'
        elif 'beat' in d2:
            print("I hope that got some stress out of your system because you are going to jail.")
            protag.change_points(10)
            return 'jail'

    #return Desk
    #return Lunchroom

class Gym(object):
    description = ("Time to pump some iron!", "Why don't you start out small?")

    def enter_scene():
        for line in Gym.description:
            print(line)
        print("This place is empty. You look at all the weight systems at your disposal.")
        return Gym.decision_time()

    def decision_time():
        decision = input("Do you start out small or go big?\n> ").lower()
        if 'small' in decision:
            print("Safety first! You get some good reps in and start looking tone.")
            protag.change_points(20)
        elif 'big' in decision:
            print("Go big or go home!")
            print("You grab a barbell with way too much weight for power cleans",\
            "and fracture every bone in your lower body")
            protag.change_health(-90)
            protag.change_points(-10)
            protag.live()
        d2 = input("Where to now?\nHome, Work, or just Away?\n> ").lower()
        if 'home' in d2:
            return 'home'
        elif 'work' in d2:
            return 'workplace'
        else:
            print("I didn't understand your input.")
            Gym.decision_time()


class Jail(Scene):
    def enter_scene():
        print("This is the end. I don't have any decisions for you to make here.",\
        "You just get beat up and die. So, uh, enjoy that.")
        lastwords = input("Any last words?\n> ")
        print('Later, at your jail death...',\
        '\n\tAnd his last words were "%s".' % lastwords)
        print('Rest in Power')
        protag.change_points(100)
        return 'death'


class Quit(Scene):
    def enter_scene():
        print('User Quit.\n"Hey, man, I get it. Life\'s tough. Be well."')
        exit(0)


class Away(Scene):
    def enter_scene():
        print("Your first good decision all day.")
        print("Run away from your problems. Out of sight, out of mind, I always say.")
        return 'bed'
