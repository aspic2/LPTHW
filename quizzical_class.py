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


class QuizInit(object):

    def __init__(self, session_dict):
        self.session_dict = session_dict

    def listmaker(self):
        self.source_dict = self.session_dict
        self.newlist = []
        for key in self.source_dict:
            self.newlist.append(key)
        return self.newlist

    def questionmaker(self,somelist):
        self.question = random.choice(self.somelist)
        question = self.question
        print("Answer/Define this:")
        print("'", question, "'")
        return question

    def answerfunction(self):
        answer = input("> ")
        return answer


def finished(explanation):
    print(explanation, "\nThanks for playing!")
    sys.exit(0)


keywordsquiz = QuizInit(ex37.keywords_dict)
sessionlist = keywordsquiz.listmaker()
new_q = keywordsquiz.questionmaker(sessionlist)
print(new_q)


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
