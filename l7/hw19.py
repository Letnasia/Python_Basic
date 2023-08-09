import random


def common_elements(count):
    first_list = []
    for i in range(0, count, 3):
        first_list.append(i)
    second_list = []
    for i in range(0, count, 5):
        second_list.append(i)
    first_list = set(first_list)
    second_list = set(second_list)
    return first_list.intersection(second_list)


print(common_elements(100))
print(common_elements(1000))