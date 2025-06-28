import unittest
from src.tests.util.TestCaseUtil import TestCaseUtil

class TestUser(unittest.TestCase):
## This tests that regardless of updates,
# The parent will see its child, and the child will see its parent.
# The child will also share the same color, unless specified otherwise(Which the child did not specify here)
    def test_SchemaValues(self):
        parentUser = TestCaseUtil.createSampleTree("abc123", "blue", 1)
        childUser = parentUser.getChild()

        self.assertEqual(parentUser.getField('color'), childUser.getField('color'))
        self.assertEqual(childUser.getParent(True), parentUser.getField('id'))
    def test_inJSONFormat(self):
        parentUser = TestCaseUtil.createSampleTree("abc123", "green", 3)
        parentString = parentUser.toString()
        try:
            TestCaseUtil.loadAsJSON(parentString)
            self.assertTrue(True)
        except TypeError as e:
            self.assertFalse(False, e)
