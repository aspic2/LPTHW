#centralize the quiz functions and just import appropriate dicts
#revisit commandline arguments. find way to input dictionaries from there
'''functions/processes for this script:
    import dict(s)
    function: make list from dicts
        return list or Error
    function: pull random question from list
        return question or Error
    function: request input from user
        return input or Error
    function: evaluate user input and question
        increment points or move on
    function: exit game
        at end of turns or when user prompts exit
'''


import appropriate dictionaries
import random
from sys import exit




def listmaker(source_dict):
    new_list = []
    for key in source_dict:
        newlist.append(key)
    return newlist

sessionlist = listmaker(source_dict)

def questionmaker(x):
    question = random.choice(x)
    print(question)
    return question


def finished(explanation):
    print(explanation, "\nThanks for playing!")
    sys.exit(0)

def answerfunction():
    answer = input("> ")
    return answer


def quizzical(scoring):
    print("Time to test your knowledge!")
    turns = input("How many turns would you like?\n> ")
    try:
        turns = int(turns)
    except Exception as e:
        raise ValueError
        print("Please enter a whole number.")
        quizzical(turns)
    points = 0
    gameround = 1
    gameround = turns - gameround
    while gameround <= turns:
        print("-" * 15, "\n\nRound %d" % gameround)
        questionmaker()
        answerfunction()
        if scoring == True:
            if answer == question:
                points += 1
                print("That is correct! Nice work!")
            else:
                print("Sorry, that is incorrect.")
        else:
            print("Here is the correct answer:")
            print(source_dict(questionmaker.question))
        gameround += 1
        print("Here's your standing:\n%d turns\n%d points" % (turns, points))
    finished("Nice work!")

if __name__ == '__main__':
    quizzical(False)
