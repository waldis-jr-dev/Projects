while True:
    print('Щоб завершити ввід оцінок введіть крапку (.) \n')
    marks = 0
    count = 0
    while True:
        mark = input('Введіть оцінку : ')
        if mark == '.':
            break
        if mark.isdigit():
            marks += float(mark)
            count += 1
        else:
            print('Неправильні вхідні данні !')
    print(f'\nСередня оцінка : {marks/count}\n')
