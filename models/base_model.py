#!/usr/bin/python3
"""
Base model for AirBnB Project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Main Class Body"""

    def __init__(self, *args, **kwargs):
        """ Initializer Function """

        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.updated_at = self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Prints string representation of the data object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the datetime and saves the object.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary with all object data.
        """
        return dict(self.__dict__,
                    __class__=self.__class__.__name__,
                    updated_at=str(self.updated_at.isoformat()),
                    created_at=str(self.created_at.isoformat()))
