#!/usr/bin/python3
"""Defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initializes the Base.
        Args:
            *args: list of arguments
            **kwargs: named arguments
        """
	if kwargs:
            datetime_isoformat = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], datetime_isoformat)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], datetime_isoformat)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
	    models.storage.new(self)

    def __str__(self):
        """Returns a readable string representation
        of BaseModel instances"""

        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        """Updates the instance attribute updated_at
        with the current datetime"""

        self.updated_at = datetime.now()
	models.storage.save()

    def to_dict(self):
        """returns all
        keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__

	return new_dict
