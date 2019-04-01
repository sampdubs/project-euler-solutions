counter = 200
while True:
    counter += 20
    is_good = True
    for i in range(2, 21):
        if counter % i != 0:
            is_good = False
            break
    print(counter)
    if is_good:
        break

print(counter)