let = input('Enter letter : ')
string = input('Enter string : ')
place = 0
for i in range(len(string)):
    if string[i] == let:
        place = i
print(place)input('Enter string : ')