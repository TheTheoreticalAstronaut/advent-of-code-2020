import unittest
from src.Day1 import Day1
from src.Day2 import Day2


class TestAdventOfCode2020(unittest.TestCase):
    DAY_1_PART_ONE_SOLUTION = 1014171
    DAY_1_PART_TWO_SOLUTION = 46584630
    DAY_2_PART_ONE_SOLUTION = 393
    DAY_2_PART_TWO_SOLUTION = 690

    def testDay1PartOne(self):
        challenge = Day1(2020)
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_1_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_1_PART_ONE_SOLUTION, challengeSolution))

    def testDay1PartTwo(self):
        challenge = Day1(2020)
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_1_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_1_PART_TWO_SOLUTION, challengeSolution))

    def testDay2PartOne(self):
        challenge = Day2()
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_2_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_2_PART_ONE_SOLUTION, challengeSolution))

    def testDay2PartTwo(self):
        challenge = Day2()
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_2_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_2_PART_TWO_SOLUTION, challengeSolution))


if __name__ == '__main__':
    unittest.main()
