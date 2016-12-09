#centralize the quiz functions and just import appropriate dicts

import appropriate dictionaries

def listmaker(source_dict):
    new_list = []
    for key in source_dict:
        newlist.append(key)
    return newlist

sessionlist = listmaker(source_dict)

def prompt():
    pass

def finished():
    pass

def answerfunction():
    pass


def quizzical(turns):
    turns = input("> ")
    points = 0
    gameround = 1
    gameround = turns - gameround
    while gameround <= turns:
        print("-" * 15, "\n\nRound %d" % gameround)
        question = questionfunction()
        answer = answerfunction()
        if answer == question:
            points += 1
            print("That is correct! Nice work!")
        else:
            print("Sorry, that is incorrect.")
        gameround += 1
        print("Here's your standing:\n%d turns\n%d points" % (turns, points))
    finished("Nice work!")
