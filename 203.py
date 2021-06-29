def flatten(stack):
    flat = []
    for layer in stack:
        for num in layer:
            flat.append(num)
    return flat

def pasctri(n): # n is the number of layers
    triangle = [[1]]
    for layer in range(1, n): # number of nums in layer is equivalent to layer + 1
        triangle.append([])
        for position in range(layer + 1):
            num = 0
            num_index = len(triangle[layer]) # index where num will be put at
            # To find a parent, look up one layer at num_index, and up one layer at num_index - 1
            if len(triangle[layer - 1]) > num_index: # up one layer, does it have this index
                num += triangle[layer - 1][num_index]
            if num_index > 0: # up one layer, can I look left one index
                num += triangle[layer - 1][num_index - 1]
            triangle[layer].append(num)
    return flatten(triangle)

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for m in range(5, int(n ** 0.5), 6):
        if n % m == 0 or n % (m + 2) == 0:
            return False
    return True

def next_prime(n): # Find next prime larger than n
    if n <= 1:
        return 2
    
    while (n := n + 1):
        if is_prime(n):
            return n

def is_squarefree(n, primes): # A positive integer n is called squarefree if no square of a prime divides n
    next_check_index = 0
    next_check = primes[next_check_index] * primes[next_check_index]

    while next_check <= n:
        if n % next_check == 0:
            return False
        next_check_index += 1
        if next_check_index >= len(primes):
            primes.append(next_prime(primes[-1]))
        next_check = primes[next_check_index] * primes[next_check_index]
    return True

if __name__ == "__main__":
    primes = [2]
    nums = pasctri(51)
    squarefrees = {num for num in nums if is_squarefree(num, primes)}
    print(sum(squarefrees))
