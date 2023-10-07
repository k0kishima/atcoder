N = int(input())

win_counts_indexed_by_player_number = {}
for i in range(N):
    result = input()
    win_counts_indexed_by_player_number[i + 1] = result.count("o")

sorted_data = sorted(
    win_counts_indexed_by_player_number.items(),
    key=lambda x: (x[1], -x[0]),
    reverse=True,
)
print(" ".join([str(n) for n, _ in sorted_data]))
