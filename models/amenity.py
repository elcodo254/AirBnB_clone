#!/usr/bin/python3
"""Define class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents amenity.

    Args:
        name (str): name of the ammenity
    """
    name = ""
