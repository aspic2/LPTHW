#centralize the quiz functions and just import appropriate dicts
'''
Instructions: dictionaries imported at the top of the script.
Set session_dict to the correct dictionary, and reset quizzical
argument at bottom (and in turns try/except) to True or False
'''

#from ex27v2 import logic_dict
from ex37 import full_dict
#from ex41 import oop_phrases
import random
from sys import exit


session_dict = full_dict


def listmaker(source_dict):
    newlist = []
    for key in source_dict:
        newlist.append(key)
    return newlist

'''!!!change this to the correct dictionary!!!'''
sessionlist = listmaker(session_dict)

def questionmaker(question_list):
    question = random.choice(question_list)
    print(question)
    return question

def finished(explanation):
    print(explanation, "\nThanks for playing!")
    exit(0)

def userresponse():
    response = input("> ")
    if response == 'Q' or response == 'q':
        finished("User quit.")
    else:
        return response

def quizzical(scoring):
    print("Time to test your knowledge!")
    print("Follow the prompts on the screen or type 'q' to quit.")
    turns = input("How many turns would you like?\n> ")
    if turns == 'Q' or turns == 'q':
        finished("User quit")
    else:
        try:
            turns = int(turns)
        except Exception as e:
            print("Please enter a whole number.\n\n")
#is there a way to connect this value to the original argument?
            quizzical(False)

    points = 0
    gameround = 1
    while gameround <= turns:
        print("-" * 15, "\n\nRound %d:    %d points" % (gameround, points))
        print("Please define the following value or command:")
        turn_q = questionmaker(sessionlist)
        turn_r = userresponse()
        #Ensure all boolean values are strings
        correct_a = str(session_dict[turn_q])
        if scoring == True:
            lower_turn_r = turn_r.lower()
            lower_correct_a = correct_a.lower()
            if lower_turn_r == lower_correct_a:
                points += 1
                print("That is correct! Nice work!")
            else:
                print("Sorry, that is incorrect. Here is the correct answer: ")
                print(correct_a)
        else:
            print("Here is the correct answer: ")
            print(correct_a)
        gameround += 1
    finished("\n\nFinished all %d rounds with %d points!" %(turns, points))



if __name__ == '__main__':
    #quizzical(True)
    quizzical(False)
