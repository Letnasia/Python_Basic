# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

import random

my_list = [random.randint(1, 10) for i in range(random.randint(3, 10))]
new_list = [my_list[0], my_list[2], my_list[-2]]
print(my_list)
print(new_list)