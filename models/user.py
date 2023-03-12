#!/usr/bin/python3
"""Define User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents class user

    Args:
        email (str): email of the user
        password (str): user password
        first_name (str): first name of the user
        last_name (str): last name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
