import json
from src.main.Models.User import User
import random

class TestCaseUtil:
    def generateAttributesPayloadString():
        payload = {
            "id" : "test123",
            "name": "Ethan",
            "color": "blue",
            "extraAttributes": {"waa": "wee"}
        }
        payloadString = json.dumps(payload)
        return payloadString
    def createSampleTree(treeId=None, treeColor=None, numberOfNodes=None):
        parentUser = TestCaseUtil.createSampleUser(treeId, None, treeColor)

        lastKnownUser = parentUser
        for childNumber in range(numberOfNodes):
            choice = random.randint(0, 1)
            if choice == 0:
                lastKnownUser = TestCaseUtil.createSampleUser(treeId, childNumber)
                parentUser.addChild(lastKnownUser)
            if choice == 1:
                tempUser = TestCaseUtil.createSampleUser(treeId, childNumber)
                lastKnownUser.addChild(tempUser)
                lastKnownUser = tempUser
        return parentUser

    def createSampleUser(id, number=None, color=None):
        value = number
        if value is None:
            value = "parent"
        return User("{t}_userId_{i}".format(t = id, i = value), "{t}_userName_{i}".format(t = id, i = value), color)


    def generateAttributesPayload():
        return json.loads(TestCaseUtil.generateAttributesPayloadString())
    def loadAsJSON(payloadString):
        return json.loads(payloadString)
    def loadAsStr(payload):
        return json.dumps(payload)