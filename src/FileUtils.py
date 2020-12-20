def readNumbersFromFile(filename):
    numbers = []
    with open(filename, "r") as file:
        numbers = [int(num) for line in file for num in line.split() ]
    return numbers

def writeLineToFile(filename, line):
    with open(filename, "a") as file:
        file.write(line)