from ..c import calculate_breakdown_bills


def test_calculation() -> None:
    breakpoint()
    assert calculate_breakdown_bills(9, 45000) == (4, 0, 5)
