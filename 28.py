nums = list(range(1, 1001 ** 2 + 1))
total = 0
increment = 2
idx = 0
while True:
    for i in range(4):
        if idx >= len(nums):
            break
        total += nums[idx]
        idx += increment
    if idx >= len(nums):
        break
    increment += 2

print(total)
