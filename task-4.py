from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    result = []

    now = datetime.now().date()

    for user in users:
        user_birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        user_birthday_this_year = user_birthday.replace(year=now.year)

        if user_birthday_this_year < now:
            user_birthday_this_year = user_birthday_this_year.replace(year=now.year + 1)

        days_to_user_birthday = (user_birthday_this_year - now).days

        if 0 <= days_to_user_birthday <= 7:
            weekday = user_birthday_this_year.weekday()
            if weekday >= 5:
                user_birthday_this_year += timedelta(days=7 - weekday)

            result.append({
                'name': user['name'],
                'congratulation_date': user_birthday_this_year.strftime('%Y.%m.%d'),
            })

    return result


users = [
    {'name': 'John Doe', 'birthday': '1985.01.23'},
    {'name': 'Jane Smith', 'birthday': '1990.01.27'},
    {'name': 'Ann Brown', 'birthday': '1980.05.05'},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print('Список привітань на цьому тижні:', upcoming_birthdays)
