data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(1,len(data)+1):
    if i % 3 == 0:
        data[i-1] = 100
print(data)
