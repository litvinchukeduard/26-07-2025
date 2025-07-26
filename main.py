from itertools import zip_longest

my_list = ['hello', 'world', 3, 7]
my_list_two = [4, 5, 6, 7, 8]
# # print(my_list[1:])
# # item_one_path, item_two_path = my_list[1], my_list[2]
# item_one_path, item_two_path = my_list[1:]
# # item_two_path = my_list[2]

# for index, element in enumerate(my_list):
#     print(index)
#     print(element)

for el in zip_longest(my_list, my_list_two, fillvalue=''):
    print(el)

# for index, (first_list_element, second_list_element) in enumerate(zip(my_list, my_list_two)):
#     print(index, first_list_element, second_list_element)
# print(item_one_path)
# print(item_two_path)
