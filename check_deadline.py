import datetime


def get_current_date():
    # Возвращает текущую дату в формате день-месяц-год.
    return datetime.datetime.now().strftime("%d-%m-%Y")


def parse_issue_date(issue_date_str):
    # Возвращает дату как обьект из строки с датой

    try:
        return datetime.datetime.strptime(issue_date_str, "%d-%m-%Y").date()

    except ValueError:
        raise ValueError(
            "Некорректный формат даты. Убедитесь,"
            " что вводите дату в формате день-месяц-год"
            " (например, 10-12-2024).")



def check_deadline(issue_date):
    # Сравнивает дату дедлайна с текущей датой и выводит соответствующее сообщение.
    current_date = datetime.date.today()

    if issue_date < current_date:
        days_overdue = (current_date - issue_date).days
        return f"Внимание! Дедлайн истёк {days_overdue} дня(ей) назад."
    elif issue_date == current_date:
        return "Дедлайн сегодня!"
    else:
        days_left = (issue_date - current_date).days
        return f"До дедлайна осталось {days_left} дня(ей)."


def main():
    print(f"Текущая дата: {get_current_date()}")

    while True:
        issue_date_str = input("Введите дату дедлайна (в формате день-месяц-год): ")
        try:
            issue_date = parse_issue_date(issue_date_str)

            break
        except ValueError as e:
            print(e)
    result_message = check_deadline(issue_date)
    print(result_message)


if __name__ == "__main__":
     main()

