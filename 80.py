from decimal import getcontext, Decimal
getcontext().prec = 110


def digital_sqrt_sum(n):
    num = str(Decimal(n).sqrt())
    if "." not in num:
        return 0
    num = num.replace(".", "")
    return sum(int(d) for d in num[:100])

print(sum(digital_sqrt_sum(n) for n in range(100)))