string = list(input('Enter string : '))
ch_let = input('Уnter the letter you want to change : ')
let = input('Enter letter : ')
for i in range(len(string) - 1):
    if string[i] == ch_let:
        string[i+1] = let
out = ''.join(string)
print(out)
