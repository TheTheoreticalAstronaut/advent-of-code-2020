from src.Challenge import Challenge
import re


class Day2(Challenge):
    DATA_FILENAME = "resources/day2_input.dat"
    inputPattern = "([0-9]+)-([0-9]+)\s+([a-zA-Z]):\s+([a-zA-Z]*)"

    def __init__(self):
        self.compiledRegex = re.compile(self.inputPattern)

    def runPartOne(self):
        validPasswords = 0
        with open(self.DATA_FILENAME,"r") as file:
            for (firstIndexStr, secondIndexStr, char, password) in self.compiledRegex.findall(file.read()):
                minCharInstances = int(firstIndexStr)
                maxCharInstances = int(secondIndexStr)
                validPasswords += bool(minCharInstances <= password.count(char) <= maxCharInstances)
        self.__printResult(validPasswords)
        return validPasswords

    def runPartTwo(self):
        validPasswords = 0
        with open(self.DATA_FILENAME,"r") as file:
            for (firstIndexStr, secondIndexStr, char, password) in self.compiledRegex.findall(file.read()):
                firstIndex = int(firstIndexStr) - 1
                secondIndex = int(secondIndexStr) - 1
                if len(password) > secondIndex:
                    validPasswords += (bool(password[firstIndex] == char) != bool(password[secondIndex] == char))
        self.__printResult(validPasswords)
        return validPasswords

    def __printResult(self, validPasswords):
        if not self.verbose:
            return
        print("Number of valid passwords: {0}".format(validPasswords))
