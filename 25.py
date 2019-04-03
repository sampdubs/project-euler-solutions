fibs = [1, 1]

while True:
    new = fibs[-1] + fibs[-2]
    fibs.append(new)
    if len(str(new)) >= 1000:
        break

print(len(fibs))