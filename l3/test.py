# # def most_frequent(data: list[str]) -> str:
# #       return max(data, key=data.count)
# #
# #
# # print("Example:")
# # print(most_frequent(["a", "b", "c", "a", "b", "a"]))
#
#
# from collections.abc import Iterable
#
#
# def compress(items: list[int]) -> Iterable[int]:
#     for ind, val in enumerate(items):
#         if not ind or val != items[ind - 1]:
#             yield val
#
#
#
# print("Example:")
# print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))
#
# # These "asserts" are used for self-checking
# assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
#     5,
#     4,
#     5,
#     6,
#     5,
#     7,
#     8,
#     0,
# ]
# assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
# assert list(compress([7, 7])) == [7]
# assert list(compress([])) == []
# assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
# assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
# assert list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")


FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(num: int) -> str:
    res = []
    num = str(num)
    ones = int(num[-1])
    if len(num) > 1:
        tens = int(num[-2])
    else:
        tens = 0
    if len(num) > 2:
        hundreds = int(num[-3])
    else:
        hundreds = 0

    if hundreds:
        res.append(FIRST_TEN[hundreds - 1])
        res.append(HUNDRED)
    if tens == 1:
        res.append(SECOND_TEN[ones])
    else:
        if tens:
            res.append(OTHER_TENS[tens - 2])
        if ones:
            res.append(FIRST_TEN[ones - 1])

    return " ".join(res)


print("Example:")
print(checkio(23))


# These "asserts" are used for self-checking
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
assert checkio(5) == "five"
assert checkio(6) == "six"
assert checkio(9) == "nine"
assert checkio(10) == "ten"
assert checkio(11) == "eleven"
assert checkio(12) == "twelve"
assert checkio(13) == "thirteen"
assert checkio(14) == "fourteen"
assert checkio(15) == "fifteen"
assert checkio(16) == "sixteen"
assert checkio(17) == "seventeen"
assert checkio(18) == "eighteen"
assert checkio(19) == "nineteen"
assert checkio(999) == "nine hundred ninety nine"
assert checkio(784) == "seven hundred eighty four"
assert checkio(777) == "seven hundred seventy seven"
assert checkio(88) == "eighty eight"
assert checkio(44) == "forty four"
assert checkio(20) == "twenty"
assert checkio(30) == "thirty"
assert checkio(40) == "forty"
assert checkio(50) == "fifty"
assert checkio(80) == "eighty"
assert checkio(90) == "ninety"
assert checkio(100) == "one hundred"
assert checkio(200) == "two hundred"
assert checkio(300) == "three hundred"
assert checkio(600) == "six hundred"
assert checkio(700) == "seven hundred"
assert checkio(900) == "nine hundred"
assert checkio(21) == "twenty one"
assert checkio(312) == "three hundred twelve"
assert checkio(302) == "three hundred two"
assert checkio(509) == "five hundred nine"
assert checkio(753) == "seven hundred fifty three"
assert checkio(940) == "nine hundred forty"
assert checkio(999) == "nine hundred ninety nine"

print("The mission is done! Click 'Check Solution' to earn rewards!")
