# sys.exit
# sys.argv

# import sys
# sys.argv

from pathlib import Path
from sys import argv
from colorama import Fore, Style

# import venv

# print(argv)

folder_path = '.' if len(argv) != 2 else argv[1]

p = Path(folder_path)

# print("\033[31;1;4mHello\033[0m")

for folder_item in p.iterdir():
    if folder_item.is_dir():
        print(Fore.BLUE + str(folder_item) + '/' + Style.RESET_ALL)
    else:
        print(folder_item)

# [x for x in p.iterdir() if x.is_dir()]
# folders = []
# for x in p.iterdir():
#     if x.is_dir():
#         folders.append(x)

# if len(argv) != 2:
#     print("No path provided")
#     folder_path = '.'
# else:
#     folder_path = argv[1]
# print(folder_path)
