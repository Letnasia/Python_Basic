def find_first_word(text):
    i = 0
    while i < len(text) and text[i] != ' ':
        i += 1
    return text[:i]


print(find_first_word('dgdhb  fgdbc sgdgd gdh '))
