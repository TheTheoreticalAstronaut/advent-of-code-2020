from dataclasses import dataclass
import re


class Day4:
    DATA_FILENAME = "resources/day4_input.dat"
    passportDataRegex = "(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):([#0-9a-zA-Z]*)"

    def runPartOne(self):
        compiledPassportDataRegex = re.compile(self.passportDataRegex)
        validPassports = 0
        passportData = PassportData()
        with open(self.DATA_FILENAME, "r") as file:
            for line in file:
                if not line.rstrip():
                    validPassports += passportData.isPassportValidPartOne
                    passportData.clear()
                for (attr, value) in re.findall(compiledPassportDataRegex, line):
                    setattr(passportData, attr, value)
        print("Number of valid passports: {0}".format(validPassports))
        return validPassports

    def runPartTwo(self):
        compiledPassportDataRegex = re.compile(self.passportDataRegex)
        validPassports = 0
        passportData = PassportData()
        with open(self.DATA_FILENAME, "r") as file:
            for line in file:
                if not line.rstrip():
                    validPassports += passportData.isPassportValidPartTwo
                    passportData.clear()
                for (attr, value) in re.findall(compiledPassportDataRegex, line):
                    setattr(passportData, attr, value)
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

    @property
    def isPassportValidPartOne(self):
        return all([(getattr(self, data, "") != "") for data in dir(self) if data != "cid"])

    @property
    def isPassportValidPartTwo(self):
        if not all([(getattr(self, data, "") != "") for data in dir(self) if data != "cid"]):
            return False

        try:
            byrInt = int(self.byr)
            if (not 1920 <= byrInt <= 2002) or (len(self.byr) != 4):
                return False
        except ValueError:
            return False

        try:
            iyrInt = int(self.iyr)
            if (not 2010 <= iyrInt <= 2020) or (len(self.byr) != 4):
                return False
        except ValueError:
            return False

        try:
            eyrInt = int(self.eyr)
            if (not 2020 <= eyrInt <= 2030) or (len(self.byr) != 4):
                return False
        except ValueError:
            return False

        match = re.search("([0-9]+)(in|cm)", self.hgt)
        if match:
            hgtInt = int(match.group(1))
            if match.group(2) == "cm":
                if not 150 <= hgtInt <= 193:
                    return False
            elif match.group(2) == "in":
                if not 59 <= hgtInt <= 76:
                    return False
            else:
                return False
        else:
            return False

        match = re.search("#([0-9a-f]+)", self.hcl)
        if match:
            if len(match.group(1)) != 6:
                return False
        else:
            return False

        acceptableEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if self.ecl not in acceptableEcl:
            return False

        try:
            int(self.pid)
            if len(self.pid) != 9:
                return False
        except ValueError:
            return False

        return True

    def clear(self):
        for var in dir(self):
            setattr(self, var, "")

    def print(self):
        for var in dir(self):
            print("{0}: {1}".format(var, getattr(self, var)))

    def __dir__(self):
        return ["byr", "iyr", "eyr", "hgt",
                "hcl", "ecl", "pid", "cid"]


