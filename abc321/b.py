N, X = map(int, input().split())
scores = list(map(int, input().split()))

for score in range(101):
    simulated_score = [*scores, score]
    if sum(sorted(simulated_score)[1:-1]) >= X:
        print(score)
        exit()

print(-1)
