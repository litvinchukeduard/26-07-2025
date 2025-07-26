from sys import argv, exit
from pathlib import Path
from itertools import zip_longest

'''
Important: we assummed that both files are not big
'''

if len(argv) != 3:
    print('Please provide file paths for two files')
    exit()

item_one_path, item_two_path = argv[1:]


item_one = Path(item_one_path)
item_two = Path(item_two_path)

if item_one.is_dir() and item_two.is_dir():
    print(f'Both paths "{item_one}" "{item_two}" are folders')
    exit()

if item_one.is_dir():
    print(f'{item_one} is a folder')
    exit()

if item_two.is_dir():
    print(f'{item_two} is a folder')
    exit()

with open(item_one) as file_one:
    file_one_lines = file_one.readlines()

with open(item_two) as file_two:
    file_two_lines = file_two.readlines()

# my_list = [1, 2, 3, 7]
# my_list_two = [4, 5, 6, 7]
# 1 -> 4, 5, 6, 7
# 2 -> 4, 5, 6, 7
# for line in file_one_lines:
#     for line_two in file_two_lines:
#         ...

# Скажемо що обидва списки однакової довжини
# for i in range(len(file_one_lines)):
#     # file_one_lines[i]
#     # file_two_lines[i]
#     first_file_line = file_one_lines[i]
#     second_file_line = file_two_lines[i]
#     if first_file_line != second_file_line:
#         print(i + 1)
#         print(f"> {first_file_line.rstrip()}")
#         print(f"< {second_file_line.rstrip()}")

# for first_file_line, second_file_line in zip(file_one_lines, file_two_lines):
#     if first_file_line != second_file_line:
#         # print(i + 1)
#         print(f"> {first_file_line.rstrip()}")
#         print(f"< {second_file_line.rstrip()}")

for i, (first_file_line, second_file_line) in enumerate(zip_longest(file_one_lines, file_two_lines, fillvalue='')):
    if first_file_line != second_file_line:
        print(i + 1)
        print(f"> {first_file_line.rstrip()}")
        print(f"< {second_file_line.rstrip()}")

