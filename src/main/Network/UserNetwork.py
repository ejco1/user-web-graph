from dash import Dash, html
import dash_cytoscape as cyto
import json

### This is a sample class used to see how one can transform the data to match
### necessary values for whichever library you use to visualize a tree.
class UserNetwork:
### Format: {'data': {'source': user.parent.id, 'target': user.id}}
    def createSource(self, userString):
        userJSON = json.loads(userString)
        dataObj = json.loads('{}') 
        sourceJSON = json.loads('{}')
        userDataJSON = userJSON['User']
        dataObj['source'] = userJSON['ParentID']
        dataObj['target'] = userDataJSON['id']
        dataObj['color'] = userDataJSON['color']
        sourceJSON['data'] = dataObj
        if userJSON['ParentID'] is not None:
            return sourceJSON
### Format: {'data': {'id': user.id, 'label': user.name}}             
    def createNode(self, userString):
        userJSON = json.loads(userString)
        emptyString = '{}'
        dataObj = json.loads(emptyString) 
        nodeJSON = json.loads(emptyString)
        userDataJSON = json.loads(emptyString)
        userDataJSON = userJSON['User']
        dataObj['id'] = userDataJSON['id']
        dataObj['label'] = userDataJSON['name']
        dataObj['color'] = userDataJSON['color']
        nodeJSON['data'] = dataObj
        return nodeJSON
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
        stylesheet=[
                {
                'selector': 'node',
                    'style': {
                        'content': 'data(label)',
                        'background-color': 'data(color)'
                    }
                },
                {
                'selector': 'edge',
                    'style': {
                        'line-color': 'data(color)'
                    }
                }
        ]
        )
        ])
        app.run(debug=True)

    
