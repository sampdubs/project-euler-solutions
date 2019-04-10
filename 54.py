def hand_to_tup(hand):
    nums = {}
    ntos = {}
    stoint = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    hand = hand.split(' ')
    suitset = set()
    for card in hand:
        num = stoint[card[0]]
        suit = card[1]
        if num in nums:
            nums[num] += 1
            ntos[num].append(suit)
        else:
            nums[num] = 1
            ntos[num] = [suit]
        suitset.add(suit)
    numset = set(nums)
    if len(suitset) == 1:
        if numset == {10, 11, 12, 13, 14}:
            return (9,)
        mxn = max(numset)
        stdn = sorted(numset)
        if len(numset) == 5 and stdn == list(range(min(numset), mxn + 1)):
            return (8, mxn)
        return (5,) + tuple(stdn[::-1])
    lnns = len(numset)
    if lnns == 2:
        if set(nums.values()) == {1, 4}:
            for num, count in nums.items():
                if count == 4: fourKind = num
                else: oneKind = num
            return (7, fourKind, oneKind)
        else:
            for num, count in nums.items():
                if count == 3: threeKind = num
                else: twoKind = num
            return (6, threeKind, twoKind)
    elif lnns == 3:
        if set(nums.values()) == {1, 1, 3}:
            others = []
            for num, count in nums.items():
                if count == 3: threeKind = num
                else: others.append(num)
            return (3, threeKind, max(others), min(others))
        else:
            twoKinds = []
            for num, count in nums.items():
                if count == 2: twoKinds.append(num)
                else: oneKind = num
            return (2, max(twoKinds), min(twoKinds), oneKind)
    elif lnns == 4:
        others = []
        for num, count in nums.items():
            if count == 2: twoKind = num
            else: others.append(num)
        return (1, twoKind) + tuple(sorted(others)[::-1])
    else:
        stdn = sorted(numset)
        if stdn == list(range(min(numset), max(numset) + 1)):
            return (4,) + tuple(stdn[::-1])
        else:
            return (0,) + tuple(stdn[::-1])

hands = []

with open('54.txt') as f:
    for line in f.read().split('\n')[:-1]:
        hands.append([line[:14], line[15:]])

p1wins = 0
for h in hands:
    if hand_to_tup(h[0]) > hand_to_tup(h[1]):
        p1wins += 1

print(p1wins)