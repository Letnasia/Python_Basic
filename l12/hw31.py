original_file = open("draft.html", "r", encoding="utf-8")
cleaned_file = open("cleaned.txt", "w", encoding="utf-8")
html = original_file.read()

while True:
    start_at = html.find('<')
    if start_at == -1:
        break
    end_at = html.find('>', start_at)
    html = html[:start_at] + html[end_at + 1:]

strings_html = html.split('\n')
split_empty_str = [el for el in strings_html if not el.strip() == '']
html = '\n'.join(split_empty_str)
cleaned_file.write(html)
original_file.close()
cleaned_file.close()
