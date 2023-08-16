def popular_words(text, words):
    result = dict()
    text_words = text.lower().split()
    for el in words:
        counts = text_words.count(el)
        result[el] = counts
    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')

