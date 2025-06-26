from UserNetwork import UserNetwork
from User import User

def main():
    parentUser = User('Big Yikes')
    ethanUser = User('Ethan')
    parentUser.addChild(ethanUser)
    parentUser.addChild(User('Tyler'))
    parentUser.addChild(User('Marco'))
    parentUser.addChild(User('Kevin'))
    sampleNetwork = UserNetwork(parentUser)
    sampleNetwork.generateGraph()

if __name__ == '__main__':
    main()
