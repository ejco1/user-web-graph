import uuid

def updateColor(user, color):
    retColor = ''
    if color is None:
        retColor = 'black'
    elif user.parent is not None and user.parent.color == 'black':
        retColor = user.color
    elif color != 'black':
        retColor = color
    else:
        retColor = user.parent.color
    return retColor


class User:
    def __init__(self, name=None, id=None, color=None):
        self.parent = None
        self.id = id if id is not None else str(uuid.uuid4()) +'_id'
        self.name = name if name is not None else str(uuid.uuid4()) + '_name'
        self.children = []
        self.color = updateColor(self, color)

    
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
        self.color = color
      
    def createSource(self):
        if self.parent != None:
            sourceString = {'data': {'source': self.parent.id, 'target': self.id}, 'classes': self.parent.color}
            return sourceString
    def createNode(self):
        nodeString = {'data': {'id': self.id, 'label': self.name}, 'classes': self.color}
        return nodeString
# This is a recursive method to draw lines from child to parent.  
    def drawConnection(self):
        elementsArray = []
        if len(self.children) == 0:
            sourceString = self.createSource()
            nodeString = self.createNode()
            if(sourceString != None):
                elementsArray.append(sourceString)
            elementsArray.append(nodeString)
            return elementsArray
        else:
            child = self.children.pop() # Decrement Children by 1.
            elementsArray += child.drawConnection() # Recursive Call.
            elementsArray += self.drawConnection() # Recurses itself to see if Node has more children.
            return elementsArray