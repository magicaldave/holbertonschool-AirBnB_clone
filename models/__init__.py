#!/usr/bin/python3
"""
Initializes an instance of the data storage class.
"""
from .engine.file_storage import FileStorage
from models import base_model
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
