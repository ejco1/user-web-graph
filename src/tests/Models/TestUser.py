import unittest
from src.tests.util.TestCaseUtil import TestCaseUtil
from src.main.Models.User import User

class TestUser(unittest.TestCase):
    def test_SchemaValues(self):
        testUser = User()
        testChild = User()
        testUserId = testUser.getField('id')
        testChildId = testChild.getField('id')

        testUser.addChild(testChild)
        testChild = User()
        self.assertNotEqual
        
