#!/usr/bin/python3
"""module user
containes data for user module
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class representing User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
