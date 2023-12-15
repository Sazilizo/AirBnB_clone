#!/usr/bin/python3
""" A models module for the AirBnB clone"""

import uuid
from datetime import datetime

class BaseModel:
    """Aclass that defines thebase class for the AirBnB clone"""


    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

    def __str__(self):
        """returns the string representation of the class"""

        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates attribute updated_at by the current date and time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary with the keys-values pairs of __dict__"""

        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = type(self).__name__
        dict_rep["created_at"] = dict_rep["created_at"].isoformat()
        dict_rep["updated_at"] = dict_rep["updated_at"].isoformat()

        return dict_rep

