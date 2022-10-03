#!/usr/bin/python3
"""module user
containes data for user module
"""


import email
from ssl import _PasswordType
from models.base_model import BaseModel


class  User(BaseModel):
    """Class representing User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
