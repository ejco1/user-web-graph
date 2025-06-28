import uuid
import UserAttributes

class User:
    def __init__(self, id=None, name=None, color=None):
        self.parent = None
        self.children = []
        self.attributes = UserAttributes()
        self.attributes.updateAttributes(id, name, color)

    def addChild(self, child):
        child.setParent(self)
        child.color = updateColor(child, self.color)
        self.children.append(child)
    def removeChild(self, child):
        self.children.remove(child)
    def clearChildren(self):
        self.children.clear()
    def setParent(self, parent):
        self.parent = parent
        self.color = updateColor(self, parent.color)
    def getParent(self):
        return self.parent
    def getId(self):
        return self.id
    def setId(self, newId):
        self.id = newId
    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
    def setColor(self, color):
        if len(self.children) == 0:
            self.color = color
        else:
            for child in self.children:
                child.setColor(color)