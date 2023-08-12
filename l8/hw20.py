def add_one(some_list):
    number = 0
    for dig in some_list:
        number = number * 10 + dig
    number = number + 1
    number = str(number)
    lst = []
    for i in number:
        lst.append(int(i))
    return lst


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
