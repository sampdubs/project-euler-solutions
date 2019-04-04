import json

def get_word_val(word):
    val = 0
    for let in word:
        val += ord(let) - 64
    return val

def get_tri_nums(n):
    nums = []
    for i in range(1, n + 1):
        nums.append(0.5 * i * (i + 1))
    return nums

words = None
with open("42.txt") as f:
    words = json.loads("[" + f.read() + "]")

tri_count = 0
tris = get_tri_nums(25)
for word in words:
    if get_word_val(word) in tris:
        tri_count += 1
print(tri_count)