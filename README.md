This project is to create a graph that will allow me to visualize all the members of a server and their connections//people they've brought into the server.

## How to Run this Repository
Clone this repository to your local and run
> pip install -r requirements.txt

Once all the dependencies are downloaded, you should be able to run
> python3 scriptTester.py

Upon running, you'll be able to see the page generated on: http://127.0.0.1:8050/

Because this is using Dash, you're able to update the values & the page will update in real time.

TODO:
1. Create functionality to allow external sources to call methods & generate a graph.
2. Fix the graph to be more concentric.
     Requirements:
     a. Level 0: Is the center.
     b. Level 1: The Main Branches, where the rest of the children will sprout from.
         After Level 1, the branches should populate the quadrant or partition the level 1 parent is, should cause NO overlap.
3. Create functionality that would screenshot the graph & export it to an external source.
