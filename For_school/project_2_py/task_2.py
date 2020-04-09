'''У заданому рядку всі символи '0' замінити на '1' та навпаки'''

string = list(input('Enter string: '))
for i in range(len(string)):
    if string[i] == '0':
        string[i] = '1'
    elif string[i] == '1':
        string[i] = '0'
answ = ''
for i in string:
    answ += i
print(answ)