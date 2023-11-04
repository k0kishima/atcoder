from pprint import pprint

grid = [list(map(int, input().split())) for _ in range(9)]

if not all([len(set(row)) == 9 for row in grid]):
    print("No")
    exit()

transposed_grid = list(zip(*grid))
if not all([len(set(row)) == 9 for row in transposed_grid]):
    print("No")
    exit()

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        sub_grid = [row[j : j + 3] for row in grid[i : i + 3]]
        if len(set(item for r in sub_grid for item in r)) != 9:
            print("No")
            exit()

print("Yes")
