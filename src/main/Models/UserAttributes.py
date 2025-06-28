import uuid
import json

class UserAttributes:
    def __init__(self):
        self.color = ''
        self.id = str(uuid.uuid4())+'_id'
        self.name = str(uuid.uuid4())+'_name'
        self.extraAttributes = '{}'
    def getAttribute(self, key):
        if key == 'id':
            return self.id
        elif key == 'name':
            return self.name
        elif key == 'color':
            return str(self.color)
        else:
            return self.extraAttributes
    def __addExtraAttribute(self, key, value):
        data = json.loads(self.extraAttributes)
        data[key] = value
        self.extraAttributes = json.dumps(data)
    def updateAttribute(self, key=None, value=None):
        if key == 'id':
            self.id = value
        elif key == 'name':
            self.name = value
        elif key == 'color':
            self.color = value
        elif key is not None:
            self.__addExtraAttribute(key, value)
    def printAttributes(self):
        attributes = '{}'
        data = json.loads(attributes)
        data['id'] = self.getAttribute('id')
        data['name'] = self.getAttribute('name')
        data['color'] = self.getAttribute('color')
        extra = json.loads(self.getAttribute('doesnt matter'))
        data['extraAttributes'] = extra
        
        attributesString = json.dumps(data)
        return attributesString