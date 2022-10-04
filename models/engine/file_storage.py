#!/usr/bin/python3
"""
File Storage Engine Module
"""

import json
from os.path import exists
import models
import datetime


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
                old_instances = json.load(ininstances)
                for key in old_instances:
                    self.__objects[key] = getattr(
                        models,
                        old_instances[key]['__class__'])(**old_instances[key])

    def attributes(self):
        """Returns the valid attributes and their types for classname."""

        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
