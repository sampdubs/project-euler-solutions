from dataclasses import dataclass
from typing import Type
from math import inf

@dataclass
class Node:
    value: int
    dist: int = inf
    right: Type["Node"] = None
    above: Type["Node"] = None
    below: Type["Node"] = None
    prev: Type["Node"] = None
    def __hash__(self):
        return self.value

with open("matrix.txt") as matrixFile:
    matrix = [
        [Node(int(num)) for num in line.split(",")]
        for line in matrixFile.read().split("\n")[:-1]
    ]

for row in matrix:
    for i in range(len(row) - 1):
        row[i].right = row[i + 1]
    row[0].dist = row[0].value

for i in range(len(matrix) - 1):
    for j in range(len(matrix[i])):
        matrix[i][j].below = matrix[i + 1][j]

for i in range(1, len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j].above = matrix[i - 1][j]

# Use a set to accelerate removal and checking if vertex still remains
allVerticies = {vertex for row in matrix for vertex in row}

# Use Dijkstra's algorithm to compute shortest path
while len(allVerticies) > 0:
    vertex = min(allVerticies, key=lambda v: v.dist)
    
    allVerticies.remove(vertex)

    if (r := vertex.right) in allVerticies:
        alt = vertex.dist + r.value
        if alt < r.dist:
            r.dist = alt
            r.prev = vertex
    if (a := vertex.above) in allVerticies:
        alt = vertex.dist + a.value
        if alt < a.dist:
            a.dist = alt
            a.prev = vertex
    if (b := vertex.below) in allVerticies:
        alt = vertex.dist + b.value
        if alt < b.dist:
            b.dist = alt
            b.prev = vertex

print(min([row[-1] for row in matrix], key=lambda v: v.dist).dist)