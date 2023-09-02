# Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
#
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
#
# Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з усім набором потрібних букв

# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

text = input('Enter two letters with hyphen between them: ')
a = string.ascii_letters.find(text[0])
b = string.ascii_letters.find(text[2])
print(string.ascii_letters[a:b + 1])
