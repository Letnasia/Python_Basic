# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
#
# Змінна не може:
#
#     - починатися з цифри,
#     - складатися тільки з цифр,
#     - містити великі літери, пропуск і знаки пунктуації (взяти можна тут string.punctuation),
#       окрім нижнього підкреслення "_".
#     - бути жодним із зареєстрованих слів.
# При цьому ім'я змінної може складатися тільки з одного нижнього підкреслення "_".
#
# Список зареєстрованих слів можна взяти із keyword.kwlist.
#
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.

import string
import keyword

text = input("Enter a string: ")

for i, l in enumerate(text):
    if i == 0:
        if l != '_' and not l.islower():
            print(False)
            break

    elif l != '_' and not l.islower() and not l.isdigit():
        print(False)
        break
else:
    if text in keyword.kwlist:
        print(False)
    else:
        print(True)