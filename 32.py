nine_digit_products = []

for a in range(1, 5000):
    for b in range(1, 5000):
        prod = a * b
        str_rep = str(a) + str(b) + str(prod)
        if len(str_rep) == 9:
            nine_digit_products.append((str_rep, prod))


def is_pandigital(n):
    return "".join(sorted(str(n))) == "123456789"

pans = set()

for sprod in nine_digit_products:
    if is_pandigital(sprod[0]):
        pans.add(sprod[1])

print(sum(pans))