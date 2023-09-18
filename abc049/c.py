S = input()

keywords = ["dream", "dreamer", "erase", "eraser"]

result = False
while True:
    hit = next((k for k in keywords if S.endswith(k)), None)

    if S == hit:
        result = True
        break

    if hit is None:
        break

    S = S[: -len(hit)]

print("YES" if result else "NO")
