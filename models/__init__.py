#!/usr/bin/python3
"""
Initializes an instance of the data storage class.
"""
from .engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


storage = FileStorage()
storage.reload()
