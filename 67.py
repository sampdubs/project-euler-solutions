from dataclasses import dataclass

@dataclass
class Node:
    val: int
    left: int = 0
    right: int = 0

    def choose_best(self):
        self.val += max(self.left, self.right)

with open("67_triangle.txt") as fs:
    triangle = [[int(num) for num in row.split(" ")] for row in fs.read().split("\n")]

# turn the bottom row into nodes

for j in range(len(triangle[-1])):
    triangle[-1][j] = Node(triangle[-1][j])

# Starting at the bottom, each node chooses which ever child is greater,
# and adds it to itself. Doing this all the way up the triangle
# results in the final node choosing the largest possible sequence sum

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] = Node(triangle[i][j], triangle[i + 1][j].val, triangle[i + 1][j + 1].val)
        triangle[i][j].choose_best()

print(triangle[0][0].val)