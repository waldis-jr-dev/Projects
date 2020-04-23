calc  = int(input('How many users : '))
data = []
for _ in range(calc):
    data.append(input('Enter name : '))
data.sort()
print(data)