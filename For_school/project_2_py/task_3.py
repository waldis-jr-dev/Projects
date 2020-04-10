'''Вивести на екран великі латинські літери, що входять до заданого рядка'''

import string
for i in input('Enter string: '):
    if i in string.ascii_uppercase:
        print(i)
