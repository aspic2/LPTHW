#Zed's quiz on OOP syntax
'''
Things to revise:
1) fix 'gameround' logic in while block. Currently stops only at multiples of 6.
2) Better organization of sections. Callable functions, maybe. (or classes)
3) write a Quit function besides CTRL-D
4) Parser to grade user input and turn into game with points system
'''


import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%)":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***):":
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@):":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    #readline returns byte characters. decode and return as string, then add to WORDS
    WORDS.append(str(word.strip(),'utf-8'))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


#keep going until they hit CTRL-D
#edit: adding a number of turns until end
gameround = 1
try:
    while gameround < 12:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            print("Round %d" % gameround)
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)


            input("> ")
            print("ANSWER: %s\n\n" % answer)
            gameround += 1
    print("-" * 15, "\nEnd of quiz")
    sys.exit(0)
except EOFError:
    print("\nBye")
