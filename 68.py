from itertools import permutations

def findLines(inner, outer):
    lines = []
    length = len(inner)
    for i in range(length):
        line = [outer[i], inner[i], inner[(i + 1) % length]]
        lines.append(line)
    return lines

def testSolution(inner, outer):
    lines = findLines(inner, outer)
    sums = set()
    for line in lines:
        sums.add(sum(line))
        if len(sums) != 1:
            return False
    return True

def minIndex(outer):
    winning = 9999
    winningI = -1
    for i in range(len(outer)):
        if outer[i] < winning:
            winning = outer[i]
            winningI = i
    return winningI

def makeString(solution):
    starting = minIndex(solution[1])
    lines = findLines(*solution)
    answer = lines[starting:] + lines[:starting]
    return "".join([str(num) for line in answer for num in line])

def findAll(n):
    # n as in magic n-gon ring
    possibilities = permutations(range(1, 2 * n + 1))
    workingSolutions = []
    for possibility in possibilities:
        solution = (possibility[:n], possibility[n:])
        if testSolution(*solution):
            workingSolutions.append(solution)
    return workingSolutions

# Strategy is to look at all 3,628,800 possibilities for the ring
# Find all the ones that work, then turn them all into strings,
# and find the biggest of the 16 digit long ones
# (takes about 8.5 seconds)

if __name__ == "__main__":
    strings = [makeString(solution) for solution in findAll(5)]
    print(max(string for string in strings if len(string) == 16))