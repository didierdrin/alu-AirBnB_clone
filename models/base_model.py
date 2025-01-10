#!usr/bin/python3
"""Module for the BaseModel class"""
import uuid 
from datetime import datetime 
import os
import sys  
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


class BaseModel: 
    def __init__(self, *args, **kwargs):
        """BaseModel class initialization"""
        if kwargs: 
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'update_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__': 
                    setattr(self, key, value) 
            self.__class__ == self.__class__  
        else:
            self.id = str(uuid.uuid4()) 
            self.create_at = datetime.now() 
            self.updated_at = datetime.now() 
            from models.engine import storage 
            storage.new(self) 
    
    def __str__(self): 
        """String representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, 
            self.id, 
            self.__dict__
        )        
    
    def save(self):
        """Add current time & save to storage"""
        self.updated_at = datetime.now() 
        from models.engine import storage  
        storage.save() 

    def to_dict(self): 
        """return Dictionary of BaseModel class""" 
        dictionary = self.__dict__.copy() 
        dictionary['__class__'] = self.__class__.__name__ 
        dictionary['created_at'] = self.create_at.isoformat() 
        dictionary['updated_at'] = self.updated_at.isoformat() 
        return dictionary  
    
