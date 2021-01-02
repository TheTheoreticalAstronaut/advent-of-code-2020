import unittest
from src.Day1 import Day1
from src.Day2 import Day2
from src.Day3 import Day3
from src.Day4 import Day4
from src.Day5 import Day5
from src.Day6 import Day6
from src.Day7 import Day7


class TestAdventOfCode2020(unittest.TestCase):
    DAY_1_PART_ONE_SOLUTION = 1014171
    DAY_1_PART_TWO_SOLUTION = 46584630
    DAY_2_PART_ONE_SOLUTION = 393
    DAY_2_PART_TWO_SOLUTION = 690
    DAY_3_PART_ONE_SOLUTION = 247
    DAY_3_PART_TWO_SOLUTION = 2983070376
    DAY_4_PART_ONE_SOLUTION = 237
    DAY_4_PART_TWO_SOLUTION = 172
    DAY_5_PART_ONE_SOLUTION = 888
    DAY_5_PART_TWO_SOLUTION = 522
    DAY_6_PART_ONE_SOLUTION = 6549
    DAY_6_PART_TWO_SOLUTION = 3466
    DAY_7_PART_ONE_SOLUTION = 139
    DAY_7_PART_TWO_SOLUTION = 58175
    verbose = False

    def testDay1PartOne(self):
        challenge = Day1(2020)
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_1_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_1_PART_ONE_SOLUTION, challengeSolution))

    def testDay1PartTwo(self):
        challenge = Day1(2020)
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_1_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_1_PART_TWO_SOLUTION, challengeSolution))

    def testDay2PartOne(self):
        challenge = Day2()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_2_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_2_PART_ONE_SOLUTION, challengeSolution))

    def testDay2PartTwo(self):
        challenge = Day2()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_2_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_2_PART_TWO_SOLUTION, challengeSolution))

    def testDay3PartOne(self):
        challenge = Day3()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_3_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_3_PART_ONE_SOLUTION, challengeSolution))

    def testDay3PartTwo(self):
        challenge = Day3()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_3_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_3_PART_TWO_SOLUTION, challengeSolution))

    def testDay4PartOne(self):
        challenge = Day4()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_4_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_4_PART_ONE_SOLUTION, challengeSolution))

    def testDay4PartTwo(self):
        challenge = Day4()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_4_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_4_PART_TWO_SOLUTION, challengeSolution))

    def testDay5PartOne(self):
        challenge = Day5()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_5_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_5_PART_ONE_SOLUTION, challengeSolution))

    def testDay5PartTwo(self):
        challenge = Day5()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_5_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_5_PART_TWO_SOLUTION, challengeSolution))

    def testDay6PartOne(self):
        challenge = Day6()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_6_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_6_PART_ONE_SOLUTION, challengeSolution))

    def testDay6PartTwo(self):
        challenge = Day6()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_6_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_6_PART_TWO_SOLUTION, challengeSolution))

    def testDay7PartOne(self):
        challenge = Day7()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartOne()
        self.assertEqual(challengeSolution, self.DAY_7_PART_ONE_SOLUTION, "Expected {0}, got {1}".format(self.DAY_7_PART_ONE_SOLUTION, challengeSolution))

    def testDay7PartTwo(self):
        challenge = Day7()
        challenge.setVerbose(self.verbose)
        challengeSolution = challenge.runPartTwo()
        self.assertEqual(challengeSolution, self.DAY_7_PART_TWO_SOLUTION, "Expected {0}, got {1}".format(self.DAY_7_PART_TWO_SOLUTION, challengeSolution))


if __name__ == '__main__':
    unittest.main()
