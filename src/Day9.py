from src.Challenge import Challenge
import bisect


class Day9(Challenge):
    DATA_FILENAME = "resources/day9_input.dat"

    def __init__(self):
        self._readInput()
        self._preambleSize = 25

    def runPartOne(self) -> int:
        sortedPreambleEntries = sorted(self._input[:self._preambleSize])
        currentLine = self._preambleSize
        while currentLine < len(self._input):
            if not self._preambleDoubleSumCheck(sortedPreambleEntries, self._input[currentLine]):
                if self.verbose:
                    print("First value failing the sum rule: {0}".format(self._input[currentLine]))
                return self._input[currentLine]
            sortedPreambleEntries.remove(self._input[currentLine - self._preambleSize])
            bisect.insort_left(sortedPreambleEntries, self._input[currentLine])
            currentLine += 1
        return -1

    def runPartTwo(self) -> int:
        firstLineFailingSumRule = 502  # From part one
        valueFailingSumRule = self._input[firstLineFailingSumRule]
        currentSum = self._input[firstLineFailingSumRule-1]
        currentSequence = [self._input[firstLineFailingSumRule-1]]
        for lastTerm in self._input[firstLineFailingSumRule-2::-1]:
            currentSequence.append(lastTerm)
            currentSum += lastTerm
            if currentSum > valueFailingSumRule:
                currentSum -= currentSequence.pop(0)
            if currentSum == valueFailingSumRule and len(currentSequence) != 1:
                return self._foundSequence(currentSequence)

    def _foundSequence(self, sequence):
        sumMinMaxInSequence = max(sequence) + min(sequence)
        if self.verbose:
            print("The sum of the min and max values in the sequence is: {0}".format(sumMinMaxInSequence))
        return sumMinMaxInSequence

    def _readInput(self) -> None:
        with open(self.DATA_FILENAME, "r") as file:
            self._input = [int(line.rstrip()) for line in file]

    def _preambleDoubleSumCheck(self, sortedPreambleEntries, value: int) -> bool:
        insertPoint = bisect.bisect_left(sortedPreambleEntries, value)
        if insertPoint == 0:
            return False
        globalMinIdx = 0
        for maxIdx in range(insertPoint-1, 0, -1):
            for minIdx in range(globalMinIdx, maxIdx):
                preambleSum = sortedPreambleEntries[minIdx] + sortedPreambleEntries[maxIdx]
                if preambleSum == value:
                    return True
                elif preambleSum < value:
                    globalMinIdx = minIdx
                else:
                    break
        return False
