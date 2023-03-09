#!/usr/bin/env python3
"""Module that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines HBNB command intepreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """command to execute an empty line + <ENTER>"""
        pass

    def do_EOF(self):
        """command to execute Ctrl-c(EOF)"""
        print("")
        return True

    def do_quit(self, status: int):
        """command to exit the console"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
