#список введенных словарей для переборки
notes = [{'Имя пользователя': 'ира', 'Заголовок заметки': 'покупки', 'Описание заметки': 'бананы яблоки творог', 'Статус заметки': 'в процессе', 'Дата создания заметки': '22-12-2024', 'Дедлайн': '23-12-2024'}, {'Имя пользователя': 'кирилл', 'Заголовок заметки': 'дела', 'Описание заметки': 'работа зал книга', 'Статус заметки': 'в процессе', 'Дата создания заметки': '22-12-2024', 'Дедлайн': '23-12-2024'}]
while True:  #цикл для входа в главное меню
    print("\nМеню:")
    print("3. Создать новую заметку")
    print("4. Выйти")

    choice = input("Введите номер действия: ")
    if choice == "3":
        #цикл для переборки элементов списка
        for i in notes:
            #цикл для переборки элементов словаря
            for j, value in i.items():
                j = input('Ведите имя пользователя или заголовок заметки: ')
                if value == j:
                    notes.remove(i)   #удаление заметки при совпадении условий
                    print('Успешно удалено. Остались следующие заметки: ')
                    print(notes)
                    break

    elif choice == "4":
        print("Спасибо за использование менеджера заметок. До свидания!")
        break
    else: print("Некорректный ввод. Пожалуйста, попробуйте снова.")