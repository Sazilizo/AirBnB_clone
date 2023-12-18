#!/usr/bin/env python3

import uuid
from datetime import datetime
"""This module is containes a class defining the base of the AirBnB clone
"""

class BaseModel:
	"""
	a class defining the baseodel of the airBnB clone
	"""
	def __init__(self, id, created_at, updated_at):
		self.id = uuid.uuid4()
		self.created_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
		self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
	def __str__(self):
		print("{} {} {}".format(self.__class__.__name__, self.id, self.__dict__))

	def save(self):
		self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
	def to_dict(self):
		"""keys/values of the instance"""
        	new_dict = self.__dict__.copy()
        	new_dict['updated_at'] = self.updated_at.isoformat()
        	new_dict['created_at'] = self.created_at.isoformat()
        	new_dict['__class__'] = self.__class__.__name__
		
		return new_dict
