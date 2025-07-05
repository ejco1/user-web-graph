from src.main.Network.UserNetwork import UserNetwork
from src.tests.util.TestCaseUtil import TestCaseUtil

##Try it yourself! -- run "python3 -m src.tests.Network.sampleVisualizer"
##
def main():
    sampleParent = TestCaseUtil.createSampleTree('abc123', 'blue', 12)
#    sampleParent.getChild().updateField('color', 'green')
#    sampleParent.getChild().addChild(TestCaseUtil.createSampleTree('NEW_ADDITION', None, 6))
    sampleArray = sampleParent.traverseAndUpdateTree()
    jsonToSend = []
    for sample in sampleArray:
        jsonToSend.append(sample.toString())
    userNetwork = UserNetwork()
    userNetwork.generateGraph(jsonToSend)

if __name__ == '__main__':
    main()
