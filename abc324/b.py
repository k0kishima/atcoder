N = int(input())

x = 0
y = 0

while N % 2 == 0 and N > 0:
    N //= 2
    x += 1

while N % 3 == 0 and N > 0:
    N //= 3
    y += 1

print("Yes" if N == 1 else "No")
