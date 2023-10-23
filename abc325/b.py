N = int(input())
bases = [list(map(int, input().split())) for _ in range(N)]

totals = []
for h in range(0, 24):
    totals.append(
        sum(
            [
                headcount
                for headcount, offset in bases
                if (now := (h + offset) % 24) and now >= 9 and now <= 17
            ]
        )
    )

print(max(totals))
