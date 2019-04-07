class Memoizer:
    def __init__(self, func):
        self.func = func
        self.mems = {}
    def __call__(self, *args):
        if args not in self.mems:
            self.mems[args] = self.func(*args)
        return self.mems[args]

def waysToMake(coins, total):
    if total == 0:
        return 1
    if len(coins) == 0 or total < 0:
        return 0
    coinMax = max(coins)
    return mem(coins, total - coinMax) + mem(coins - frozenset({coinMax}), total)

mem  = Memoizer(waysToMake)
print(mem(frozenset({1, 2, 5, 10,  20, 50, 100, 200}), 200))