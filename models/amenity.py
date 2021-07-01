#!/usr/bin/python3
"""
Module containing the class Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity representation"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of the class amenity"""
        super().__init__(*args, **kwargs)
