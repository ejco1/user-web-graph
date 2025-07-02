This project is to create a graph that will allow me to visualize all the members of a server and their connections//people they've brought into the server.

## How to Run this Repository
Clone this repository to your local and run
> pip install -r requirements.txt

To run the test cases on the back-end logic:
> python -m unittest discover 

If you add more test cases, make sure to also add a file called "__init__.py" to the new module/directory(if you created one)
No, I don't understand how it works, but it does for some reason.

TODO:
1. Create functionality to allow external sources to call methods & generate a graph.
2. Fix the graph to be more concentric.
     Requirements:
     a. Level 0: Is the center.
     b. Level 1: The Main Branches, where the rest of the children will sprout from.
         After Level 1, the branches should populate the quadrant or partition the level 1 parent is, should cause NO overlap.
    c. IDEA- Divide the nodes using Levels, and for each Node, their children will surround them. 
3. Create functionality that would screenshot the graph & export it to an external source.
4. Test Cases.
