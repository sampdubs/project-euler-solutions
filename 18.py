nums = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split('\n')
for i in range(len(nums)):
    nums[i] = nums[i].split(' ')

for row in nums:
    for i in range(len(row)):
        row[i] = int(row[i])

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def add_right(self, node):
        self.right = node

    def add_left(self, node):
        self.left = node
    
    def find_max(self, counter=0):
        counter += self.val
        if ((self.right == None) and (self.left == None)):
            return counter
        else:
            return max(self.left.find_max(counter=counter), self.right.find_max(counter=counter))

tree = []

for i in range(len(nums)):
    tree.append([])
    for n in nums[i]:
        tree[i].append(Node(n))

# left of the same, right of the previous

for i in range(len(tree)):
    for j in range(len(tree[i])):
        if j > 0:
            tree[i - 1][j - 1].add_right(tree[i][j])
        if j < len(tree[i - 1]) and i - 1 >= 0:
            tree[i - 1][j].add_left(tree[i][j])

print(tree[0][0].find_max())