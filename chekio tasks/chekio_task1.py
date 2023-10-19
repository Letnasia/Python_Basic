def translate(text: str) -> str:
    vowels = "aeiouy"
    consonant = 'bcdfghjklmnpqrstvwxz'
    new_text = ''
    index = 0
    while index < len(text):
        if text[index] in consonant:
            new_text += text[index]
            index += 2
        elif text[index] in vowels:
                new_text += text[index]
                index += 3
        else:
            new_text += text[index]
            index += 1
    return new_text


print("Example:")
print(translate("hieeelalaooo"))


# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")