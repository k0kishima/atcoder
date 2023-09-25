N = input()

should_be_bigger = 10
for str_int in N:
    i = int(str_int)
    if i >= should_be_bigger:
        print("No")
        exit()
    should_be_bigger = i

print("Yes")
