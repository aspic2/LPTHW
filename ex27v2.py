#Program to test my knowledge of boolean logic

import random

#error.




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


def listmaker(soon_to_be_list):
    new_list = []
    for key in soon_to_be_list:
        new_list.append(key)
    return new_list

logic_list = listmaker(logic_dict)

def promptmaker():
    prompt = (input("Is this 'True' or 'False'?\n> "))
    #print(prompt)
    prompt = prompt.lower()
    if 't' in prompt:
        prompt = 't'
    elif 'f' in prompt:
        prompt = 'f'
    else:
        print("Error with prompt value. Please try again.")
    return prompt

def questionnaire():
    question = random.choice(logic_list)
    print(question,"\n")
    #print(question in logic_dict, "\n\n")
    if (question in logic_dict) == True:
        question = 't'
    elif (question in logic_dict) == False:
        question = 'f'
    else:
        print("Error with dictionary values")
        question = None
    return question

def logic_test():
    print("Let's play a logic game. Answer these questions as best you can.")
    turns = 7
    points = 0
    gameround = 1
    while turns > 0:
        print("\n\nRound", gameround)
        question = questionnaire()
        prompt = promptmaker()
        print(question)
        if question == prompt:
            print("That is correct!")
            points += 1
            turns -= 1
            gameround += 1
            print(turns, "turns left\n", points, "points")
        else:
            print("Sorry, that is incorrect.")
            print(question, "is not", prompt)
            turns -= 1
            gameround += 1
            print(turns, "turns left\n", points, "points")



logic_test()
