'''Замінити у рядку кожну крапку трьома крапками'''

string = list(input('Enter string: '))
for i in range(len(string)):
    if string[i] == '.':
        string[i] = '...'
answ = ''
for i in string:
    answ += i
print(answ)
