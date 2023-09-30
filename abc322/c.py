N, M = map(int, input().split(" "))
days = list(map(int, input().split(" ")))

for i in range(1, N + 1):
    if i in days:
        print(0)
    else:
        next_day = next(filter(lambda d: d > i, days))
        print(next_day - i)
