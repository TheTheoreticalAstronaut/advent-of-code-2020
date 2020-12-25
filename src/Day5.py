from src.Challenge import Challenge


class Day5(Challenge):
    DATA_FILENAME = "resources/day5_input.dat"
    __rowsExponent = 7
    __columnsExponent = 3

    def __init__(self):
        self.__rows = 2**self.__rowsExponent
        self.__columns = 2**self.__columnsExponent
        self.__rowsList = range(self.__rows)
        self.__columnsList = range(self.__columns)

    def runPartOne(self) -> int:
        seatIds = self.__getSortedSeatIds()
        if self.verbose:
            print("Highest seat ID: {0}".format(seatIds[-1]))
        return seatIds[-1]

    def runPartTwo(self) -> int:
        seatIds = self.__getSortedSeatIds()
        missingSeat = next(iter(set(range(seatIds[0], seatIds[-1] + 1)) - set(seatIds)))
        if self.verbose:
            print("Missing seat ID: {0}".format(missingSeat))
        return missingSeat

    def __getSortedSeatIds(self):
        with open(self.DATA_FILENAME, "r") as file:
            seatIds = sorted(
                [self.__rowSearcher(line[:self.__rowsExponent], self.__rowsList)[0] * self.__columns +
                 self.__columnSearcher(line[self.__rowsExponent:(self.__rowsExponent+self.__columnsExponent)], self.__columnsList)[0]
                 for line in file])
        return seatIds

    def __rowSearcher(self, rowString : str, sortedRowList):
        return self.__binarySearcher(rowString, 'F', 'B', sortedRowList)

    def __columnSearcher(self, columnString : str, sortedColumnList):
        return self.__binarySearcher(columnString, 'L', 'R', sortedColumnList)

    def __binarySearcher(self, binaryString : str, lowerHalfChar, upperHalfChar, remainingList):
        if not binaryString:
            return remainingList
        elif binaryString[0] == lowerHalfChar:
            return self.__binarySearcher(binaryString[1:], lowerHalfChar, upperHalfChar, self.__sortedListSplitter(remainingList, True))
        elif binaryString[0] == upperHalfChar:
            return self.__binarySearcher(binaryString[1:], lowerHalfChar, upperHalfChar, self.__sortedListSplitter(remainingList, False))
        else:
            print("Unexpected binaryString character: {0}".format(binaryString[0]))

    def __sortedListSplitter(self, sortedList, lowerHalf : bool):
        splitIndex = len(sortedList)//2 + len(sortedList)%2 if lowerHalf else len(sortedList)//2
        return (sortedList[:splitIndex] if lowerHalf else sortedList[splitIndex:])
