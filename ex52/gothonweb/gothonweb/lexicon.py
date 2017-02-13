# dictionary of recognized words
# words are matched with their type and sent to parser.py
# where they become sentences that the app can understand

def scan(userinput):
    # create list or dictionary of parts of speech, maybe expected
    # words for input
    vocab = {'north': 'direction', 'south': 'direction', 'east': 'direction',
    'west': 'direction', 'down': 'direction', 'up': 'direction',
    'left': 'direction', 'right': 'direction', 'back': 'direction',
    'forward': 'direction', 'eat': 'verb', 'go': 'verb', 'kill': 'verb',
    'place': 'verb', 'run': 'verb', 'set': 'verb', 'stop': 'verb',
    'tell': 'verb', 'throw': 'verb', 'the': 'stop', 'in': 'stop', 'of': 'stop',
    'from': 'stop', 'door': 'noun', 'bear': 'noun',
    'princess': 'noun', 'cabinet': 'noun'
    }

    words = userinput.lower().split()
    #split userinput into separate words and punctuation
    #make list of tuples containing userinput words and their types
    matchedwords = []
    for word in words:
        if word in vocab:
            matchedwords.append((vocab[word], word))
        else:
            try:
                word = int(word)
                matchedwords.append(('number', word))
            except ValueError:
                matchedwords.append(('error', word))

    #create sentence by using putting tuple list words in order by type
    return matchedwords
