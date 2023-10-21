H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append([True if m == "#" else False for m in list(input())])


def find_neighboring_indices_in(grid, point):
    neighbors = []
    row_idx, col_idx = point

    for i in range(-1, 2):
        for j in range(-1, 2):
            # 現在のセル
            if i == 0 and j == 0:
                continue
            n_row, n_col = row_idx + i, col_idx + j
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                neighbors.append((n_row, n_col))

    return neighbors


def dfs(row_idx, col_idx, grid, visited):
    if (
        row_idx < 0
        or row_idx >= len(grid)
        or col_idx < 0
        or col_idx >= len(grid[0])
        or visited[row_idx][col_idx]
        or not grid[row_idx][col_idx]
    ):
        return

    visited[row_idx][col_idx] = True

    for r, c in find_neighboring_indices_in(grid, (row_idx, col_idx)):
        dfs(r, c, grid, visited)


visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
count = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] and not visited[i][j]:
            dfs(i, j, grid, visited)
            count += 1

print(count)
