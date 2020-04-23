data = input('Enter your initials : ')
data = data.split()
#task_1
print(data[0],data[1][0],data[2][0])
#task_2
calc = 0
for i in data[0]:
    if i in 'Аа':
        calc += 1
print(calc)
#task_3
print(f"{data[0][0]}.{data[1][0]}.{data[2][0]}.")
#task_4
print(data[0],len(data[1]))
