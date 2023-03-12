#!/usr/bin/env python3
"""Define class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents place model.

    Args:
        city_id (str): city id
        user_id (str): user id
        name (str): name of place
        description (str): description of the place
        number_room (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): price of the place per night
        latitude (float): latitude to the place
        longitude (float): longitude to the place
        amenity_ids (list): list of amenities
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
