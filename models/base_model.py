#!/usr/bin/env python3
"""Defines base class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents class basemodel."""
    def __init__(self):
        """Initializes BaseModel

        Args:
            id (string) : id of an instance
            created_at (datetime) : datetime at creation of instance
            updated_at (datetime) : datetime at instance creation;updated
        """

        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

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
