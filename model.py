import csv

from view import creating_info as info

def writing_csv(info): # создание файла csv
    with open ('file.csv', 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]},{info[3]}\n')


def writing_txt(info): # создание файла txt
    with open ('file.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nОтчество: {info[2]}\n\nНомер телефона: {info[3]}\n\n\n')


def csv_data_open():      # импорт из файла csv
    with open('file.csv', encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res


def export_csv_txt():     # экспорт из csv в txt
    list_csv = csv_data_open()
    for i in list_csv:
        s = ' '.join(i)
        with open('file_2.txt', 'a', encoding='utf-8') as f:
            f.writelines(s + '\n')