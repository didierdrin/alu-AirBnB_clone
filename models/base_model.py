#!usr/bin/python3
"""Module for the BaseModel class"""

# import uuid
# from datetime import datetime
# import os
# import sys

# class BaseModel:
#     def __init__(self, *args, **kwargs):
#         """BaseModel class initialization"""
#         if kwargs:
#             for key, value in kwargs.items():
#                 if key == 'created_at' or key == 'update_at':
#                     value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
#                 if key != '__class__':
#                     setattr(self, key, value)
#             self.__class__ == self.__class__
#         else:
#             self.id = str(uuid.uuid4())
#             self.create_at = datetime.now()
#             self.updated_at = datetime.now()
#             from models.engine import storage
#             storage.new(self)

#     def __str__(self):
#         """String representation"""
#         return "[{}] ({}) {}".format(
#             self.__class__.__name__,
#             self.id,
#             self.__dict__
#         )

#     def save(self):
#         """Add current time & save to storage"""
#         self.updated_at = datetime.now()
#         from models.engine import storage
#         storage.save()

#     def to_dict(self):
#         """return Dictionary of BaseModel class"""
#         dictionary = self.__dict__.copy()
#         dictionary['__class__'] = self.__class__.__name__
#         dictionary['created_at'] = self.create_at.isoformat()
#         dictionary['updated_at'] = self.updated_at.isoformat()
#         return dictionary


import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel with unique ID and creation time."""

        tform = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())  # unique id converted to string
        self.created_at = datetime.now()  # current datetime for creation
        self.updated_at = datetime.now()  # updated_at same as as created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, tform))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        # Copy the instance's __dict__ and add the __class__ key
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        # Convert created_at and updated_at to ISO 8601 format strings
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result