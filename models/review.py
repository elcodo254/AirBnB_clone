#!/usr/bin/env python3
"""Defines class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents Review

    Args:
        place_id (str): place id
        user_id (str): id of user
        text (str): text for review
    """
    place_id = ""
    user_id = ""
    text = ""
