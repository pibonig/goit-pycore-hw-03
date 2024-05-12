import random


def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    if not (0 < min_value < max_value <= 100 and quantity > 0):
        return []

    numbers = set()

    while len(numbers) < quantity:
        numbers.add(random.randint(min_value, max_value))

    numbers = list(numbers)
    numbers.sort()

    return numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
