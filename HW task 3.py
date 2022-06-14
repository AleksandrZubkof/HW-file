from pprint import pprint
import os

base_path = os.getcwd()
logs_file_list = os.listdir()
logs_file_list.sort()
logs_file_list_2 = logs_file_list[1:4]

dict_file = {}
dict_file_2 = {}
for file in logs_file_list_2:
    with open(file, 'r', encoding='utf-8') as file_book:
        data = file_book.readlines()
        data = [line.strip() for line in data]
        dict_file_2[file] = data
        dict_file[file] = len(data)

sorted_dict = {}
sorted_keys = sorted(dict_file, key=dict_file.get)

for w in sorted_keys:
    sorted_dict[w] = dict_file[w]

with open('4.txt', 'a', encoding='utf-8') as file_book_2:
    for key, value in sorted_dict.items():
        file_book_2.write(f'{key}\n')
        file_book_2.write(f'{value}\n')
        x = '\n'.join(dict_file_2[key])
        file_book_2.write(f'{x}\n')
