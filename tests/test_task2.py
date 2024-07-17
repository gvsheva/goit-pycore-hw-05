from decimal import Decimal

from pytest import fixture


@fixture
def text():
    return """Загальний дохід працівника складається з декількох частин:
1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00
доларів."""


def test_task2(text):
    from task2 import find_numbers, sum_numbers
    s = sum_numbers(text, find_numbers)
    assert s == Decimal("1351.46")
