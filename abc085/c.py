import itertools
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
    for perm in list(itertools.permutations((10_000, 5_000, 1_000))):
        balance = total_amount
        counter = BillCounter()
        for bill in perm:
            property_name = "one_thousand"
            if bill == 10_000:
                property_name = "ten_thousand"
            elif bill == 5_000:
                property_name = "five_thousand"
            setattr(counter, property_name, balance // bill)
            balance = total_amount - counter.total_amount
            if (counter.total_count == num_of_bills) and (
                counter.total_amount == total_amount
            ):
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
