#!/usr/bin/python3
"""
File Storage Engine Module
"""

import json
from os.path import exists


class FileStorage:
    """
    Rudimentary class for file-based data storage
    """
    __file_path = 'testdata.json'
    __objects = {}  # type: dict[int, str]

    def all(self):
        """
        Returns objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Stores an object inside the object tracker
        """
        self.__objects[f"{obj.__class__.__name__}.{obj['id']}"] = obj
        print(self.__objects)

    def save(self):
        """
        Saves all object instances to a file.
        """
        with open(self.__file_path, mode="w",
                  encoding="utf-8") as outinstances:
            json.dump(self.__objects, outinstances)

    def reload(self):
        """
        Deserializes a JSON-ified object from the filesystem.
        """
        if exists(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as ininstances:
                self.__objects = json.load(ininstances)
