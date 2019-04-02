import datetime

total_sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        day = datetime.date(year, month, 1)
        if day.weekday() == 6:
            total_sundays  += 1

print(total_sundays)
