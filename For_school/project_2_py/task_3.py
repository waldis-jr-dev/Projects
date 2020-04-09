'''Вивести на екран великі латинські літери, що входять до заданого рядка'''

import string
str1 = input('Enter string: ')
for i in str1:
    if i in string.ascii_uppercase:
        print(i)
