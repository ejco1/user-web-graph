import User
from dash import Dash, html
import dash_cytoscape as cyto

class UserNetwork:
    def __init__(self, title):
        self.parentUser = title
    
    def generateGraph(self):
        app = Dash(__name__)
        app.layout = html.Div([
        html.P("User Network"),
        cyto.Cytoscape(id='cytoscape',
                   elements=self.parentUser.drawConnection(),
        layout={'name': 'concentric', 'minNodeSpacing': 30, 'sweep': 5, 'equidistant': True, 'spacingFactor': 2},
        style={'width': '1920px', 'height': '1080px', 'curve-style': 'bezier'}
        )
        ])
        app.run(debug=True)

    
