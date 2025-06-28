import UserAttributes

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
    def setParent(self, parent):
        self.parent = parent
        self.traverseAndUpdateTree('color', parent.getField('color'))
    def getParent(self):
        return self.parent
    def getField(self, key):
        return self.fields.getAttribute(key)
    def updateField(self, key, value):
        self.attributes.updateAttribute(key, value)
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
        userString = "'User': {allFields}".format(allFields = self.fields)
        return userString
