#centralize the quiz functions and just import appropriate dicts
'''
functions/processes for this script:
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

Instructions: dictionaries imported at the top of the script.
Set session_dict to the correct dictionary, and reset quizzical
argument at bottom (and in turns try/except) to True or False
'''



import ex37
import ex27v2
import ex41
import random
from sys import exit

#session_dict = ex27v2.logic_dict
session_dict = ex37.full_dict
session_dict = ex41.oop_phrases

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

    def finished(self, explanation):
        self.explanation = explanation
        print(self.explanation, "\nThanks for playing!")
        exit(0)

    def questionmaker(self,source_list):
        self.source_list = source_list
        self.question = random.choice(self.source_list)
        print("Please define the following value or command:")
        print(self.question)
        return self.question

    def userresponse(self):
        self.response = input("> ")
        if self.response == 'q' or self.response == 'Q':
            quizzical.finished("User quit")
        else:
            return self.response

    def start_quiz(self, scoring, sessionlist):
        self.scoring = scoring
        self.sessionlist = sessionlist
        print("Time to test your knowledge!")
        self.turns = input("How many turns would you like?\n> ")
        if self.turns == "Q" or self.turns == 'q':
            quizzical.finished("User quit")
        else:
            try:
                self.turns = int(self.turns)
            except Exception as e:
                print("Please enter a whole number.")
                start_quiz(self, scoring, sessionlist)
        self.points = 0
        self.gameround = 1
        while self.gameround <= self.turns:
            print("-" * 15, "\n\nRound %d:    %d points" % (self.gameround, self.points))
            turn_q = quizzical.questionmaker(sessionlist)
            turn_r = quizzical.userresponse()
            correct_a = str(quizinit.session_dict[turn_q])
            if self.scoring == True:
                correct_a = correct_a.lower()
                turn_r = session_r.lower()
                if turn_r == correct_a:
                    self.points += 1
                    print("That is correct! Nice work!")
                else:
                    print("Sorry, that is incorrect.")
                    print("Here is the correct answer:")
                    print(correct_a)
            else:
                print("Here is the correct answer:")
                print(correct_a)
            self.gameround += 1
        quizzical.finished("\n\nFinished all %d rounds with %d points!" % (self.turns, self.points))


quizinit = QuizInit(session_dict)
tolist = ToList()
made_list = tolist.listmaker(session_dict)
quizzical = Quizzical()

if __name__ == '__main__':
    session_quiz = quizzical.start_quiz(False, made_list)
