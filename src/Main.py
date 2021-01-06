from Day1 import Day1
from Day2 import Day2
from Day3 import Day3
from Day4 import Day4
from Day5 import Day5
from Day6 import Day6
from Day7 import Day7
from Day8 import Day8
from Day9 import Day9
from time import time

if __name__ == '__main__':
    startTime = time()
    challenge = Day9()
    challenge.runPartTwo()
    endTime = time()
    print("Execution took {0}ms".format(1000*(endTime - startTime)))



