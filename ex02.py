import re
from typing import Callable

def generator_numbers(text: str):
    # Regular expression for finding numbers with with space before and after format
    pattern = r'\s\d+(?:\.\d+)?\s'
    numbers = re.findall(pattern, text)
    # Convert matches to float numbers
    for num in numbers:
        yield float(num)


def sum_profit(text: str, func: Callable):
    # Setting total sum to zero
    total = 0
    for number in func(text):
        total += number
    return total


text = (
    "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
)
n = sum_profit(text, generator_numbers)
print("Total profit amount is: ", n)



