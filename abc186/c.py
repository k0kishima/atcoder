N = int(input())

unlucky_numbers = []

for i in range(1, N + 1):
    if "7" in (str(i)) or "7" in (oct(i)):
        unlucky_numbers.append(i)

print(N - len(unlucky_numbers))
