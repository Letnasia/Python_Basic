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