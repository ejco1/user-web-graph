from src.main.Models.UserAttributes import UserAttributes
import json

class User:
    def __init__(self, id=None, name=None, color=None):
        self.parent = None
        self.children = []
        self.fields = self.__createInitialFields(id, name, color)

    def __createInitialFields(self, id, name, color):
        initialAttributes = UserAttributes()
        if id is not None:
            initialAttributes.updateAttribute('id', id)
        if name is not None:
            initialAttributes.updateAttribute('name', name)
        if color is not None:
            initialAttributes.updateAttribute('color', color)
        return initialAttributes

    def addChild(self, child):
        child.setParent(self)
        child.traverseAndUpdateTree('color', self.getField('color'))
        self.children.append(child)
    def removeChild(self, child):
        self.children.remove(child)
    def clearChildren(self):
        self.children.clear()
    def getChild(self, childId=None):
        if len(self.children) == 0:
            return None
        elif childId is None:
            return self.children[0]
        else:
            for child in self.children:
                if childId == child.getField('id'):
                    return child
            return None
    def getAllChildren(self, justIDs=False):
        listOfChildren = []
        if len(self.children) == 0:
            return None
        else:
            if justIDs == True:
                for child in self.children:
                    listOfChildren.append(child.getField('id'))
            else:
                return self.children

    def setParent(self, parent):
        self.parent = parent
        self.traverseAndUpdateTree('color', parent.getField('color'))
    def getParent(self, justID=False):
        if justID is True and self.parent is not None:
            return self.parent.getField('id')
        else:
            return self.parent
    def getField(self, key):
        return self.fields.getAttribute(key)
    def getAllFields(self):
        return self.fields.toString()
    def updateField(self, key, value):
        self.fields.updateAttribute(key, value)
    def traverseAndUpdateTree(self, keyToUpdate=None, valueToUpdate=None):
        listOfUsers = []
        if len(self.children) == 0:
            if keyToUpdate is not None:
                self.updateField(keyToUpdate, valueToUpdate)
            listOfUsers.append(self)
        else:
            for child in self.children:
                child.traverseTree(keyToUpdate, valueToUpdate)
        return listOfUsers
    def toString(self):
        userString = '{}'
        justIDs = True
        data = json.loads(userString)
        data['User'] = json.loads(self.getAllFields())
        data['ParentID'] = self.getParent(justIDs)
        data['Children'] = self.getAllChildren(justIDs)
        return userString
