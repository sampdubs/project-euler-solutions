import json

names = []
with open("22.txt") as f:
    names = json.loads("[" + f.read() + "]")

names.sort()
scores = []

def get_val(name):
    total = 0
    for char in name:
        total += ord(char) - 64
    return total

for i in range(len(names)):
    scores.append((i + 1) * get_val(names[i]))

print(sum(scores))