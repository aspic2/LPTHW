'''
Program to test my knowledge of boolean logic
Bug-free! Let me know if you notice any issues!
#future edits: 1) make promptmaker function less exploitable.
2) Add real ending to game
'''
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

#function. prompts user for their answer.
def promptmaker():
    prompt = (input("Is this 'True' or 'False'?\n> "))
    #makes input all lowercase. Facilitates matching
    prompt = prompt.lower()
    #redefine prompt as 't' if there's a t in the answer or 'f' if there's an f
    #could be exploited, but also allows for misspelled answers to be evaluated
    if 't' in prompt:
        prompt = 't'
    elif 'f' in prompt:
        prompt = 'f'
    else:
        print("Error with prompt value. Please try again.")
        promptmaker()
    return prompt

def questionnaire():
    #pulls value from logic_list at a random index
    question = random.choice(logic_list)
    #print question. print new line
    print(question,"\n")
    #look up question variable as key in logic_dict. compare value found
    #render answer as 't' or 'f' for matching with prompt. Or print error.
    if logic_dict[question] == True:
        answer = 't'
    elif logic_dict[question] == False:
        answer = 'f'
    else:
        print("Error with dictionary values")
        answer = None
    return answer

#main function. starts game and references other functions
def logic_test():
    print("Let's play a logic game. Answer these questions as best you can.")
    #initialize variables. gameround or turns can be removed. redundant.
    turns = 7
    points = 0
    gameround = 1
    #Run thr game until there are no turns left
    while turns > 0:
        #print current round
        print("\n\nRound", gameround)
        #get a question value from questionnaire function
        answer = questionnaire()
        #request prompt and process it using promptmaker function
        prompt = promptmaker()
        #print answer to the screen. mostly for debugging
        print(answer)
        #logic for if answer is correct or incorrect.
        if answer == prompt:
            print("That is correct!")
            #increment values accordingly
            points += 1
            turns -= 1
            gameround += 1
            #display player's standing in the game
            print(turns, "turns left\n", points, "points")
        else:
            print("Sorry, that is incorrect.")
            print(answer, "is not", prompt)
            #increment all but points.
            turns -= 1
            gameround += 1
            print(turns, "turns left\n", points, "points")
    print("Thanks for playing! Here's your standing:\n",
    (gameround - 1), "rounds", "\n", points, "points")




logic_test()
