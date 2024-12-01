#основные переменные
username = "Имя пользователя"
title = "Заголовок заметки"
content = "Содержание заметки"
status = "Статус"
created_date = "10-11-2024"
issue_date = "10-12-2024"


#ввод данных через input
username = input ("Введите имя пользователя ")
title = input ("Введите заголовок заметки ")
content = input ("Введите содержание заметки ")
status = input ("Введите статус заметки ")
created_date = input ('Введите дату создания заметки в формате "дд-мм-гггг" ')
issue_date = input ('Введите дату завершения заметки в формате "дд-мм-гггг" ')


#список заголовков
title_1 = input("Введите заголовок 1 ")
title_2 = input("Введите заголовок 2 ")
title_3 = input("Ведите заголовок 3 ")
titles = [title_1, title_2, title_3]


#преобразование дат

temp_created_date = created_date [0:5]
temp_issue_date = issue_date [0:5]


# организация данных в словарь
finall = {'Имя пользователя': username ,
         'Заголовок заметки': title ,
          'Описание заметки': content ,
            'Статус заметки': status ,
     'Дата создания заметки': temp_created_date ,
                   'Дедлайн': temp_issue_date }

finall['Подзаголовки'] = titles

print(finall)
