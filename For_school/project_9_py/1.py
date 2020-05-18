queue = []
for i in range(7):
    queue.append(input('Enter : '))
print(queue[0])
print(queue.pop())
print(queue.__sizeof__())