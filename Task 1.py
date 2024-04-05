import os
clear = lambda: os.system('clear')
clear()

from csv import DictReader, DictWriter
from os.path import exists

file_name = 'phone.csv'
file_name2 = 'phone(copy).csv'

def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите телефон: '))
            if len(str(phone_number)) != 11:
                print('Неверная длина номера')
            else:
                flag = True
        except ValueError:
            print('Невалидный номер')
    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['Имя','Фамилия','Телефон'])
        f_w.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8',newline='') as data:
        f_r = DictReader(data)
        return list(f_r)

def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {'Имя': lst[0], 'Фамилия':lst[1], 'Телефон': lst[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8',newline='') as data:
        f_w = DictWriter(data, fieldnames=['Имя','Фамилия','Телефон'])
        f_w.writeheader()
        f_w.writerows(res)

def copy_string(file_name, file_name2):
    string = list(map(int ,input('Введите номер строки/ номера строк (через пробел): ').split()))
    with open(file_name) as file_name, open(file_name2, 'w') as file_name2:
        for n, line in enumerate(file_name):
            if n == 0:
                file_name2.write(line)
            if n in string:
                file_name2.write(line)


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_name):
                print('Сначала создайте файл')
                continue
            copy_string(file_name, file_name2)
main()