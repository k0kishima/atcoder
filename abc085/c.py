from dataclasses import dataclass
from typing import Tuple


@dataclass
class BillCounter:
    ten_thousand: int = 0
    five_thousand: int = 0
    one_thousand: int = 0

    @property
    def total_amount(self) -> int:
        return (
            self.ten_thousand * 10_000
            + self.five_thousand * 5_000
            + self.one_thousand * 1_000
        )

    @property
    def total_count(self) -> int:
        return self.ten_thousand + self.five_thousand + self.one_thousand


def calculate_breakdown_bills(
    num_of_bills: int, total_amount: int
) -> Tuple[int, int, int]:
    counter = BillCounter()

    for i in range(num_of_bills + 1):
        counter.ten_thousand = i

        for j in range(num_of_bills + 1):
            counter.five_thousand = j
            counter.one_thousand = num_of_bills - i - j

            if counter.one_thousand < 0 or counter.one_thousand > num_of_bills:
                continue

            if counter.total_amount == total_amount:
                return (
                    counter.ten_thousand,
                    counter.five_thousand,
                    counter.one_thousand,
                )

    return (-1, -1, -1)


if __name__ == "__main__":
    num_of_bills, total_amount = map(int, input().split())
    result = calculate_breakdown_bills(num_of_bills, total_amount)
    print(" ".join([str(item) for item in result]))
