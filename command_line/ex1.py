#basic command line prompts
#design a quiz for these, one that determines your OS

import platform
import random


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

def what_os():
    system = platform.system()
    system.lower()
    return system

print(what_os())

def sort_the_dict(opsys):
    promptlist = []
    if opsys == 'Windows':
        dictionary = windows_commands
    else:
        dictionary = mac_commands
    for key in dictionary:
        promptlist.append(key)
    return promptlist

print(sort_the_dict(what_os()))
