#scanner project goes here

def scan(userinput):
    vocab = {'north': 'direction'}
    words = userinput.lower().split()
    #create list or dictionary of parts of speech, maybe expected
    #words for input
    #split userinput into separate words and punctuation
    #make list of tuples containing userinput words and their types
    #create sentence by using putting tuple list words in order by type 
    print(words)

    #for word in words:
    #    if word in vocab:




userinput = "Ample parking day or night. People shouting \"Howdy, neighbor!\""

scan(userinput)
