from models.base_model import BaseModel 

class Review(BaseModel): 
    """Review class it inherits from BaseModel """
    place_id = "" 
    user_id = "" 
    text = "" 

