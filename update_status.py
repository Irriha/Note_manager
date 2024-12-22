# отображеие текущего статуса заметки

current_status = "в процессе"
while True:
    # цикл для изменения статуса по номеру
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
        print(current_status)
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите из предложенных вариантов.")

