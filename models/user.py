from models.base_model import BaseModel

class User(BaseModel):
    """This is the User class that inherits from BaseModel class""" 
    email = ""
    password = "" 
    first_name = "" 
    last_name = ""