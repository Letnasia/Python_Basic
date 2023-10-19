def end_zeros(number: int) -> int:
    number = str(number)
    res = 0
    for i in range(-1, -len(number)-1, -1):
        if number[i] != '0':
            break
        res += 1
    return res


print("Example:")
print(end_zeros(10666))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
