#!/usr/bin/env python3
"""Module that contains the entry point of the command interpreter"""
import cmd

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


CLASSES = [
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review"
]


def check_args(args):
    """Checks validity of arguments
    Args:
        args (str): string of arguments passed to a command

        Returns:
            Error message if args is None or not a valid class else the args
    """
    arg_list = args.split()

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
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

    def do_create(self, argv):
        """creates new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if (args := check_args(argv)) is not None:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, argv):
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

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if (arg_list := check_args(argv)) is not None:
            if len(arg_list) == 1:
                print("** instance id is missing**")
            else:
                key = "{}.{}".format(*arg_list)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, argv):
        """"Prints all string reps of all instances, based or not, on the class
        name"""
        arg_list = argv.split()
        objects = storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_update(self, argv):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        if (arg_list := check_args(argv)) is not None:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = f"{arg_list[0]}.{arg_list[1]}"
                if instance_id in storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
