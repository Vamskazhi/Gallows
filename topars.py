print
soup.title  # <title>Python 3 - Программирование на Python 3</title>
print
soup.title.string  # Python 3 - Программирование на Python 3

# Содержимое мета полей
for meta in soup.find_all('meta'):
    print(meta.get('content'))