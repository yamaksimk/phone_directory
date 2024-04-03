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

def read_file2(file_name2):
    with open(file_name2, 'r', encoding='utf-8',newline='') as data:
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

def read_file_for_copy(file_name):
    with open(file_name, 'r') as file_name:
        for i, line in enumerate(file_name):
            print(i, line)


def copy_string(file_name2):
    print(read_file_for_copy(file_name))
    string = list(map(int ,input('Введите номера строки/строк (через пробел): ').split()))
    file1 = open('phone.csv')
    file2 = open('phone(copy).csv', 'w')
    for n, line in enumerate(file1):
        if n == 0:
            file2.write(line)
        if n in string:
            file2.write(line)
    file1.close()
    file2.close()

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
            copy_string(file_name2)
            print('Скопированные строки:')
            print(read_file2(file_name2))
main()