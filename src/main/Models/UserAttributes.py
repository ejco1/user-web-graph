import uuid

class UserAttributes:
    def __init__(self):
        self.color = None
        self.id = str(uuid.uuid4())+'_id'
        self.name = str(uuid.uuid4())+'_name'
    def getColor(self):
        return self.color
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def updateAttributes(self, id=None, name=None, color=None):
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if color is not None:
            self.color = color
    