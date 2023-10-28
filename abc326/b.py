N = int(input())

for n in range(N, 1000):
    a, b, c = map(int, list(str(n)))
    if a * b == c:
        print(n)
        exit()
