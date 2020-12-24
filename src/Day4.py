from src.Challenge import Challenge
from dataclasses import dataclass
import re


class Day4(Challenge):
    DATA_FILENAME = "resources/day4_input.dat"
    passportDataRegex = "(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):([#0-9a-zA-Z]*)"

    def runPartOne(self) -> int:
        return self.__run("isPassportValidPartOne")

    def runPartTwo(self) -> int:
        return self.__run("isPassportValidPartTwo")

    def __run(self, validityProperty):
        compiledPassportDataRegex = re.compile(self.passportDataRegex)
        validPassports = 0
        passportData = PassportData()
        with open(self.DATA_FILENAME, "r") as file:
            for line in file:
                if not line.rstrip():
                    validPassports += getattr(passportData, validityProperty)
                    passportData.clear()
                for (attr, value) in re.findall(compiledPassportDataRegex, line):
                    setattr(passportData, attr, value)
        if self.verbose:
            print("Number of valid passports: {0}".format(validPassports))
        return validPassports


@dataclass
class PassportData:
    byr: str = ""
    iyr: str = ""
    eyr: str = ""
    hgt: str = ""
    hcl: str = ""
    ecl: str = ""
    pid: str = ""
    cid: str = ""
    __acceptableEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    __byrLowerLimit = 1920
    __byrUpperLimit = 2002
    __iyrLowerLimit = 2010
    __iyrUpperLimit = 2020
    __eyrLowerLimit = 2020
    __eyrUpperLimit = 2030
    __hgtCmLowerLimt = 150
    __hgtCmUpperLimit = 193
    __hgtInLowerLimt = 59
    __hgtInUpperLimit = 76

    @property
    def isPassportValidPartOne(self) -> bool:
        return all([(getattr(self, data, "") != "") for data in dir(self) if data != "cid"])

    @property
    def isPassportValidPartTwo(self) -> bool:
        if not all([(getattr(self, data, "") != "") for data in dir(self) if data != "cid"]):
            return False

        if not self.__checkIfNumWithinLimits(self.byr, self.__byrLowerLimit, self.__byrUpperLimit):
            return False

        if not self.__checkIfNumWithinLimits(self.iyr, self.__iyrLowerLimit, self.__iyrUpperLimit):
            return False

        if not self.__checkIfNumWithinLimits(self.eyr, self.__eyrLowerLimit, self.__eyrUpperLimit):
            return False

        if not self.__checkHeight():
            return False

        if not self.__checkHairColor():
            return False

        if self.ecl not in self.__acceptableEcl:
            return False

        if not self.__checkPassportId():
            return False

        return True

    def clear(self):
        for var in dir(self):
            setattr(self, var, "")

    def print(self):
        for var in dir(self):
            print("{0}: {1}".format(var, getattr(self, var)))

    def __checkIfNumWithinLimits(self, numStr, lowerLim, upperLim) -> bool:
        try:
            numInt = int(numStr)
            if not lowerLim <= numInt <= upperLim:
                return False
        except ValueError:
            return False
        return True

    def __checkHeight(self) -> bool:
        match = re.search("([0-9]+)(in|cm)", self.hgt)
        if match:
            if match.group(2) == "cm" and not self.__checkIfNumWithinLimits(match.group(1), self.__hgtCmLowerLimt, self.__hgtCmUpperLimit):
                return False
            elif match.group(2) == "in" and not self.__checkIfNumWithinLimits(match.group(1), self.__hgtInLowerLimt, self.__hgtInUpperLimit):
                return False
        else:
            return False
        return True

    def __checkHairColor(self) -> bool:
        match = re.search("#([0-9a-f]+)", self.hcl)
        if not match or len(match.group(1)) != 6:
            return False
        return True

    def __checkPassportId(self) -> bool:
        try:
            int(self.pid)
            if len(self.pid) != 9:
                return False
        except ValueError:
            return False
        return True

    def __dir__(self):
        return ["byr", "iyr", "eyr", "hgt",
                "hcl", "ecl", "pid", "cid"]


