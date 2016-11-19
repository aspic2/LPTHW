#Program to test my knowledge of boolean logic

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
'not(False and True)':	True,
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

def logic_test():
    print("Let's play a game of logic.\nTell me if this is true or not. ")
    turns = 7
    points = 0
    while turns > 0:
        question = random.choice(list(logic_dict))
        prompt = (input("Is this 'True' or 'False'? "), question)
        print(prompt)
        if prompt == question:
            print("That is correct!")
            points += 1
            turns -= 1
            print(turns, "turns left\n", points, "points")
        else:
            print("Sorry, that is incorrect. ")
            turns -= 1
            print(turns, "turns left\n", points, "points")

logic_test()

'''
assign value (True or False) to each logic question

put questions into numbered list

call random list object. Have user input answer

return value of list object
'''
