import src.main.Models.User as User
from dash import Dash, html
import dash_cytoscape as cyto

class UserNetwork:
    def createSource(self, user):
        if user.parent != None:
            sourceString = {'data': {'source': user.parent.id, 'target': user.id}, 'classes': user.parent.color}
            return sourceString
    def createNode(self, user):
        nodeString = {'data': {'id': user.id, 'label': user.name}, 'classes': user.color}
        return nodeString
    
    def generateElements(self, user):
        elementsArray = []
        if len(user.children) == 0:
            sourceString = self.createSource(user)
            nodeString = self.createNode(user)
            if(sourceString != None):
                elementsArray.append(sourceString)
            elementsArray.append(nodeString)
            return elementsArray
        else:
            child = user.children.pop() # Decrement Children by 1.
            elementsArray += self.generateElements(child) # Recursive Call.
            elementsArray += self.generateElements(user) # Recurses itself to see if Node has more children.
            return elementsArray

    def generateGraph(self, user):
        app = Dash(__name__)
        app.layout = html.Div([
        html.P("User Network"),
        cyto.Cytoscape(id='cytoscape',
                   elements=self.generateElements(user),
        layout={'name': 'concentric', 'minNodeSpacing': 30, 'sweep': 5, 'equidistant': False, 'spacingFactor': 2},
        style={'width': '1920px', 'height': '1080px', 'curve-style': 'bezier'},
        stylesheet=[
            {
                'selector': '.red',
                'style': {
                    'background-color': 'red',
                    'line-color': 'red'
                }
            },
             {
                'selector': '.blue',
                'style': {
                    'background-color': 'blue',
                    'line-color': 'blue'
                }
            },
             {
                'selector': '.black',
                'style': {
                    'background-color': 'black',
                    'line-color': 'black'
                }
            },
             {
                'selector': '.yellow',
                'style': {
                    'background-color': 'yellow',
                    'line-color': 'yellow'
                }
            },
             {
                'selector': '.green',
                'style': {
                    'background-color': 'green',
                    'line-color': 'green'
                }
            }
        ]
        )
        ])
        app.run(debug=True)

    
