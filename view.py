def write_menu(): # меню для выбора типа файла
    print('Если Вы хотите создать файл csv наберите цифру 1')
    print('Если Вы хотите создать файл txt наберите цифру 2')
    return int(input('Введите цифру: '))


def number_entries(): # сколько записей сделать в тел книге
    num = int(input('Введите количество записей, которые Вы хотите сделать: '))
    return num

# print(number_entries())

def creating_info(): # создание записи по одному человеку
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    second_name = input('Введите отчество: ')
    info.append(second_name)
    tel = input('Введите номер телефона: ')
    info.append(tel)
    return info

# print(creating_info())

def menu_csv(): # выбор возможностей с csv файлом 
    print('Наберите цифру 1, если Вы хотите открыть файл')
    print('Наберите цифру 2, если Вы хотите экспортировать файл в формат txt')
    return int(input('Введите цифру: '))


def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))
