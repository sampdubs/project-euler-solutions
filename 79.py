raw = open("keylog.txt").read()
history = raw.split("\n")[:-1]
from collections import defaultdict

# def agrees(solution, hint):
#     for digit in hint:
#         try:
#             idx = solution.index(digit)
#             solution = solution[idx + 1:]
#         except ValueError:
#             return False
#     return True

# def isPossible(solution):
#     solution = str(solution)
#     for hint in history:
#         if not agrees(solution, hint):
#             return False
#     return True

# x = 0
# while not isPossible(x):
#     x += 1
#     if x % 100_000 == 0:
#         print(x)
# print(x)

before = defaultdict(set)
after = defaultdict(set)

for hint in history:
    before[hint[1]].add(hint[0])
    before[hint[2]].add(hint[0])
    before[hint[2]].add(hint[1])

# find number that has nothing before it
password = ""
while True:
    for i in range(10):
        i = str(i)
        if len(before[i]) == 0 and i in raw:
            password += i
            raw = raw.replace(i, "")
            for key in before:
                if i in before[key]:
                    before[key].remove(i)
    if raw.strip() == "":
        break
print(password)