# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

text = input('Enter two letters with hyphen between them: ')
a = string.ascii_letters.find(text[0])
b = string.ascii_letters.find(text[2])
print(string.ascii_letters[a:b + 1])
