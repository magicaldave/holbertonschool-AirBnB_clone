#!/usr/bin/python3
"""
Base model for AirBnB Project
"""

from uuid import uuid4
from datetime import datetime
from .__init__ import storage


class BaseModel:
    """Main Class Body"""

    def __init__(self, *args, **kwargs):
        """ Initializer Function """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.updated_at = self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints string representation of the data object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        For now, simply updates date of the object.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary with all object data.
        """
        return dict(self.__dict__,
                    __class__=self.__class__.__name__,
                    updated_at=self.updated_at.isoformat(),
                    created_at=self.created_at.isoformat())
