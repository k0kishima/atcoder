from typing import List

n = int(input())
integers: List[int] = list(map(int, input().split()))

if len(integers) != n:
    raise ValueError(f"{n}個の数値が渡されるとされる前提に対して実際には{len(integers)}個が渡されています")

count = 0
while all(i % 2 == 0 for i in integers):
    integers = [i // 2 for i in integers]
    count += 1

print(count)
