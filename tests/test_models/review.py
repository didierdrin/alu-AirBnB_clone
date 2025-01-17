#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test cases for State class"""
    
    def setUp(self):
        """Set up test method"""
        self.state = State()
        
    def test_inheritance(self):
        """Test if state inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)
        
    def test_attributes(self):
        """Test state attributes"""
        self.assertTrue(hasattr(self.state, "state"))
        
        
    def test_attributes_types(self):
        """Test if attributes are strings"""
        self.assertIsInstance(self.state.name, str)
        

if __name__ == '__main__':
    unittest.main()