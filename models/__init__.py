#!/usr/bin/python3
"""
Initializes an instance of the data storage class.
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
