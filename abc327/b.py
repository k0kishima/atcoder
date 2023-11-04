B = int(input())

x = B
n = 1
while x >= n:
    x = round(B ** (1 / n))
    if x**n == B and x == n:
        print(n)
        exit()
    n += 1

print("-1")
