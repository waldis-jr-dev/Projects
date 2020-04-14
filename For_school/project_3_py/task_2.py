let = input('Enter letter : ')
string = input('Enter string : ')
for i in range(len(string)):
    if string[i] == let:
        print(i)
        break