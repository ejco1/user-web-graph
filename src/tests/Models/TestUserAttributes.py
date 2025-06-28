import unittest
from src.tests.util.TestCaseUtil import TestCaseUtil
from src.main.Models.UserAttributes import UserAttributes

class TestUserAttributes(unittest.TestCase):
## This tests that regardless of updates,
# These values will always exist.
    def test_SchemaValues(self):
        testFieldsObject = UserAttributes()
        testFields = TestCaseUtil.loadAsJSON(testFieldsObject.toString())
        self.assertIn("id", testFields)
        self.assertIn("name", testFields)
        self.assertIn("color", testFields)
        self.assertIn("extraAttributes", testFields)
    
    def test_basicFieldsReturn(self):
        samplePayload = TestCaseUtil.generateAttributesPayload()
        userAttributes = UserAttributes()
        userAttributes.updateAttribute('id', samplePayload['id'])
        userAttributes.updateAttribute('name', samplePayload['name'])
        userAttributes.updateAttribute('color', samplePayload['color'])
        userAttributes.updateAttribute('waa', samplePayload['extraAttributes']['waa'])

        self.assertEqual(userAttributes.toString(), TestCaseUtil.loadAsStr(samplePayload))

if __name__ == '__main__':
    unittest.main()