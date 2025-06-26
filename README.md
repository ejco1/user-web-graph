This project is to create a graph that will allow me to visualize all the members of a server and their connections//people they've brought into the server.

Objects in the project so far:

User {
    Parent: User
    Children: []User

    addChild(): void
    removeChild(): void
    clearChildren(): void
    setParent(): void
    createSource(): String
    createNode(): String
    drawConnection(): []String
}
### Unfamiliar with graph implementation right now. The Parent User should be the server name, just to serve as the center of the web.
UserNetwork {
    ParentUser: User
    generateGraph(): Runs Application
}