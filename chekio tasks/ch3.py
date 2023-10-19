# def is_ascending(items: list) -> bool:
#     i = 0
#     while i < len(items) - 1:
#         if items[i] >= items[i + 1]:
#             return False
#
#         i += 1
#     return True
# print("Example:")
# print(is_ascending([-5, 10, 99, 123456]))
#
# # These "asserts" are used for self-checking
# assert is_ascending([-5, 10, 99, 123456]) == True
# assert is_ascending([99]) == True
# assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
# assert is_ascending([]) == True
# assert is_ascending([1, 1, 1, 1]) == False
# assert is_ascending([1, 3, 3, 5]) == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

def words_order(text: str, words: list) -> bool:
    # result = {i for i in text.split() if i in words}
    # return sorted(result, key=text.index) == words

    if len(set(words)) < len(words):
        return False
    text_new = []
    for i in text.split():
        if i in words and i not in text_new:
            text_new.append(i)

    return text_new == words
print("Example:")
print(words_order("hi world im here", ["world", "here"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
    words_order("hi world world im here hi world world im here", ["world", "here"])
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
