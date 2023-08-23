EVEN_DIGIT = {
    '0': True,
    '1': False,
    '2': True,
    '3': False,
    '4': True,
    '5': False,
    '6': True,
    '7': False,
    '8': True,
    '9': False
}


def is_even(number):
    number = str(number)
    return EVEN_DIGIT[number[-1]]


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
