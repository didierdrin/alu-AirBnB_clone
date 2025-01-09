import json     
from models.base_model import BaseModel 

class FileStorage:   
    """Deserialization & Serialization of instances to a JSON file"""
    __file_path = "file.json" 
    __objects = {} 

    def all(self): 
        """Return the dictionary __objects.""" 
        return self.__objects 
    
    def new(self, objekt): 
        """Sets in __objects -> objekt with key id"""
        key = f"{objekt.__class__.__name__}.{objekt.id}"
        self.__objects[key] = objekt 

    def save(self): 
        """__objects serialization""" 
        with open(self.__file_path, 'w') as f: 
            json.dump({key: objekt.to_dict() for key, objekt in self.__objects.items()}, f) 

    def reload(self): 
        """__objects Deserialization""" 
        try: 
            with open(self.__file_path, 'r') as f:  
                for key, value in json.load(f).items():
                    self.__objects = {key: self.classes()[value["__class__"]](**value)}
        except FileNotFoundError:  
            pass 

    def classes(self): 
        """Dictionary of valid classes & their references"""
        return { 
            "BaseModel": BaseModel, 
        }