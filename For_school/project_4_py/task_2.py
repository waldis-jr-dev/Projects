string = input('Enter string: ')
data = {}
for i in string:
    if i not in data.keys():
        data[i] = 1
    else:
        data[i] += 1
answ = ''
num = 0
for key, value in data.items():
    if value > num:
        answ = key
        num = value
print(answ)
