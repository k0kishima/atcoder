N, M = map(int, input().split())

points = list(map(int, input().split()))
points.sort()

point_len = len(points)
left, right = 0, 0
record = 0

while right < point_len:
    while right < point_len and points[right] < points[left] + M:
        right += 1
    count = right - left

    if count > record:
        record = count

    left += 1

print(record)
