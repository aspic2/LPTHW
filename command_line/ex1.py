#basic command line prompts quiz
#design a quiz for these, one that determines your OS

import platform
import random
import sys

windows_commands = {
'pwd': 'print working directory',
'hostname': "my computer's network name",
'mkdir': 'make directory',
'cd': 'change directory',
'ls': 'list directory',
'rmdir': 'remove directory',
'pushd': 'push directory',
'popd': 'pop directory',
'cd': 'copy a file or directory',
'robocopy': 'robust copy',
'mv': 'move a file or directory',
'more': 'page through a file',
'type': 'print the whole file',
'forfiles': 'run a command on lots of files',
'dir -r': 'find files',
'select-string': 'find things inside files',
'help': 'read a manual page',
'helpctr': 'find what man page is appropriate',
'echo': 'print some arguments',
'set': 'export/set a new environment variable',
'exit': 'exit the shell',
'runas': 'DANGER! become super user root DANGER!'
}

mac_commands = {
'pwd': 'print working directory',
'hostname': "my computer's network name",
'mkdir': 'make directory',
'cd': 'change directory',
'ls': 'list directory',
'rmdir': 'remove directory',
'pushd': 'push directory',
'popd': 'pop directory',
'cp': 'copy a file or directory',
'mv': 'move a file or directory',
'less': 'page through a file',
'cat': 'print the whole file',
'xargs': 'execute arguments',
'find': 'find files',
'grep': 'find things inside files',
'man': 'read a manual page',
'apropos': 'find what man page is appropriate',
'env': 'look at your environment',
'echo': 'print some arguments',
'export': 'export/set a new environment variable',
'exit': 'exit the shell',
'sudo': 'DANGER! become super user root DANGER!'
}

def finished(reason):
    print(reason, "\nThanks for playing!")
    sys.exit(0)


def which_os():
    system = platform.system()
    system.lower()
    return system

session_os = which_os()
print("You are running a %s device. Generating dictionary..." % session_os)

def proper_dict(x):
    if x == 'Windows':
        dictionary = windows_commands
    else:
        dictionary = mac_commands
    return dictionary

session_dict = proper_dict(session_os)

def listmaker(dictionary):
    newlist = []
    for key in dictionary:
        newlist.append(key)
    return newlist

command_list = listmaker(session_dict)


def user_input():
    response = input("> ")
    if response == 'q':
        finished("User quit")
    else:
        return response

def honesty():
    resp = input("> ")
    resp = resp.lower()
    if resp == 'y' or resp == 'n':
        pass
    elif resp == 'q':
        finished("User quit")
    elif resp =='yes':
        resp = 'y'
    elif resp == 'no':
        resp = 'n'
    else:
        print("invalid input. please try again.")
        honesty()
    return resp

#variable source is a list from which to choose questions
def questions(source):
    print("No quiz this time. Just iterate through the answers.")
    turns = 15
    gameround = 1
    points = 0
    while turns > 0:
        print("-" * 20, "\n Round %d" % gameround)
        current_question = random.choice(source)
        print("What does this command do?", "\n%s" % current_question)
        user_input()
        print("The answer is:")
        print(session_dict[current_question])
        print("Are you correct?", "\n \n \n")
        turns -= 1
        gameround += 1
        '''
        honesty()
        if honesty() == 'y':
            points += 1
        else:
            print("Thanks for your honesty. Still, you don't get points.")
        turns -= 1
        print("%d turns left" % turns)
        '''
    print("Nice work. Here's your score. \n")
    print("%d points over %d turns." % (points, turns))
    finished("End of game")


questions(command_list)
