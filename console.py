#!/usr/bin/python3
"""Module console
Creating command interpreter console
"""


import cmd
import readline


class HBNBCommand(cmd.Cmd):
    """class for console"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """handles end of line char"""
        return True

    def emptyline(self):
        """does nothing on enter"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
