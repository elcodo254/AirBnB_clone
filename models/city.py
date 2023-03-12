#!/usr/bin/python3
"""Defines City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents City

    Args:
        state_id (str): identity of state
        name (str): name of city
    """
    state_id = ""
    name = ""
