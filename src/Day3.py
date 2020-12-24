from src.Challenge import Challenge


class Day3(Challenge):
    DATA_FILENAME = "resources/day3_input.dat"
    patternMatrix = []

    def runPartOne(self):
        self.__getPatternMatrix()
        treesHit = self.__getTreesHit(3,1)
        if self.verbose:
            print("Number of trees hit: {0}".format(treesHit))
        return treesHit

    def runPartTwo(self):
        self.__getPatternMatrix()
        treesHit = 1
        treesHit *= self.__getTreesHit(1, 1)
        treesHit *= self.__getTreesHit(3, 1)
        treesHit *= self.__getTreesHit(5, 1)
        treesHit *= self.__getTreesHit(7, 1)
        treesHit *= self.__getTreesHit(1, 2)
        if self.verbose:
            print("Product of hit trees: {0}".format(treesHit))
        return treesHit

    def __getPatternMatrix(self):
        self.patternMatrix = []
        with open(self.DATA_FILENAME, "r") as file:
            for line in file:
                self.patternMatrix.append([int(val) for val in line.rstrip().replace(".","0").replace("#","1")])
        return self.patternMatrix

    def __getTreesHit(self, horizontalIncrement, verticalIncrement):
        if (not self.patternMatrix) or (verticalIncrement < 1):
            return 0
        height = len(self.patternMatrix)
        width = len(self.patternMatrix[0])
        treesHit = 0
        for h in range(0, height, verticalIncrement):
            w = (horizontalIncrement * (h // verticalIncrement)) % width
            treesHit += self.patternMatrix[h][w]
        return treesHit
