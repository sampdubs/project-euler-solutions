from sympy import isprime

def get_prop_prime(nums):
    # return number of primes in nums / len of nums
    return [isprime(num) for num in nums].count(True) / len(nums)

def smart_get_diags(sidelen):
    # to generate the diagonals, simply start at 1, then add 2 4 times, then add 4 4 times, then 6, etc.
    assert sidelen % 2 == 1, "sidelen must be odd"
    maxadd = sidelen - 1
    diags = [1]
    adding = 2
    while adding <= maxadd:
        for _ in range(4):
            diags.append(diags[-1] + adding)
        adding += 2
    return diags

if __name__ == "__main__":
    prop = 1
    sidelen = 1
    # do a binary search of sorts by taking big steps until you get below 0.1, then find where exactly it crosses 0.1
    step = 512
    while step > 1:
        while prop >= 0.1:
            sidelen += step
            diags = smart_get_diags(sidelen)
            prop = get_prop_prime(diags)
            print(sidelen, prop)
        sidelen = sidelen - step
        step //= 2
        prop = 1
    print(sidelen + 2)