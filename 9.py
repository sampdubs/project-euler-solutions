def get_triples(n):
    triples = []
    a, b, c = 2, 3, 4
    while a <= n:
        a += 1
        b = a
        while b <= n:
            b += 1
            c = b
            while c <= n:
                c += 1
                if a ** 2 + b ** 2 == c ** 2:
                    triples.append([a, b, c])
    return triples

for trip in get_triples(500):
    if sum(trip) == 1000:
        print(trip[0] * trip[1] * trip[2])
        break
