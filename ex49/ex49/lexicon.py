#scanner project goes here

def scan(userinput):
    #create list or dictionary of parts of speech, maybe expected
    #words for input
    '''directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    verbs = ['go', 'stop', 'kill', 'eat']
    stops = ['the', 'in', 'of', 'from']
    nouns = ['door', 'bear', 'princess', 'cabinet']
    '''
    
    vocab = {'north': 'direction', 'south': 'direction', 'east': 'direction',
    'west': 'direction', 'down': 'direction', 'up': 'direction',
    'left': 'direction', 'right': 'direction', 'back': 'direction', 'go': 'verb',
    'stop': 'verb', 'kill': 'verb', 'eat': 'verb', 'the': 'stop', 'in': 'stop',
    'of': 'stop', 'from': 'stop', 'door': 'noun', 'bear': 'noun',
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
