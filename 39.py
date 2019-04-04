import math
def get_trips_under(n):
    trips = []
    for b in range(n):
        for a in range(1, b):
            c = math.sqrt( a * a + b * b)
            if c % 1 == 0:
                trips.append((a, b, int(c)))
    return trips

trips = get_trips_under(3000)
p_counts = {i: 0 for i in range(1001)}

for trip in trips:
    p = sum(trip)
    if p <= 1000:
        p_counts[p] += 1

winner = -1
winning_val = -1
for p in p_counts:
    if p_counts[p] > winner:
        winner = p_counts[p]
        winning_val = p

print(winning_val)