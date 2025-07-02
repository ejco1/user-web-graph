from dash import Dash, html
from src.main.Models.User import User
import dash_cytoscape as cyto
import json

class UserNetwork:
### Format: {'data': {'source': user.parent.id, 'target': user.id}}
    def createSource(userString):
        userJSON = json.loads(userString)
        dataObj = json.loads('{}') 
        sourceJSON = json.loads('{}')
        userDataJSON = userJSON['User']
        dataObj['source'] = userJSON['ParentID']
        dataObj['target'] = userDataJSON['id']
        sourceJSON['data'] = dataObj
        sourceString = json.dumps(sourceJSON)
        if userJSON['ParentID'] is not None:
            return sourceString
### Format: {'data': {'id': user.id, 'label': user.name}}             
    def createNode(userString):
        userJSON = json.loads(userString)
        emptyString = '{}'
        dataObj = json.loads(emptyString) 
        nodeJSON = json.loads(emptyString)
        userDataJSON = json.loads(emptyString)
        userDataJSON = userJSON['User']
        dataObj['id'] = userDataJSON['id']
        dataObj['label'] = userDataJSON['name']
        nodeJSON['data'] = dataObj
        nodeString = json.dumps(nodeJSON)
        return nodeString
    def generateElements(self, userArray):
        elementsArray = []
        for user in userArray:
            sourceString = self.createSource(user)
            nodeString = self.createNode(user)
            if(sourceString is not None):
                elementsArray.append(sourceString)
            elementsArray.append(nodeString)
        return elementsArray

    def generateGraph(self, userArray):
        app = Dash(__name__)
        app.layout = html.Div([
        html.P("User Network"),
        cyto.Cytoscape(id='cytoscape',
                   elements=self.generateElements(userArray),
        layout={'name': 'concentric', 'minNodeSpacing': 30, 'sweep': 5, 'equidistant': False, 'spacingFactor': 2},
        style={'width': '1920px', 'height': '1080px', 'curve-style': 'bezier'},
        stylesheet=[]
        )
        ])
        app.run(debug=True)

    
