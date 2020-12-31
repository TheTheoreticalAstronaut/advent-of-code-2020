from src.Challenge import Challenge


class Day6(Challenge):
    DATA_FILENAME = "resources/day6_input.dat"
    _allLettersSet = set("abcdefghijklmnopqrstuvwxyz")

    def runPartOne(self) -> int:
        with open(self.DATA_FILENAME, "r") as file:
            totalYesCount = 0
            groupString = ""
            for line in file:
                if not line.rstrip():
                    totalYesCount += len(set(groupString))
                    groupString = ""
                    continue
                groupString += line.rstrip()
            totalYesCount += len(set(groupString))
        if self.verbose:
            print("Total 'yes' count: {0}".format(totalYesCount))
        return totalYesCount

    def runPartTwo(self) -> int:
        with open(self.DATA_FILENAME, "r") as file:
            totalYesCount = 0
            groupEntries = []
            for line in file:
                if not line.rstrip():
                    totalYesCount += len(self._allLettersSet.intersection(*[set(entry) for entry in groupEntries]))
                    groupEntries = []
                    continue
                groupEntries.append(line.rstrip())
            totalYesCount += len(self._allLettersSet.intersection(*[set(entry) for entry in groupEntries]))
        if self.verbose:
            print("Total 'yes' count: {0}".format(totalYesCount))
        return totalYesCount
