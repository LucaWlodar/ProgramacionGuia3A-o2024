import webbrowser, requests

cont = 0
data = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
data.raise_for_status
data = data.textv.upper()

file = open('romeo.txt', 'w')
for chunk in data:
    if 'A' <= chunk <= 'Z' and cont < 5000:
        file.write(chunk)
        cont += 1
