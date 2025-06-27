import uuid


class User:
    def __init__(self, name, id=(str(uuid.uuid4())+'_user')):
        self.parent = None
        self.id = id
        self.name = name
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)
        child.setParent(self)
    def removeChild(self, child):
        self.children.remove(child)
    def clearChildren(self):
        self.children.clear()
    def setParent(self, parent):
        self.parent = parent
      
    def createSource(self):
        if self.parent != None:
            sourceString = {'data': {'source': self.parent.id, 'target': self.id}}
            return sourceString
    def createNode(self):
        nodeString = {'data': {'id': self.id, 'label': self.name}}
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