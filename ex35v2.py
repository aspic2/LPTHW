from sys import exit

#creates next room
def gold_room():
    print("This room is full of gold. How much do you take?")
#take user input for amount of gold
#revise choice logic. as of now, can only be input containing a 0 or 1. For example:
#'25' is not valid. but 'F13' is.
#3 attempted solutions:
    choice = input("Enter an integer. No units\n> ")

#1) check if input is in list of digits option. NOT WORKING
    '''
    choice = input("please enter a value ")
    numbers = []
    for num in range(10):
        numbers.append(num)
    print(numbers)
    choice_list = []
    for value in choice:
        value = int(value)
        choice_list.append(value)
    print(choice_list)
    if choice_list in numbers:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    '''


#2) original logic
    '''
    if "0" in choice or "1" in choice:
        how_much = int(choice)

    else:
        dead("Man, learn to type a number.")
    '''


#3) try/catch option
    try:
        how_much = int(choice)
        pass
    except ValueError:
        dead("Man, learn to type a number.")


    if how_much < 50:
        print("Nice, you're not greedy! You win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    print("Bear moved: %r.\n Type 'take honey' or 'taunt bear'." % bear_moved)

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you, then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
            print("type 'open door' to move to the next room.")
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print("You died.", why)
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")
    choice = choice.lower()

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")



start()
