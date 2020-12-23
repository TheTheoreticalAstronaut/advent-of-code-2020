from Day1 import Day1
from Day2 import Day2
from Day3 import Day3
from Day4 import Day4
from time import time

if __name__ == '__main__':
    startTime = time()
    challenge = Day4()
    challenge.runPartTwo()
    endTime = time()
    print("Execution took {0}ms".format(1000*(endTime - startTime)))



