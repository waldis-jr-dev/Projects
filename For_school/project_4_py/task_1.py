def check(string):
    open = 0
    close = 0
    for i in string:
        if i == '(':
            open += 1
        if i == ')':
            close += 1
        if close - open > 0:
            return 'Incorrect !'

    if close - open == 0:
        return 'All right )'
    else:
        return 'Incorrect !'


print(check(input('Enter string: ')))
