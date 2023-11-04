N = int(input())
S = input()

prev = ""
for char in S:
    if char == "a":
        if prev == "b":
            print("Yes")
            exit()
    if char == "b":
        if prev == "a":
            print("Yes")
            exit()
    prev = char

print("No")
