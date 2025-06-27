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

    
