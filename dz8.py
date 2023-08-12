# Задача №49.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def work_with_phonebook():
    choise = show_menu()

    phone_book = read_txt('phonebook.txt')

    while choise != 9:

        if choise == 1:
            print_result('phonebook.txt')
        elif choise == 2:
            last_name = input('Введите фамилию: ')
            print('Номер телефона: ',find_by_lastname(phone_book,last_name))
        elif choise == 3:
            last_name = input('Какой номер хотите изменить: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book,last_name,new_number)) #перезапись в словаре
            # write_txt('phonebook.txt', change_number(phone_book,last_name,new_number)) #перезапись в файл
        elif choise == 4:
            last_name = input('Введите фамилию для удаления записи: ')
            print(delete_by_lastname(phone_book,last_name)) #удаление записи в словаре
            write_txt('phonebook.txt', delete_by_lastname(phone_book,last_name)) #удаление записи в файле
        elif choise == 5:
            number = input('Введите номер телефона: ')
            print('Фамилия: ',finf_by_number(phone_book,number))
        elif choise == 6:
            user_data = [input('Введите фамилию абонента: '),
                         input('Введите имя абонента: '),
                         input('Введите отчество абонента: '),
                         input('Введите номер телефона абонента: ')]
            print(add_user(phone_book,user_data))
            write_txt('phonebook.txt',phone_book)
        elif choise == 7:
            last_name = input('Введите фамилию: ')
            key_name = int(input('Какой параметр хотите изменить (1-фамилия,2-имя,3-отчество,4-телефон): '))
            new_value = input('Что хотите добавить: ')
            print(change_value(phone_book,last_name,key_name,new_value)) #перезапись в словаре
            # write_txt('phonebook.txt', change_number(phone_book,last_name,new_number)) #перезапись в файл
        elif choise == 8:
            last_name = input('Введите фамилию: ')
            last_value = input('Что хотите удалить: ')
            print(delete_value(phone_book,last_name,last_value)) #перезапись в словаре
            # write_txt('phonebook.txt', change_number(phone_book,last_name,new_number)) #перезапись в файл
        choise = show_menu()
def show_menu():
    print('Список команд:\n'
          '1. Распечатать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Найти абонента по фамилии и заменить информацию у него\n'
          '8. Найти абонента по фамилии и удалить информацию у него\n'
          '9. Закончить работу')
    choice=int(input("Введите команду: "))
    return choice
# чтение из файла (создание словаря, в котором будем работать)
def read_txt(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Отчество', 'Телефон']
    with open(filename,'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields,line.strip().split(',')))
            phone_book.append(record)
    return phone_book
# перезапись данных из словаря в файл
def write_txt(filename, phone_book):
    with open(filename,'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')
# печать данных из файла
def print_result(filename):
    print('В файле содержатся данные:')
    data = open(filename,'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()
# поиск номера телефона по фамилии
def find_by_lastname(phone_book, last_name):
    tel = None
    for i in phone_book:
         if i['Фамилия'] == last_name:
             tel = i['Телефон']
    return tel
# замена одного номера телефона на другой 
def change_number(phone_book,number_1,number_2):
    for i in phone_book:
        if i['Телефон'] == number_1:
            i['Телефон'] = number_2
    return phone_book
# удаление записи абонента
def delete_by_lastname(phone_book,last_name):
    for i in phone_book:
        if i['Фамилия'] == last_name:
            i['Фамилия'], i['Имя'], i['Отчество'], i['Телефон'] = '', '', '', '',
    return phone_book
# поиск фамилии по заданному номеру телефона
def finf_by_number(phone_book, number):
    fam = None
    for i in phone_book:
        if i['Телефон'] == number:
            fam = i['Фамилия']
    return fam
# добавление абонента в справочник
def add_user(phone_book, user_data):  
    phone_book.append({'Фамилия:': user_data[0], 
                       'Имя:': user_data[1], 
                       'Отчество:': user_data[2], 
                       'Телефон:': user_data[3]})
    return phone_book
# замена информации у абонента
def change_value(phone_book,last_name,key_name,new_value):
    for i in phone_book:
        if i['Фамилия'] == last_name:
            if key_name == 1:
                i['Фамилия'] = new_value
            elif key_name == 2:
                i['Имя'] = new_value
            elif key_name == 3:
                i['Отчетство'] = new_value
            elif key_name == 4:
                i['Телефон'] = new_value
    return phone_book
# удаление информации у абонента
def delete_value(phone_book,last_name,last_value):
    for i in range(len(phone_book)):
        for v in phone_book[i].values():
            if v == last_name:
                list_keys = list(phone_book[i].keys())
                list_values = list(phone_book[i].values())
                for j in range(len(list_values)):
                    if last_value == list_values[j]:
                        myKey = list_keys[j]
        phone_book[i][myKey] = ''
    return phone_book

work_with_phonebook()