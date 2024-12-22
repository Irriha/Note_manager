
import datetime

print('Добро пожаловать в "Менеджер заметок"!')
print('Вы можете добавлять новые заметки.')



# Функция для получения текущей даты
def get_current_date():
    # Возвращает текущую дату в формате день-месяц-год
    return datetime.datetime.now().strftime("%d-%m-%Y")


# Функция для парсинга даты дедлайна
def parse_issue_date(issue_date_str):
    try:
        # Преобразует строку с датой в объект datetime.date
        return datetime.datetime.strptime(issue_date_str, "%d-%m-%Y").date()
    except ValueError:
        raise ValueError(
            "Некорректный формат даты. Убедитесь, "
            "что вводите дату в формате день-месяц-год "
            "(например, 10-12-2024)."
        )


# Функция для создания заметки
def create_note():
    note = {}  # Словарь для хранения данных заметки

    # Запрашиваем данные у пользователя
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")

    # Устанавливаем начальный статус
    current_status = "в процессе"

    while True:
        print("\nВыберите новый статус заметки:")
        print("1. выполнено")
        print("2. в процессе")
        print("3. отложено")
        print("4. завершить выбор статуса")

        status_choice = input("Введите номер статуса: ")

        if status_choice == "1":
            current_status = "выполнено"
        elif status_choice == "2":
            current_status = "в процессе"
        elif status_choice == "3":
            current_status = "отложено"
        elif status_choice == "4":
            print("Статус заметки успешно установлен.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите из предложенных вариантов.")

    # Получаем текущую дату создания заметки
    creation_date = get_current_date()

    # Ввод и обработка дедлайна
    while True:
        issue_date_str = input("Введите дату дедлайна (в формате день-месяц-год): ")
        try:
            deadline_date = parse_issue_date(issue_date_str)
            break  # Если дата корректна, выходим из цикла
        except ValueError as e:
            print(e)  # Выводим сообщение об ошибке и повторяем ввод

    # Сохраняем данные заметки в словарь
    note = {
        'Имя пользователя': username,
        'Заголовок заметки': title,
        'Описание заметки': content,
        'Статус заметки': current_status,
        'Дата создания заметки': creation_date,
        'Дедлайн': deadline_date.strftime("%d-%m-%Y")  # Преобразуем дату в строку для вывода
    }

    # Выводим финальную заметку
    print("\nЗаметка успешно создана!")
    print(note)
    return note  # выводим переменную из функции для дальнейшей работы с ней

# Основная функция
def main():
    notes = []  # список для сохранения заметок
    while True:
        print("\nМеню:")
        print("1. Создать новую заметку")
        print("2. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            notes.append(create_note()) # для добавления заметок в список
            print(notes)
        elif choice == "2":
            print("Спасибо за использование менеджера заметок. До свидания!")
            break
        else:
         print("Некорректный ввод. Пожалуйста, попробуйте снова.")

# точка входа для главной функции
if __name__ == "__main__":
     main()

