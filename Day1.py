from FileUtils import readNumbersFromFile

class Day1():
    DATA_FILENAME = "day1_input.dat"
    targetSum = -1
    targetProduct = -1
    magicNumbers = []
    found = False

    def __init__(self, targetSum):
        self.targetSum = targetSum

    def runPartOne(self):
        data = readNumbersFromFile(self.DATA_FILENAME)
        if not data:
            return

        data.sort()
        remainingSecondValues = data
        for firstVal in data:
            targetValue = self.targetSum - firstVal
            remainingSecondValues = [val for val in remainingSecondValues[1:] if val <= targetValue]
            if targetValue in remainingSecondValues:
                self.found = True
                self.targetProduct = firstVal*targetValue
                self.magicNumbers.extend([firstVal, targetValue])
                break

        self.__printResult()

    def runPartTwo(self):
        data = readNumbersFromFile(self.DATA_FILENAME)
        if not data:
            return

        data.sort()
        remainingSecondValues = data
        for firstVal in data:
            thresholdValue = self.targetSum - firstVal
            remainingSecondValues = [val for val in remainingSecondValues if val <= thresholdValue and val != firstVal]
            if not remainingSecondValues:
                break

            remainingThirdValues = set([val for val in remainingSecondValues[1:] if val <= (thresholdValue - remainingSecondValues[0])])
            for secondVal in remainingSecondValues:
                targetValue = self.targetSum - firstVal - secondVal
                if targetValue in remainingThirdValues:
                    self.found = True
                    self.targetProduct = firstVal*secondVal*targetValue
                    self.magicNumbers.extend([firstVal, secondVal, targetValue])
                if self.found:
                    break
            if self.found:
                break

        self.__printResult()

    def __printResult(self):
        if self.found:
            print("The magic numbers are {0}".format(self.magicNumbers))
            print("Their product is {0}".format(self.targetProduct))
        else:
            print("Result not found")


