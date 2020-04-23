data = input('Enter string : ')
words = []
word = ''
for i in data:
    if i not in ', .':
        word += i
    else:
        words.append(word)
        word = ''
max_len = 0
for i in words:
    if len(i) > max_len:
        max_len = len(i)
        word = i
print(word)
