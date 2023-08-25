num_of_500_yen_coins, num_of_100_yen_coins, num_of_50_yen_coins, amount = [
    int(input()) for _ in range(4)
]

count = 0
for i in range(num_of_500_yen_coins + 1):
    for j in range(num_of_100_yen_coins + 1):
        for k in range(num_of_50_yen_coins + 1):
            if amount == (500 * i + 100 * j + 50 * k):
                count += 1

print(count)
