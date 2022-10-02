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
    # Path to data
    __file_path = 'testdata.json'
    # Stores all objects by <name>.<name.id>
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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Saves all object instances to a file.
        """
        with open(self.__file_path, 'w', encoding='utf-8') as outinstances:
            json.dump(
                {
                    k: (v.to_dict() if not isinstance(v, dict) else v)
                    for (k, v) in self.__objects.items()
                }, outinstances)

    def reload(self):
        """
        Deserializes a JSON-ified object from the filesystem.
        """
        if exists(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as ininstances:
                self.__objects = json.load(ininstances)
