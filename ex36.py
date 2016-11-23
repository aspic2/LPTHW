#Second attempt to write a boolean memorization game

'''Game map:
1. Create different methods (functions) for each group of boolean questions.
2. Initialize the boolean statements as variables. The variables should have
    'True' or 'False' associated to them.
3. Set a number of turns or lives for the player. Iterate through each group
    until lives or turns is up.
4. Handle errant input
'''
def main():
    print("Welcome to the boolean challenge!")
    turns = input("How many turns would you like?\n> ")
    try:
        turns = int(turns)
        if turns < 1 or turns > 26:
            print("Please enter an integer from 1 to 26\n> ")
            main()
    except ValueError:
        print("Please enter an integer from 1 to 26\n> ")
        main()
    print("%d turns, huh? Alright. Get ready!" % turns)
    gametime()

def gametime():
    while turns > 0:



main()


#def NOT_True:
not_false = not False
not_true = not True
#print(not_true)

#def OR_True:
true_or_False = True or False
true_or_true = True or True
false_or_true = False or True
false_or_false = False or False
#print(false_or_false)

#def AND_True:
true_and_false = True and False
true_and_true = True and True
false_and_true = False and True
false_and_false = False and False
#print(false_and_false)

#def NOT_OR_True:
not_true_or_false = not(True or False)
not_true_or_true = not(True or True)
not_false_or_true = not(False or True)
not_false_or_false = not(False or False)
#print(not_false_or_false)

#def NOT_AND_True:
not_true_and_false = not(True and False)
not_true_and_true = not(True and True)
not_false_and_true = not(False and True)
not_false_and_false = not(False and False)
#print(not_false_and_false)

#def not_equal_to_True:
one_not_equal_zero = (1 != 0)
one_not_equal_one = (1 != 1) #False
zero_not_equal_1 = (0 != 1) #True,
zero_not_equal_zero = (0 != 0) #False,
#print(one_not_equal_zero)

#def equals_True:
one_equals_zero = (1 == 0) #False,
one_equals_one = (1 == 1) #True,
zero_equals_one = (0 == 1) #False,
zero_equals_zero = (0 == 0) #True
#print(zero_equals_zero)
