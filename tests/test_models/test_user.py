#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test cases for User class"""
    
    def setUp(self):
        """Set up test method"""
        self.user = User()
        
    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)
        
    def test_attributes(self):
        """Test User attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        
    def test_attributes_types(self):
        """Test if attributes are strings"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

if __name__ == '__main__':
    unittest.main()