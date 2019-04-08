def multiples_same(n):
    nums = ''.join(sorted(str(n)))
    for i in range(2,  7):
        if ''.join(sorted(str(n * i))) != nums:
            return False
    return True

counter = 0
while True:
    counter += 1
    if multiples_same(counter):
        print(counter)
        break