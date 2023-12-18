#!/usr/bin/python3

"""A module that creates a user for the AirBnB project"""

from models.base_model import BaseModel

class User(BaseModel):
	"""class that creates a user based on BaseModel parent class"""

	email = ""
	password = ""
	first_name = ""
	last_name = ""
