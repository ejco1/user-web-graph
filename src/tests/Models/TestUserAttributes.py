import unittest
from src.tests.util.TestCaseUtil import TestCaseUtil
from src.main.Models.UserAttributes import UserAttributes

class TestUserAttributes(unittest.TestCase):

    def test_PayloadPrint(self):
        payloadString = TestCaseUtil.generateAttributesPayload()
        testFields = UserAttributes()
        testFields.updateAttribute('id', 'test123')
        testFields.updateAttribute('name', 'Ethan')
        testFields.updateAttribute('color', 'blue')
        testFields.updateAttribute('waa', 'wee')
        self.assertEqual(payloadString, testFields.printAttributes())

if __name__ == '__main__':
    unittest.main()