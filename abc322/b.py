N, M = map(int, input().split(" "))
S = input()
T = input()

if T.startswith(S) and T.endswith(S):
    print(0)
    exit()

if T.startswith(S):
    print(1)
    exit()

if T.endswith(S):
    print(2)
    exit()

print(3)
