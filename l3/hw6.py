lst = [12, 3, 4, 10]
# lst = [1]
# lst = []
# lst = [12, 3, 4, 10, 8]

# [12, 3, 4, 10] # => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]

if len(lst) == 0:
    print(lst)
else:
    a = lst.pop()
    lst.insert(0, a)
    print(lst)