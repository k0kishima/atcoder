N = int(input())
S = input()

for i in range(N + 1):
    for j in range(i + 1, N + 1):
        if S[i:j].startswith("ABC"):
            print(i + 1)
            exit()

print(-1)
