'''
Program to test my knowledge of boolean logic
Bug-free! Let me know if you notice any issues!
Fixes to make:
1) Find way to use question variable without making global.
'''
from sys import exit
import random

logic_dict = {
#NOT_True = {
'not False': True,
'not True': False,

#}
#OR_True = {
'True or False': True,
'True or True': True,
'False or True': True,
'False or False': False,
#}

#AND_True = {
'True and False': False,
'True and True': True,
'False and True': False,
'False and False': False,
#}

#NOT_OR_True = {
'not(True or False)': False,
'not(True or True)': False,
'not(False or True)': False,
'not(False or False)': True,
#}

#NOT_AND_True = {
'not(True and False)': True,
'not(True and True)': False,
'not(False and True)': True,
'not(False and False)': True,
#}

#not_equal_to_True = {
'1 != 0': True,
'1 != 1': False,
'0 != 1': True,
'0 != 0': False,
#}

#equals_True = {
'1 == 0': False,
'1 == 1': True,
'0 == 1': False,
'0 == 0': True
}

#function. takes a dictionary as argument and makes the dictionary keys a list.
#dictionary keys are now indexed and able to be called randomly
def listmaker(soon_to_be_list):
    new_list = []
    for key in soon_to_be_list:
        new_list.append(key)
    return new_list

#define new list of keys from logic_dict dictionary
logic_list = listmaker(logic_dict)


#since questionnaire() value will be truncated (to 't' or 'f') in function
#declare global var to be called in function logic_test()
question = None
def questionnaire():
    global question
    #pulls value from logic_list at a random index
    question = random.choice(logic_list)
    print(question,"\n")
    if logic_dict[question] == True:
        answer = 'TRUE'
    elif logic_dict[question] == False:
        answer = 'FALSE'
    else:
        print("Error with dictionary values")
        answer = None
    return answer

#function. prompts user for their answer.
def promptmaker():
    prompt = (input("Is this 'True' or 'False'?\n> "))
    #standardize inputs to match with answer from questionnaire()
    # 'Q' ends the game. unrecognized values re-prompts user for input.
    prompt = prompt.upper()
    if prompt == 'TRUE' or prompt == 'FALSE':
        pass
    elif prompt == 'T':
        prompt = 'TRUE'
    elif prompt =='F':
        prompt = 'FALSE'
    elif prompt =='Q':
        endgame("Quitting game...")
    else:
        print("Input not recognized. Please try again or enter Q to quit.")
        promptmaker()
    return prompt

def endgame(endmessage):
    print(endmessage, "\nThanks for playing!")
    exit(0)

#main function. starts game and references other functions
def logic_test():
    print("Let's play a logic game. Try to answer these questions.",
    "\nEnter Q at any time to quit.")
    #initialize variables. gameround or turns can be removed as they are redundant.
    turns = 7
    points = 0
    gameround = 1
    while turns > 0:
        print("\n\n--------\nRound", gameround)
        #get a question value from questionnaire function
        answer = questionnaire()
        #request prompt and process it using promptmaker function
        prompt = promptmaker()
        #print answer to the screen. mostly for debugging
        print(logic_dict[question])
        if answer == prompt:
            print("That is correct!")
            points += 1
        else:
            print("Sorry, that is incorrect.")
            #deactivated code: print(answer, "is not", prompt)
        turns -= 1
        gameround += 1
        #display player's standing in the game
        print("%d turn(s) left\n%d points" % (turns, points))
    endgame("---------\nHere's how you did:\n%d rounds\n%d points"\
    % (gameround - 1, points))



#run the test
if __name__ == '__main__':
    logic_test()
