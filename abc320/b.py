S = input()

answer = 0

for i in range(len(S) + 1):
    for j in range(i + 1, len(S) + 1):
        substring = S[i:j]
        if substring == substring[::-1]:
            if answer < len(substring):
                answer = len(substring)

print(answer)
