from src.Challenge import Challenge


class Day8(Challenge):
    DATA_FILENAME = "resources/day8_input.dat"

    def __init__(self):
        self._readCode()

    def runPartOne(self) -> int:
        self._runCode()
        if self.verbose:
            print("Accumulator value: {0}".format(self._accumulator))
        return self._accumulator

    def runPartTwo(self) -> int:
        self._runCode()
        visitedJmpLines = [line for line in self._visitedLines if self._code[line][0] == "jmp"]
        visitedNopLines = [line for line in self._visitedLines if self._code[line][0] == "nop"]
        for line in visitedJmpLines:
            self._code[line] = ("nop", self._code[line][1])
            self._runCode()
            if self._currentLine == len(self._code):
                print("Accumulator value: {0}".format(self._accumulator))
                return self._accumulator
            self._code[line] = ("jmp", self._code[line][1])
        for line in visitedNopLines:
            self._code[line] = ("jmp", self._code[line][1])
            self._runCode()
            if self._currentLine == len(self._code):
                print("Accumulator value: {0}".format(self._accumulator))
                return self._accumulator
            self._code[line] = ("nop", self._code[line][1])

    def _readCode(self) -> None:
        self._code = []
        with open(self.DATA_FILENAME, "r") as file:
            for line in file:
                action, arg = line.rstrip().split(" ", 1)
                self._code.append((action, int(arg)))

    def _runCode(self) -> None:
        self._resetVars()
        while True:
            if (self._currentLine in self._visitedLines) or (self._currentLine >= len(self._code)):
                break
            self._visitedLines.add(self._currentLine)
            action, arg = self._code[self._currentLine]
            self._runInstruction(action, arg)

    def _runInstruction(self, action: str, arg: int) -> None:
        if action == "nop":
            self._currentLine += 1
        elif action == "acc":
            self._accumulator += arg
            self._currentLine += 1
        elif action == "jmp":
            self._currentLine += arg

    def _resetVars(self) -> None:
        self._currentLine = 0
        self._accumulator = 0
        self._visitedLines = set()
