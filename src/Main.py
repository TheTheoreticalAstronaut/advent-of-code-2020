from Day1 import Day1
from Day2 import Day2
from time import time

if __name__ == '__main__':
    startTime = time()
    challenge = Day1(2020)
    challenge.runPartTwo()
    endTime = time()
    print("Execution took {0}s".format(1000*(endTime - startTime)))



