#!/usr/bin/env python3
"""Module that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


def check_args(args):
    """Checks validity of arguments
    Args:
        args (str): string of arguments passed to a command

        Returns:
            Error message if args is None or not a valid class else the args
    """
    __classes = [
            "BaseModel",
            ]

    arg_list = args.split()

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in __classes:
        print("** class doesn't exist **")
    else:
        return arg_list


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

    def do_create(self, argv: str):
        """creates new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if (args := check_args(argv)) is not None:
            print(eval(args[0])().id)
            storage.save()
            
    def do_show(self, argv: str):
        """Prints the string representation of an instance based on
        the class name and id.
        """
        if (args := check_args(argv)) is not None:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

            
if __name__ == "__main__":
    HBNBCommand().cmdloop()
