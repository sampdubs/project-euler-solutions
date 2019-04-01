length_table = {0:0, 1:0}

def collatz_length(n):
    start = n
    length = 0
    while n > 1:
        if n % 2 == 0 :
            n /= 2
        else:
            n = 3 * n + 1
        length += 1
        if n in length_table:
            length += length_table[n]
            break
    length_table[start] = length
    return length

winner = 0
winning_length = -1

for n in range(1000000):
    value = collatz_length(n)
    if value > winning_length:
        winner = n
        winning_length = value
print(winner)
print(winning_length)