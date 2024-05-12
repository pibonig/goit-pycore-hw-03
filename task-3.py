import re


def normalize_phone(phone_number: str) -> str:
    formated_phone_number = re.sub(r'[^0-9+]', '', phone_number)

    if re.match(r'^380', formated_phone_number) is not None:
        formated_phone_number = "+" + formated_phone_number
    elif re.match(r'^\+38', formated_phone_number) is None:
        formated_phone_number = "+38" + formated_phone_number

    return formated_phone_number


raw_numbers = [
    '067\\t123 4567',
    '(095) 234-5678\\n',
    '+380 44 123 4567',
    '380501234567',
    '    +38(050)123-32-34',
    '     0503451234',
    '(050)8889900',
    '38050-111-22-22',
    '38050 111 22 11   ',
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print('Нормалізовані номери телефонів для SMS-розсилки:', sanitized_numbers)
