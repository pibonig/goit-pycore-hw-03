from datetime import datetime


def get_days_from_today(date: str) -> int | str:
    try:
        diff = datetime.now() - datetime.strptime(date, '%Y-%m-%d')
        return abs(diff.days)
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD' format."


print(get_days_from_today('2021-10-09'))
