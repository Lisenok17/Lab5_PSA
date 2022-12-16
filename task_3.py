dice = Dice(count=5)
statistics = []
for n in range(100000):
    result = dice.roll()
    statistics.append(result[0] + result[1])
for n in range(2, 12):
    print(n, statistics.count(n))
