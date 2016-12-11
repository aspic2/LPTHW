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



import ex37
import random
from sys import exit

session_dict = ex37.full_dict

class QuizInit(object):

    def __init__(self, session_dict):
        self.session_dict = session_dict

class ToList(QuizInit):
    def __init__(self):
        return None

    def listmaker(self, source_dict):
        self.source_dict = source_dict
        self.newlist = []
        for key in self.source_dict:
            self.newlist.append(key)
        return self.newlist

class Quizzical(QuizInit):
    def __init__(self):
        pass

    def finished(explanation):
        self.explanation = explanation
        print(self.explanation, "\nThanks for playing!")
        exit(0)

    def questionmaker(self,somelist):
        self.question = random.choice(self.somelist)
        question = self.question
        print("Please define the following value or command:")
        return self.question

    def answerfunction(self):
        self.answer = input("> ")
        return self.answer

    def quizzical(self, scoring, sessionlist):
        self.scoring = scoring
        self.sessionlist = sessionlist
        print("Time to test your knowledge!")
        self.turns = input("How many turns would you like?\n> ")
        if self.turns == "Q" or self.turns == 'q':
            Quizzical.finished("User quit")
        else:
            try:
                self.turns = int(self.turns)
                print(self.turns)
            except Exception as e:
                print("Please enter a whole number.")
                quizzical(self, scoring)
        self.points = 0
        self.gameround = 1
        while self.gameround <= self.turns:
            print("-" * 15, "\n\nRound %d" % self.gameround)
            Quizzical.questionmaker(self.sessionlist)
            Quizzical.answerfunction()
            if self.scoring == True:
                if answer == question:
                    self.points += 1
                    print("That is correct! Nice work!")
                else:
                    print("Sorry, that is incorrect.")
            else:
                print("Here is the correct answer:")
                print(QuizInit.session_dict[questionmaker.question])
            self.gameround += 1
            print("Here's your standing:\n%d turns\n%d points" % (self.turns, self.points))
        Quizzical.finished("\n\nFinished all rounds!")

quizinit = QuizInit(session_dict)
tolist = ToList()
listmaker = tolist.listmaker(session_dict)
quizzical = Quizzical()
print(listmaker)
session_quiz = quizzical.quizzical(False, listmaker)



'''
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
        kq.questionmaker(sessionlist)
        kq.answerfunction()
        if scoring == True:
            if answer == question:
                points += 1
                print("That is correct! Nice work!")
            else:
                print("Sorry, that is incorrect.")
        else:
            print("Here is the correct answer:")
            print(session_dict(questionmaker.question))
        gameround += 1
        print("Here's your standing:\n%d turns\n%d points" % (turns, points))
    finished("Nice work!")

if __name__ == '__main__':
    quizzical(False)
'''
