#!/usr/bin/env python3
"""Defines base class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents class basemodel."""
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel

        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, fmt)
                else:
                    self.__dict__[k] = v

    def save(self):
        """updates attribute updated_at with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the instance.__class__ included to represent the class name of
        the object
        Is the first piece of serialization/deserializtation process
        """
        dict1 = self.__dict__.copy()
        dict1["created_at"] = self.created_at.isoformat()
        dict1["updated_at"] = self.updated_at.isoformat()
        dict1["__class__"] = type(self).__name__
        return dict1

    def __str__(self):
        """Returns str representation of the BaseModel"""
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
