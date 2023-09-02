# def get_min(*args): # упаковка аргументов в кортеж
#     if not args:
#         return None
#     min_element = args[0]
#     for element in args:
#         if element < min_element:
#             min_element = element
#     return min_element
#
# a = get_min()
# print(a)


hill = [[7],
        [5, 8],
        [9, 8, 2],
        [1, 3, 5, 6],
        [6, 2, 4, 4, 5],
        [9, 5, 3, 5, 5, 7],
        [7, 4, 6, 4, 7, 6, 8]]

def gold(arr):
    for i in range(len(arr) - 1, 0, -1):
        for y in range(len(arr[i]) - 1, 0, -1):
            a = arr[i][y] + arr[i-1][y - 1]
            b = arr[i][y - 1] + arr[i-1][y - 1]
            arr[i - 1][y - 1] = max(a, b)
    for ar in arr:
        print(ar)

gold(hill)