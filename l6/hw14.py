# 1000 -> 0
# 423 -> 8
# 1 -> 1
# 999 -> 2

dig = int(input('Enter integer number: '))

while dig > 10:
    dig_str = str(dig)
    dig = 1
    for val in dig_str:
        val = int(val)
        dig *= val
print(dig)