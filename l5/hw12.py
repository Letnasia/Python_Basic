# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

import string

text = str(input("Enter a string: "))
res = text.title()
for l in string.punctuation:
    res = res.replace(l, '')
if ' ' in res:
    res = res.replace(' ', '')

res = '#' + res[:140]
print(res)

