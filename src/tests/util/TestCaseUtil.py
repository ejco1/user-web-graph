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
    def createSampleTree(treeId, treeColor, numberOfNodes):
        parentId = "{t}_userId".format(t = treeId)
        parentName = "{t}_userName".format(t = treeId)
        parentUser = User(parentId, parentName, treeColor)

        lastKnownUser = parentUser
        for childNumber in range(numberOfNodes):
            choice = random.randint(0, 3)
            if choice == 0:
                lastKnownUser = User("{t}_userId_child{i}".format(t = treeId, i = childNumber))
                parentUser.addChild(lastKnownUser)
            if choice == 1:
                lastKnownUser.addChild()



    def generateAttributesPayload():
        return json.loads(TestCaseUtil.generateAttributesPayloadString())
    def loadAsJSON(payloadString):
        return json.loads(payloadString)
    def loadAsStr(payload):
        return json.dumps(payload)