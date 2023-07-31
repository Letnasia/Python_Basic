# [1, 3, 5] => 30
# [6] => 36
# [] => 0

# lst = [6]
# lst = []
lst = [1, 3, 5]
summa = 0
if len(lst) != 0:
    for i in range(0, len(lst), 2):
        summa += lst[i]
    print(summa * lst[-1])
else:
    print(0)
