#!/usr/bin/python3
"""Module console
Creating command interpreter console
"""


import cmd
import readline


class HBNBCommand(cmd.Cmd):
    """class for console"""

    prompt = "(hbnb)"

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()