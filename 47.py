from primefac import primefac


facts = {}
def get_num_fac(n):
    if n in facts:
        return len(facts[n])
    facs = set(primefac(n))
    facts[n] = facs
    return len(facs)

i = 646
while True:
    i += 1
    if get_num_fac(i) == 4 and get_num_fac(i + 1) == 4 and get_num_fac(i + 2) == 4 and get_num_fac(i + 3) == 4:
        print(i)
        break
