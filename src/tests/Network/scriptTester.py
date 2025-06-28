from src.main.Network.UserNetwork import UserNetwork
from src.main.Models.User import User
import random

def main():

    parentUser = User('Big Yikes')
    ethanUser = User('Ethan', None, 'red')
    tylerUser = User('Tyler', None, 'blue')
    kevinUser = User('Kevin', None, 'yellow')
    marcoUser = User('Marco', None, 'green')
    generateRandomUser(ethanUser, tylerUser, kevinUser, marcoUser)
    parentUser.addChild(ethanUser)
    parentUser.addChild(tylerUser)
    parentUser.addChild(marcoUser)
    parentUser.addChild(kevinUser)
    ethanUser.addChild(User('aaaa'))
    ethanUser.setParent(kevinUser)
    sampleNetwork = UserNetwork(parentUser)
    sampleNetwork.generateGraph()

def generateRandomUser(user1, user2, user3, user4):
    for i in range(10):
        x = random.randint(1,4)
        if x == 1:
            tempUser = User('aaaaa')
            user1.addChild(tempUser)
            tempUser.addChild(User())
        elif x == 2:
            user2.addChild(User())
        elif x == 3:
            user3.addChild(User())
        else:
            user4.addChild(User())



if __name__ == '__main__':
    main()
