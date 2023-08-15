import sys
from typing import List


def create_bucket(numbers: List[int]) -> List[int]:
    bucket = [0] * (max(numbers) + 1)
    for number in numbers:
        bucket[number] += 1
    return bucket


if __name__ == "__main__":
    args: List[int] = []

    for l in sys.stdin:
        if value := l.strip():
            args.append(int(value))
        else:
            break

    bucket = create_bucket(args[1:])
    print(sum(1 for value in bucket if value != 0))
