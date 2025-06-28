import json

class TestCaseUtil:
    def generateAttributesPayload():
        payload = {
            "id" : "test123",
            "name": "Ethan",
            "color": "blue",
            "extraAttributes": {"waa": "wee"}
        }
        payloadString = json.dumps(payload)
        return payloadString