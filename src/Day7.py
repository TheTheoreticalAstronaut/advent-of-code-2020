from src.Challenge import Challenge
import re


class Day7(Challenge):
    DATA_FILENAME = "resources/day7_input.dat"

    def __init__(self):
        self._entrySeparator = " bags contain "
        self._bagContentsRegex = "([0-9])\s([a-zA-Z\s]+)\sbags?"
        self._compiledBagContentsRegex = re.compile(self._bagContentsRegex)
        self._network = self._constructNodeNetwork()

    def runPartOne(self) -> int:
        numBagsContainingShinyGold = len(self._traceNodeBackwards(["shiny gold"], set())) - 1
        if self.verbose:
            print("Number of bags containing a 'shiny gold' bag: {0}".format(numBagsContainingShinyGold))
        return numBagsContainingShinyGold

    def runPartTwo(self) -> int:
        numBagsInsideShinyGold = self._traceNodeForwardsWithCount({"shiny gold": 1}, 0) - 1
        if self.verbose:
            print("Number of bags inside a 'shiny gold' bag: {0}".format(numBagsInsideShinyGold))
        return numBagsInsideShinyGold

    def _constructNodeNetwork(self):
        nodes = dict()
        with open(self.DATA_FILENAME) as file:
            for line in file:
                name, contains = line.rstrip().split(self._entrySeparator, 1)
                newNode = Node(name)
                for match in re.findall(self._bagContentsRegex, line):
                    newNode.addToOut(match[1], match[0])
                nodes[name] = newNode
        for node in nodes.values():
            for outNode, count in node.getOutEntries().items():
                nodes[outNode].addToIn(node.getName(), count)
        return nodes

    def _traceNodeBackwards(self, nodesToCheck, nodesChecked):
        if not nodesToCheck:
            return nodesChecked
        currentNode = nodesToCheck.pop(0)
        nodesChecked.add(currentNode)
        nodesToCheck.extend([node for node in self._network[currentNode].getInEntries().keys() if node not in nodesChecked])
        return self._traceNodeBackwards(nodesToCheck, nodesChecked)

    def _traceNodeForwardsWithCount(self, nodesToCheck, count):
        newNodesToCheck = {}
        for nodeToCheck, nodeMultiplier in nodesToCheck.items():
            nodeMultiplierInt = int(nodeMultiplier)
            count += nodeMultiplierInt
            for newNode, newNodeMultiplier in self._network[nodeToCheck].getOutEntries().items():
                if newNode in newNodesToCheck:
                    newNodesToCheck[newNode] += nodeMultiplierInt*int(newNodeMultiplier)
                else:
                    newNodesToCheck[newNode] = nodeMultiplierInt*int(newNodeMultiplier)
        if not newNodesToCheck:
            return count
        return self._traceNodeForwardsWithCount(newNodesToCheck, count)


class Node:
    def __init__(self, name: str):
        self._out = dict()
        self._in = dict()
        self._name = name

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._name == other._name

    def __hash__(self):
        return hash(self._name)

    def getName(self):
        return self._name

    def addToOut(self, name: str, quantity: int) -> None:
        self._out[name] = quantity

    def addToIn(self, name: str, quantity: int) -> None:
        self._in[name] = quantity

    def getOutEntries(self):
        return self._out

    def getInEntries(self):
        return self._in
