#!/usr/bin/python3
"""Module city
Module containing city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class for representing a City"""

    state_id = ""
    name = ""
