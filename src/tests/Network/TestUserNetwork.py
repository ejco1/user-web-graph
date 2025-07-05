import unittest
from src.tests.util.TestCaseUtil import TestCaseUtil
from src.main.Network.UserNetwork import UserNetwork

class TestUserNetwork(unittest.TestCase):
## No matter what changes we make to creating elements,
## Users must map all of their attributes to the data object.
    def test_UserMapsMandatoryDetailsToNodesAndSources(self):
        parentUser = TestCaseUtil.createSampleTree("abc123", "blue", 2)
        sampleNetwork = UserNetwork()
        childUser = parentUser.getChild()
        nodeDataObjects = sampleNetwork.createNode(childUser.toString())
        sourceDataObject = sampleNetwork.createSource(childUser.toString())

        nodeData = nodeDataObjects['data']
        sourceData = sourceDataObject['data']

        self.assertEqual(nodeData['id'], childUser.getField('id'))
        self.assertEqual(nodeData['label'], childUser.getField('name'))

        self.assertEqual(sourceData['source'], childUser.getParent(True))
        self.assertEqual(sourceData['target'], childUser.getField('id'))


    